import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def load_and_engineer(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    # Drop near-empty field
    if 'car' in df.columns:
        df = df.drop(columns=['car'])

    age_map = {
        'below21': 18, '21': 21, '26': 26, '31': 31,
        '36': 36, '41': 41, '46': 46, '50plus': 55,
    }
    income_map = {
        'Less than $12500': 6250,
        '$12500 - $24999': 18750,
        '$25000 - $37499': 31250,
        '$37500 - $49999': 43750,
        '$50000 - $62499': 56250,
        '$62500 - $74999': 68750,
        '$75000 - $87499': 81250,
        '$87500 - $99999': 93750,
        '$100000 or More': 110000,
    }
    time_map = {'7AM': 7, '10AM': 10, '2PM': 14, '6PM': 18, '10PM': 22}
    visit_map = {'never': 0, 'less1': 0.5, '1~3': 2, '4~8': 6, 'gt8': 9}

    map_specs = [
        ('age', age_map),
        ('income', income_map),
        ('time', time_map),
        ('Bar', visit_map),
        ('CoffeeHouse', visit_map),
        ('CarryAway', visit_map),
        ('RestaurantLessThan20', visit_map),
        ('Restaurant20To50', visit_map),
    ]
    for col, mapper in map_specs:
        if col in df.columns:
            df[f'{col}_num'] = df[col].map(mapper)

    if {'direction_same', 'direction_opp'}.issubset(df.columns):
        df['direction_consistency'] = df['direction_same'] - df['direction_opp']

    if 'Y' in df.columns:
        df = df.drop(columns=['Y'])

    return df


def build_features(df: pd.DataFrame):
    num_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
    cat_cols = [c for c in df.columns if c not in num_cols]

    num_pipe = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler(with_mean=False)),
    ])
    cat_pipe = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore')),
    ])

    pre = ColumnTransformer([
        ('num', num_pipe, num_cols),
        ('cat', cat_pipe, cat_cols),
    ])
    return pre.fit_transform(df)


def evaluate_k(X, k_min: int = 2, k_max: int = 10, random_state: int = 42):
    k_values = list(range(k_min, k_max + 1))
    inertias = []
    silhouettes = []

    for k in k_values:
        model = KMeans(n_clusters=k, n_init=20, random_state=random_state)
        labels = model.fit_predict(X)
        inertias.append(model.inertia_)
        silhouettes.append(
            silhouette_score(X, labels, metric='euclidean', sample_size=4000, random_state=random_state)
        )

    # Knee by maximum distance to line between endpoints
    x = np.array(k_values)
    y = np.array(inertias)
    line = np.array([x[-1] - x[0], y[-1] - y[0]], dtype=float)
    norm = np.linalg.norm(line)
    dists = []
    for xi, yi in zip(x, y):
        p = np.array([xi - x[0], yi - y[0]], dtype=float)
        dists.append(abs(line[0] * p[1] - line[1] * p[0]) / norm)

    elbow_k = int(x[np.argmax(dists)])
    silhouette_k = int(x[np.argmax(silhouettes)])

    return k_values, inertias, silhouettes, elbow_k, silhouette_k


def main():
    data_path = '../data/in-vehicle-coupon-dataset.csv'
    df = load_and_engineer(data_path)
    X = build_features(df)
    k_values, inertias, silhouettes, elbow_k, silhouette_k = evaluate_k(X)

    print('k,inertia,silhouette')
    for k, i, s in zip(k_values, inertias, silhouettes):
        print(f'{k},{i:.2f},{s:.4f}')
    print(f'elbow_k={elbow_k}')
    print(f'silhouette_best_k={silhouette_k}')


if __name__ == '__main__':
    main()

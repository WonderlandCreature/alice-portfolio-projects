import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import sparse
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# =========================
# Step 1: Load Data
# =========================
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


# =========================
# Step 2: Basic Cleaning
# =========================
def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    # Drop near-empty column (~99% missing)
    if "car" in out.columns:
        miss_rate = out["car"].isna().mean()
        if miss_rate > 0.95:
            out = out.drop(columns=["car"])

    return out


# =========================
# Step 3: Feature Engineering
# =========================
def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    age_map = {
        "below21": 18, "21": 21, "26": 26, "31": 31,
        "36": 36, "41": 41, "46": 46, "50plus": 55,
    }
    income_map = {
        "Less than $12500": 6250,
        "$12500 - $24999": 18750,
        "$25000 - $37499": 31250,
        "$37500 - $49999": 43750,
        "$50000 - $62499": 56250,
        "$62500 - $74999": 68750,
        "$75000 - $87499": 81250,
        "$87500 - $99999": 93750,
        "$100000 or More": 110000,
    }
    time_map = {"7AM": 7, "10AM": 10, "2PM": 14, "6PM": 18, "10PM": 22}
    visit_map = {"never": 0, "less1": 0.5, "1~3": 2, "4~8": 6, "gt8": 9}

    mapping_specs = [
        ("age", age_map),
        ("income", income_map),
        ("time", time_map),
        ("Bar", visit_map),
        ("CoffeeHouse", visit_map),
        ("CarryAway", visit_map),
        ("RestaurantLessThan20", visit_map),
        ("Restaurant20To50", visit_map),
    ]

    for col, mapper in mapping_specs:
        if col in out.columns:
            out[f"{col}_num"] = out[col].map(mapper)

    if {"direction_same", "direction_opp"}.issubset(out.columns):
        out["direction_consistency"] = out["direction_same"] - out["direction_opp"]

    return out


# =========================
# Step 4: Preprocess Matrix
# =========================
def preprocess_for_clustering(df: pd.DataFrame):
    # Remove target if present (unsupervised clustering)
    X = df.drop(columns=["Y"]) if "Y" in df.columns else df.copy()

    num_cols = [c for c in X.columns if pd.api.types.is_numeric_dtype(X[c])]
    cat_cols = [c for c in X.columns if c not in num_cols]

    num_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler(with_mean=False)),
    ])
    cat_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ])

    pre = ColumnTransformer([
        ("num", num_pipe, num_cols),
        ("cat", cat_pipe, cat_cols),
    ])

    X_processed = pre.fit_transform(X)
    if not sparse.issparse(X_processed):
        X_processed = sparse.csr_matrix(X_processed)

    return X_processed, pre


# =========================
# Step 5: Elbow + Silhouette
# =========================
def evaluate_k(
    X_processed,
    k_min: int = 2,
    k_max: int = 10,
    random_state: int = 42,
    silhouette_sample_size: int = 4000,
):
    k_values = list(range(k_min, k_max + 1))
    inertias = []
    silhouettes = []

    for k in k_values:
        km = KMeans(n_clusters=k, n_init=20, random_state=random_state)
        labels = km.fit_predict(X_processed)

        inertias.append(km.inertia_)
        silhouettes.append(
            silhouette_score(
                X_processed,
                labels,
                metric="euclidean",
                sample_size=min(silhouette_sample_size, X_processed.shape[0]),
                random_state=random_state,
            )
        )

    return k_values, inertias, silhouettes


# =========================
# Step 6: Pick Elbow k
# =========================
def elbow_k_by_max_distance(k_values, inertias):
    x = np.array(k_values, dtype=float)
    y = np.array(inertias, dtype=float)

    line = np.array([x[-1] - x[0], y[-1] - y[0]], dtype=float)
    denom = np.linalg.norm(line)

    distances = []
    for xi, yi in zip(x, y):
        point = np.array([xi - x[0], yi - y[0]], dtype=float)
        d = abs(line[0] * point[1] - line[1] * point[0]) / denom
        distances.append(d)

    best_idx = int(np.argmax(distances))
    return int(x[best_idx])


# =========================
# Step 7: Plot Curves
# =========================
def plot_results(k_values, inertias, silhouettes, elbow_k, sil_k):
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    axes[0].plot(k_values, inertias, marker="o")
    axes[0].axvline(elbow_k, linestyle="--", color="red", label=f"Elbow k={elbow_k}")
    axes[0].set_title("Elbow Method")
    axes[0].set_xlabel("k")
    axes[0].set_ylabel("Inertia (WCSS)")
    axes[0].legend()

    axes[1].plot(k_values, silhouettes, marker="o")
    axes[1].axvline(sil_k, linestyle="--", color="green", label=f"Silhouette best k={sil_k}")
    axes[1].set_title("Silhouette Score")
    axes[1].set_xlabel("k")
    axes[1].set_ylabel("Silhouette")
    axes[1].legend()

    plt.tight_layout()
    plt.savefig("k_selection_plots.png", dpi=150)
    plt.close(fig)


# =========================
# Step 8: Report Text
# =========================
def print_report(df_raw, df_clean, k_values, inertias, silhouettes, elbow_k, sil_k):
    print("\n" + "=" * 72)
    print("REPORT: K-MEANS K IDENTIFICATION (ELBOW + SILHOUETTE)")
    print("=" * 72)

    print("\n1) Data Overview")
    print(f"- Original shape: {df_raw.shape}")
    print(f"- Cleaned shape:  {df_clean.shape}")
    if "car" in df_raw.columns and "car" not in df_clean.columns:
        miss_rate = df_raw["car"].isna().mean() * 100
        print(f"- Dropped 'car' due to missing rate: {miss_rate:.2f}%")

    print("\n2) Preprocessing and Feature Engineering")
    print("- Impute missing values (numeric: median, categorical: most frequent)")
    print("- One-hot encode categorical variables")
    print("- Scale numeric variables")
    print("- Added engineered numeric features (age_num, income_num, time_num, visit-frequency nums)")
    print("- Added direction_consistency")

    print("\n3) K Evaluation Results")
    print("k\tinertia\tsilhouette")
    for k, i, s in zip(k_values, inertias, silhouettes):
        print(f"{k}\t{i:.2f}\t{s:.4f}")

    print("\n4) Method Conclusions")
    print(f"- Elbow suggested k: {elbow_k}")
    print(f"- Silhouette best k: {sil_k}")

    if elbow_k == sil_k:
        final_k = elbow_k
        reason = "Both methods agree."
    else:
        # For actionable segmentation, choose elbow if conflict.
        final_k = elbow_k
        reason = "Methods differ; elbow chosen for richer, actionable segmentation granularity."

    print("\n5) Final Recommended k")
    print(f"- Recommended k: {final_k}")
    print(f"- Reason: {reason}")
    print("=" * 72 + "\n")


# =========================
# Main
# =========================
def main():
    data_path = "../data/in-vehicle-coupon-dataset.csv"

    df_raw = load_data(data_path)
    df_clean = basic_cleaning(df_raw)
    df_feat = feature_engineering(df_clean)

    X_processed, _ = preprocess_for_clustering(df_feat)

    k_values, inertias, silhouettes = evaluate_k(
        X_processed,
        k_min=2,
        k_max=10,
        random_state=42,
        silhouette_sample_size=4000,
    )

    elbow_k = elbow_k_by_max_distance(k_values, inertias)
    sil_k = int(k_values[int(np.argmax(silhouettes))])

    plot_results(k_values, inertias, silhouettes, elbow_k, sil_k)
    print_report(df_raw, df_clean, k_values, inertias, silhouettes, elbow_k, sil_k)


if __name__ == "__main__":
    main()

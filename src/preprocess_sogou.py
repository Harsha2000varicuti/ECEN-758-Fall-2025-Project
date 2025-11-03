import os
from datasets import load_dataset
import pandas as pd

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(OUT_DIR, exist_ok=True)

def main():
    ds = load_dataset("community-datasets/sogou_news")

    train_df = pd.DataFrame(ds["train"])
    test_df = pd.DataFrame(ds["test"])

    # sanity check
    expected_cols = {"title", "content", "label"}
    assert expected_cols.issubset(train_df.columns), f"Missing columns: {expected_cols - set(train_df.columns)}"

    train_path = os.path.join(OUT_DIR, "sogou_train.csv")
    test_path = os.path.join(OUT_DIR, "sogou_test.csv")

    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)

if __name__ == "__main__":
    main()
from pathlib import Path
import sys
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Online Store Analytics
# Run: python run_analysis.py
# Input CSV must be next to this script.
# Reports and charts are saved in ./output.

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "online_store_dataset.csv"
OUTPUT_DIR = BASE_DIR / "output"
CHARTS_DIR = OUTPUT_DIR / "charts"

REQUIRED_COLUMNS = {
    "date", "country", "device", "continent", "channel",
    "test", "test_group", "event_name", "value"
}


def main():
    if not DATA_FILE.exists():
        print(f"ERROR: Dataset not found: {DATA_FILE}")
        print("Place online_store_dataset.csv next to run_analysis.py.")
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)

    print("Loading dataset...")
    try:
        df = pd.read_csv(DATA_FILE)
    except Exception as exc:
        print(f"ERROR: Could not read CSV: {exc}")
        sys.exit(1)

    print(f"Rows loaded: {len(df):,}")
    print(f"Columns found: {len(df.columns)}")

    missing_columns = sorted(REQUIRED_COLUMNS - set(df.columns))
    if missing_columns:
        print("ERROR: Required columns are missing:")
        for column in missing_columns:
            print(f"  - {column}")
        sys.exit(1)

    raw_df = df.copy()

    text_columns = ["country", "device", "continent", "channel", "event_name"]
    for column in text_columns:
        df[column] = df[column].astype("string").str.strip()

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df["test"] = pd.to_numeric(df["test"], errors="coerce")
    df["test_group"] = pd.to_numeric(df["test_group"], errors="coerce")

    duplicate_rows = int(raw_df.duplicated().sum())
    invalid_dates = int(df["date"].isna().sum())
    invalid_values = int(df["value"].isna().sum())
    invalid_tests = int(df["test"].isna().sum())
    invalid_test_groups = int(df["test_group"].isna().sum())

    quality_rows = [
        ("row_count", len(df), "Rows loaded from the input CSV"),
        ("column_count", len(df.columns), "Columns loaded from the input CSV"),
        ("duplicate_full_rows", duplicate_rows, "Exact duplicate rows in the original data"),
        ("invalid_or_missing_dates", invalid_dates, "Dates that could not be parsed"),
        ("invalid_or_missing_value", invalid_values, "Values that could not be converted to numbers"),
        ("invalid_or_missing_test", invalid_tests, "Test values that could not be converted to numbers"),
        ("invalid_or_missing_test_group", invalid_test_groups, "Test group values that could not be converted to numbers"),
    ]
    for column in df.columns:
        quality_rows.append((
            f"missing_values::{column}",
            int(df[column].isna().sum()),
            "Missing values after type conversion"
        ))

    pd.DataFrame(
        quality_rows, columns=["check", "result", "description"]
    ).to_csv(OUTPUT_DIR / "data_quality_report.csv", index=False)

    overview = pd.DataFrame({
        "column": df.columns,
        "data_type": [str(df[c].dtype) for c in df.columns],
        "missing_values": [int(df[c].isna().sum()) for c in df.columns],
        "unique_values": [int(df[c].nunique(dropna=True)) for c in df.columns],
    })
    overview.to_csv(OUTPUT_DIR / "data_overview.csv", index=False)

    # Event counts and value totals. value is not assumed to mean revenue.
    events = (
        df.groupby("event_name", dropna=False)
        .agg(rows=("event_name", "size"), total_value=("value", "sum"))
        .reset_index()
        .sort_values("rows", ascending=False)
    )
    events.to_csv(OUTPUT_DIR / "events_summary.csv", index=False)

    by_device = (
        df.groupby(["device", "event_name"], dropna=False)
        .agg(rows=("event_name", "size"), total_value=("value", "sum"))
        .reset_index()
        .sort_values(["event_name", "rows"], ascending=[True, False])
    )
    by_device.to_csv(OUTPUT_DIR / "events_by_device.csv", index=False)

    by_channel = (
        df.groupby(["channel", "event_name"], dropna=False)
        .agg(rows=("event_name", "size"), total_value=("value", "sum"))
        .reset_index()
        .sort_values(["event_name", "rows"], ascending=[True, False])
    )
    by_channel.to_csv(OUTPUT_DIR / "events_by_channel.csv", index=False)

    by_country = (
        df.groupby(["country", "event_name"], dropna=False)
        .agg(rows=("event_name", "size"), total_value=("value", "sum"))
        .reset_index()
        .sort_values(["country", "rows"], ascending=[True, False])
    )
    by_country.to_csv(OUTPUT_DIR / "events_by_country.csv", index=False)

    test_groups = (
        df.groupby(["test_group", "event_name"], dropna=False)
        .agg(rows=("event_name", "size"), total_value=("value", "sum"))
        .reset_index()
        .sort_values(["test_group", "rows"], ascending=[True, False])
    )
    test_groups.to_csv(OUTPUT_DIR / "test_groups_summary.csv", index=False)

    dated_df = df.dropna(subset=["date"]).copy()
    daily_events = (
        dated_df.groupby([pd.Grouper(key="date", freq="D"), "event_name"], dropna=False)
        .agg(rows=("event_name", "size"), total_value=("value", "sum"))
        .reset_index()
        .sort_values(["date", "event_name"])
    )
    daily_events.to_csv(OUTPUT_DIR / "daily_events.csv", index=False)

    extra_summaries = {
        "events_by_continent.csv": ["continent", "event_name"],
        "events_by_test.csv": ["test", "event_name"],
        "events_by_test_group.csv": ["test_group", "event_name"],
    }
    for filename, group_columns in extra_summaries.items():
        summary = (
            df.groupby(group_columns, dropna=False)
            .agg(rows=("event_name", "size"), total_value=("value", "sum"))
            .reset_index()
            .sort_values(group_columns)
        )
        summary.to_csv(OUTPUT_DIR / filename, index=False)

    # Charts show row counts, not the sum of `value`.
    device_pivot = df.pivot_table(
        index="event_name", columns="device", values="value",
        aggfunc="size", fill_value=0
    )
    if not device_pivot.empty:
        ax = device_pivot.sort_index().plot(kind="bar")
        ax.set_title("Events by Device")
        ax.set_xlabel("Event")
        ax.set_ylabel("Number of Rows")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(CHARTS_DIR / "events_by_device.png", dpi=150)
        plt.close()

    channel_pivot = df.pivot_table(
        index="event_name", columns="channel", values="value",
        aggfunc="size", fill_value=0
    )
    if not channel_pivot.empty:
        ax = channel_pivot.sort_index().plot(kind="bar")
        ax.set_title("Events by Channel")
        ax.set_xlabel("Event")
        ax.set_ylabel("Number of Rows")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(CHARTS_DIR / "events_by_channel.png", dpi=150)
        plt.close()

    if not dated_df.empty:
        daily_counts = dated_df.groupby(pd.Grouper(key="date", freq="D")).size()
        ax = daily_counts.plot(kind="line")
        ax.set_title("Daily Event Rows")
        ax.set_xlabel("Date")
        ax.set_ylabel("Number of Rows")
        plt.tight_layout()
        plt.savefig(CHARTS_DIR / "daily_events.png", dpi=150)
        plt.close()

    print("\nAnalysis completed.")
    print(f"Rows: {len(df):,}")
    print(f"Exact duplicate rows: {duplicate_rows:,}")
    print(f"Invalid/missing dates: {invalid_dates:,}")
    print(f"Invalid/missing numeric values in value: {invalid_values:,}")
    print(f"Reports saved to: {OUTPUT_DIR}")
    print(f"Charts saved to: {CHARTS_DIR}")
    print("Created CSV reports:")
    for file_path in sorted(OUTPUT_DIR.glob("*.csv")):
        print(f"  - {file_path.name}")
    print("Created charts:")
    for file_path in sorted(CHARTS_DIR.glob("*.png")):
        print(f"  - {file_path.name}")


if __name__ == "__main__":
    main()

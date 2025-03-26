import pandas as pd


def categorical_summary(df: pd.DataFrame, columns: list[str]) -> None:
    csv_table = {
        "columns": ["variableName", "unique_classes", "missing_values", "class_proportions"],
        "rows": [],
    }

    for column in columns:
        class_proportion_filename = f"csv_results/class_proportions/{column}_class_proportions.csv"
        csv_table["rows"].append([
            column,
            df[column].nunique(),
            df[column].isna().sum(),
            class_proportion_filename
        ])

        class_dict = (df[column].value_counts(normalize=True) * 100).to_dict()
        class_proportion_df = pd.DataFrame(list(class_dict.items()), columns=["Class", "Proportion [%]"]).round(2)
        class_proportion_df.to_csv(class_proportion_filename, index=False)

    out_df = pd.DataFrame(csv_table["rows"], columns=csv_table["columns"])
    out_df.to_csv("csv_results/categorical_results.csv", index=False)

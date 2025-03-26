import pandas


def statistics_summary(df: pandas.DataFrame, columns: list[str]) -> None:
    csv_table = {
        "columns": ["variableName", "mean", "median", "min_value", "max_value", "std_deviation", "5th_percentile", "95th_percentile", "NA_values"],
        "rows": [],
    }

    for column in columns:
        csv_table["rows"].append([
            column,
            df[column].mean(),
            df[column].median(),
            df[column].min(),
            df[column].max(),
            df[column].std(),
            df[column].quantile(0.05),
            df[column].quantile(0.95),
            df[column].isna().sum()
        ])

    out_df = pandas.DataFrame(csv_table["rows"], columns=csv_table["columns"])
    out_df.to_csv("csv_results/numerical_results.csv")

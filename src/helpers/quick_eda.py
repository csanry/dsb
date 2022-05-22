def quick_eda(df):

    rows, cols = df.shape
    print(
        f"""
    Dataframe has {rows} rows and {cols} cols
    {df.info()}
    """
    )
    display(df.describe().T)
    display(df.head(5))

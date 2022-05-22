def standardize_cols(column_list):

    return [
        col.lower().strip().replace(" ", "_").replace("-", "_") for col in column_list
    ]

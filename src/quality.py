def calculate_quality(df):

    total_cells = df.size

    missing = df.isnull().sum().sum()

    duplicates = df.duplicated().sum()

    score = 100 - ((missing + duplicates) / total_cells * 100)

    return round(score, 2)
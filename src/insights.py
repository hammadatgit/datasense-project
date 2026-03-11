def generate_insights(region_table, monthly_table):
    """
    Returns simple automated insights from analysis tables
    """
    # Top revenue region
    top_region = region_table.sort_values(
        "revenue", ascending=False
    ).iloc[0]

    # Month with highest sales
    best_month = monthly_table.idxmax()

    insights = []
    insights.append(
        f"Top revenue region is {top_region['region']} with revenue {top_region['revenue']}"
    )
    insights.append(
        f"Highest sales month is {best_month}"
    )

    return insights
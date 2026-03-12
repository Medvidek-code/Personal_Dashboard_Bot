def generate_report(weather, news, stocks):
    report = "# Weather Report\n\n"
    report += f"Weather: {weather}\n\n"
    report += "# News Report\n\n"
    report += f"News: {news}\n\n"
    report += "# Stock Report\n\n"
    report += f"Stocks: {stocks}\n\n"
    return report

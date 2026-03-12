from weather import get_weather
from stocks import get_stock_prices
from news import get_news
from report_generator import generate_report


def main():
    weather = get_weather()
    news = get_news()
    stocks = get_stock_prices()
    report = generate_report(weather, news, stocks)

    with open("README.md", "w") as f:
        f.write(report)


if __name__ == "__main__":
    main()

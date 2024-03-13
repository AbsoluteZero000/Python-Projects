import requests
from bs4 import BeautifulSoup




if __name__ == "__main__":
    url = "https://books.toscrape.com/"
    try:
        response = requests.get(url, timeout=(10, 10))
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        books = soup.find_all("article")

        for book in books:
            title = book.find("h3").find("a").get("title", "[Title not found]")
            rating = book.p.get("class")[1].strip()
            price = book.find_all("p", class_="price_color")[0].text.strip()
            print(f"The book: {title} of price {price} has the rating {rating} stars.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the data: {e}")

# Testing the implementation
if __name__ == "__main__":
    test_url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"

    print("Fetching the page for the first time:")
    print(get_page(test_url))

    print("\nFetching the page for the second time (should be cached):")
    print(get_page(test_url))

    print("\nAccess count:")
    redis_client = redis.Redis()
    print(redis_client.get(f"count:{test_url}").decode('utf-8'))

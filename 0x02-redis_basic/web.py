#!/usr/bin/env python3
"""
Module web
"""

import redis
import requests
from typing import Callable
from functools import wraps

# Initialize Redis client
redis_client = redis.Redis()


def cache_response(method: Callable) -> Callable:
    """
    Decorator to cache the response of a function with an expiration time.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper function to cache the response and track access count.
        """
        cache_key = f"cache:{url}"
        count_key = f"count:{url}"

        # Increment the access count
        redis_client.incr(count_key)

        # Check if the response is cached
        cached_response = redis_client.get(cache_key)
        if cached_response:
            return cached_response.decode('utf-8')

        # Fetch the response and cache it with an expiration time of 10 seconds
        response = method(url)
        redis_client.setex(cache_key, 10, response)
        return response

    return wrapper


@cache_response
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a particular URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text


# Example usage
if __name__ == "__main__":
    url = "http://google.com"

    # First call - should fetch and cache
    print(get_page(url))  # This should fetch the page

    # Second call - should return cached response
    print(get_page(url))  # This should return cached response

    # Check the count
    print(redis_client.get(f"count:{url}").decode('utf-8'))  # This should print the count

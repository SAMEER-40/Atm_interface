# app/cache.py
import time

print("cache.py loaded")

# In-memory cache
cache = {}

def cache_response(query, response, ttl):
    print("cache_response called")
    expiration = time.time() + ttl
    cache[query] = (response, expiration)

def get_cached_response(query):
    print("get_cached_response called")
    if query in cache:
        response, expiration = cache[query]
        if time.time() < expiration:
            return response
        else:
            del cache[query]
    return None

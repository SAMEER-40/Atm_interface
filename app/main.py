# app/main.py
from flask import Flask, request, jsonify
from app.balancer import handle_query
from app.cache import get_cached_response, cache_response, cache
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


@app.route('/dns-query', methods=['GET'])
def dns_query():
    logging.debug("Received request to /dns-query")
    query = request.args.get('query')
    if not query:
        logging.debug("No query parameter provided")
        return jsonify({'error': 'No query parameter provided'}), 400

    cached_response = get_cached_response(query)
    if cached_response:
        logging.debug("Returning cached response")
        return cached_response

    response = handle_query(query)
    cache_response(query, response, ttl=300)
    logging.debug("Returning fresh DNS response")
    return response


@app.route('/status', methods=['GET'])
def status():
    logging.debug("Received request to /status")
    return jsonify({'cache_size': len(cache)})


@app.route('/', methods=['GET'])
def index():
    logging.debug("Received request to root /")
    return jsonify({'message': 'Welcome to the DNS Load Balancer and Caching System'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

import dns.message
import dns.query
import random
import dns.resolver
import logging

from flask import jsonify

dns_servers = ['8.8.8.8', '8.8.4.4', '1.1.1.1']


def get_dns_server():
    """Select a random DNS server from the list."""
    return random.choice(dns_servers)


def query_dns(domain):
    """Create and send a DNS query, then return the response."""
    try:
        query = dns.message.make_query(domain, dns.rdatatype.ANY)
        server = get_dns_server()
        response = dns.query.udp(query, server)

        # Validate the response
        if response and len(response.to_wire()) > 0:
            return response
        else:
            logging.warning("Received empty or truncated response.")
            return None
    except dns.exception.DNSException as e:
        logging.error(f"DNS exception: {e}")
        return None
    except Exception as e:
        logging.error(f"General exception: {e}")
        return None


def handle_query(query):
    try:
        resolver = dns.resolver.Resolver()
        response = resolver.resolve(query, 'A')  # Querying A records
        return jsonify({'response': [str(rdata) for rdata in response]})
    except dns.resolver.NoAnswer:
        return jsonify({'error': 'No answer for the query'}), 404
    except dns.exception.Timeout:
        return jsonify({'error': 'DNS query timed out'}), 504
    except Exception as e:
        logging.error(f"General exception: {e}")
        return None

import dns.message
import dns.query
import random
import logging

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


def handle_query(domain):
    """Handle a DNS query and return the response in text format."""
    response = query_dns(domain)
    if response:
        return response.to_text()
    return None

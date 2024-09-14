# app/balancer.py
import random
import dns.query
import dns.message

# List of DNS servers to use
dns_servers = ['8.8.8.8', '8.8.4.4', '1.1.1.1']

def get_dns_server():
    return random.choice(dns_servers)

def handle_query(query):
    message = dns.message.from_wire(query.encode())
    server = get_dns_server()
    response = dns.query.udp(message, server)
    return response.to_wire().decode()

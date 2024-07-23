server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}
def get_server_ip(server_name):
    return server_config.get(server_name, {}).get('ip', 'Server not found')  #function for retrieval
server_name = 'server1'
ip = get_server_ip(server_name)
print(f"{server_name} ip: {ip} ")

############################################

def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')  #function for retrieval

server_name = 'server2'
status = get_server_status(server_name)
print(f"{server_name} stauts: {status}")

############################################

def get_server_port(server_name):
    return server_config.get(server_name, {}).get('port', 'Server not found')  #function for retrieval

server_name = 'server3'
port = get_server_port(server_name)
print(f"{server_name} port: {port}")



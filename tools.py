def greet(tool):
    print(f"Welcome to the {tool} scanner")

def ping_target(domain):
    import socket
    ip=socket.gethostbyname(domain)
    print(f"{domain} -> {ip}")
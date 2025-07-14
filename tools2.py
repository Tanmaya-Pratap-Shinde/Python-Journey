def save_ping(domain):
    import socket
    ip = socket.gethostbyname(domain)
    with open("recon_log2.txt","a") as file:
        file.write(f"{domain} -> {ip}\n")
    print(f"Saved: {domain} -> {ip}")
    
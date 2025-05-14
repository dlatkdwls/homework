mport socket

HOST = '127.0.0.1'
PORT = 9999

def main():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cli:
                    cli.connect((HOST, PORT))

                            # 1) Download request
                                    filename = 'downloaded.bin'
                                            cli.sendall(f"GET {filename}\n".encode())
                                                    print(f"[Client] Sent request: GET {filename}")

                                                            # 2) Handle reading (header)
                                                                    header = b''
                                                                            while not header.endswith(b'\n'):
                                                                                            chunk = cli.recv(1)
                                                                                                        if not chunk:
                                                                                                                            print("[Client] No response from server.")
                                                                                                                                            return
                                                                                                                                                    header += chunk

                                                                                                                                                            # Extract status and length
                                                                                                                                                                    line = header.decode().rstrip("\n")
                                                                                                                                                                            status, rest = line.split(' ', 1)

                                                                                                                                                                                    if status == 'OK':
                                                                                                                                                                                                    length = int(rest)
                                                                                                                                                                                                                print(f"[Client] Server OK, length = {length}")

                                                                                                                                                                                                                            # 3) Read body
                                                                                                                                                                                                                                        data = b''
                                                                                                                                                                                                                                                    while len(data) < length:
                                                                                                                                                                                                                                                                        data += cli.recv(length - len(data))

                                                                                                                                                                                                                                                                                    # 4) Save file
                                                                                                                                                                                                                                                                                                out_name = 'downloaded_' + filename
                                                                                                                                                                                                                                                                                                            with open(out_name, 'wb') as f:
                                                                                                                                                                                                                                                                                                                                f.write(data)
                                                                                                                                                                                                                                                                                                                                            print(f"[Client] Saved {out_name} ({length} bytes)")

                                                                                                                                                                                                                                                                                                                                                    elif status == 'ERROR':
                                                                                                                                                                                                                                                                                                                                                                    # rest contains error message
                                                                                                                                                                                                                                                                                                                                                                                print(f"[Client] Download failed: {rest}")

                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                        print(f"[Client] Unknown response: {line}")

                                                                                                                                                                                                                                                                                                                                                                                                        if __name__ == '__main__':
                                                                                                                                                                                                                                                                                                                                                                                                                main()

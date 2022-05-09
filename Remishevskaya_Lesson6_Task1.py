with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    data = []
    for line in fr:
        remote_addr = line.split()[0]
        request_type = line.split()[5].replace('"', '')
        requested_res = line.split()[6]
        data.append((remote_addr, request_type, requested_res))
print(data)

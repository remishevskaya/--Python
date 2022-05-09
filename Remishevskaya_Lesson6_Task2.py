with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    chunk_size = 8589934592  # 8 гб в байтах
    data = []
    spam_request = {}
    while True:
        r = fr.readlines(chunk_size)
        if not r:
            break
        for log in r:
            spam_request.setdefault(log.split(' ')[0], 0)
            spam_request[log.split(' ')[0]] += 1
    top_spam = sorted(spam_request.items(), key = lambda elem: elem[1], reverse=True)
    print(f'IP-адрес спамера: {top_spam[0][0]}, Количество запросов: {top_spam[0][1]}')

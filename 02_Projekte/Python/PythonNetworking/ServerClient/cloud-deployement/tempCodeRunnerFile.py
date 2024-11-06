HOST_IP = socket.gethostbyname(socket.gethostname())
redis_client = redis.StrictRedis(host=HOST_IP, port=6379, password="1234", decode_responses=True)
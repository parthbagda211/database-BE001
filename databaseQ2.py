import redis
from rediscluster import RedisCluster

def connect_redis():
    startup_nodes = [
        {"host": "127.0.0.1", "port": "7001"},
        {"host": "127.0.0.1", "port": "7002"},
        {"host": "127.0.0.1", "port": "7003"},
    ]
    return RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

def put(client, key, value):
    client.set(key, value)
    print(f"Set {key} to {value}")

def get(client, key):
    value = client.get(key)
    print(f"Get {key}: {value}")
    return value

def delete(client, key):
    client.delete(key)
    print(f"Deleted {key}")

def main():
    client = connect_redis()

    # Put operations
    put(client, "key1", "value1")
    put(client, "key2", "value2")

    # Get operations
    get(client, "key1")
    get(client, "key2")

    # Delete operation
    delete(client, "key1")
    get(client, "key1")

if __name__ == "__main__":
    main()


class CacheManage:
    cache = {}
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return None
    def get_value(self,key):
        if key in self.cache:
            return self.cache[key]
        else:
            print('Not found')
            return None
    def save_value(self,key,value):
        self.cache[key] = str(value)

with CacheManage() as cache:
    data = cache.get_value('user_session') # Not in cache right now
    if data is None:
        value = "SessionData123"
        cache.save_value('user_session', value)



with CacheManage() as cache:
    data = cache.get_value('user_session') # Now in cache
    print(f"Retrieved data in second block: {data}")
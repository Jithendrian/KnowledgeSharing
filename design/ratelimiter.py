import time

class SimpleRateLimiter:
    def __init__(self, rate, per):
        self.rate = rate
        self.per = per
        self.last_reset = time.time()
        self.count = 0

    def is_allowed(self):
        current_time = time.time()
        if current_time - self.last_reset > self.per:
            self.last_reset = current_time
            self.count = 0

        if self.count < self.rate:
            self.count += 1
            return True
        else:
            return False

rate = 5
per_second = 10
#5 requests are allowed in every 10 seconds
rate_limiter = SimpleRateLimiter(rate=rate, per=per_second)
request_interval = 1 # request_interval = 2, 1 request in every 2 seconds
number_of_requests = 20
for i in range(number_of_requests):
    if rate_limiter.is_allowed():
        print(f"Action {i + 1} allowed.")
    else:
        print(f"Action {i + 1} denied.")
    time.sleep(request_interval)

from collections import defaultdict
class Logger:

    def __init__(self):
        self.latest = defaultdict(lambda : -1)
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        past = self.latest[message]
        # first time
        if past == -1 :
            self.latest[message] = timestamp
            return True
        if timestamp >= past + 10:
            self.latest[message] = timestamp
            return True
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
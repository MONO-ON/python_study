
class Calculator:
    """
    계산기 클래스입니다.
    """
    result = 0
    
    def add(self, a):
        self.result += a
    
    def subtract(self, a):
        self.result -= a
    
    def multiplicated_by(self, a):
        self.result *= a
    
    def divided_by(self, a):
        self.result /= a
        
    def ac(self):
        self.result = 0

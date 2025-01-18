class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def addTime(self, other_time):
        total_minutes = (self.hours * 60 + self.minutes) + (other_time.hours * 60 + other_time.minutes)
        return Time(total_minutes // 60, total_minutes % 60)
    
    def displayTime(self):
        print(f"{self.hours} hours {self.minutes} minutes")
    
    def displayMinute(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"Total minutes: {total_minutes}")


time1 = Time(2, 50)
time2 = Time(1, 20)
result_time = time1.addTime(time2)
result_time.displayTime()
result_time.displayMinute()

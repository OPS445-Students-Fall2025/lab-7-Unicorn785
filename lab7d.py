#!/usr/bin/env python3
# Student ID: Pirajeen Kandasamy
class Time:

    def __init__(self,hour=12,minute=0,second=0):
        #constructor for time object
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        #Return time object (t) as a formatted string
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        #Add two time objests and return the sum
        self_sec = self.time_to_sec()
        t2_sec = t2.time_to_sec()
        sum = sec_to_time(self_sec + t2_sec)
        return sum

    def change_time(self, seconds):
        time_seconds = self.time_to_sec()
        nt = sec_to_time(time_seconds + seconds)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second 
        return None

    def time_to_sec(self):
        #convert a time object to a single number of seconds from mid-night
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def valid_time(self):
        #checks for the validity of the time
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

def sec_to_time(seconds):
    #convert a given number of seconds to a time object in HR:M:S
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

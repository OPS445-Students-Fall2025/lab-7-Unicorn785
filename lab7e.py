#!/usr/bin/env python3
# Student ID: Pirajeen Kandasamy

class Time:

    def __init__(self, hour=12, minute=0, second=0):
        #constructor for time object
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        #return a string representation for the object self
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):

        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def format_time(self):
        #Return time object (t) as a formatted string
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        #"Add two time objects and return the sum.
        total = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total)

    def change_time(self, seconds):
        #Change this time by adding seconds 
        total = self.time_to_sec() + seconds
        nt = sec_to_time(total)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second
        return None

    def time_to_sec(self):
        #convert a time object to a single integer representing the number of seconds from mid-night
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def valid_time(self):
        #check for the validity of the time object 
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True


DAY = 24 * 60 * 60

def sec_to_time(seconds):
    #convert a given number of seconds to a time object in hour, minute, second format
    seconds = seconds % DAY
    hour = seconds // 3600
    seconds = seconds % 3600
    minute = seconds // 60
    second = seconds % 60
    return Time(hour, minute, second)

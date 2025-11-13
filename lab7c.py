#!/usr/bin/env python3
# Student ID: Pirajeen Kandasamy

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string like HH:MM:SS"""
    return f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}"

#we are going to turn this into 34hr clock and covert everything into seconds
DAY = 24 * 60 * 60  # 86400 seconds per day


def time_to_sec(time):
    """Convert a time object to total seconds since midnight."""
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def sec_to_time(seconds):
    #Convert seconds since midnight to a Time object
    seconds = seconds % DAY 

    # calculate hours, minutes, seconds manually
    hour = seconds // 3600
    seconds = seconds % 3600
    minute = seconds // 60
    second = seconds % 60

    # create and return new Time object
    t = Time(hour, minute, second)
    return t


def sum_times(t1, t2):
    #Add two time objects and return the sum using base-seconds logic.
    total = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total)


def change_time(time, seconds):
    #add or subtract seconds directly
    total = time_to_sec(time) + seconds
    new_time = sec_to_time(total)
    time.hour = new_time.hour
    time.minute = new_time.minute
    time.second = new_time.second
    return None


def valid_time(t):
    """Check validity of a time object."""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.hour >= 24 or t.minute >= 60 or t.second >= 60:
        return False
    return True

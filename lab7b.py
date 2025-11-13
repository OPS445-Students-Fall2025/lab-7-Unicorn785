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

def sum_times(t1, t2):
    """Add two time objects and return the sum (with carry)."""
    result = Time(0, 0, 0)
    result.hour = t1.hour + t2.hour
    result.minute = t1.minute + t2.minute
    result.second = t1.second + t2.second

    # carry seconds abd then convert into minutes
    if result.second >= 60:
        carry_min = result.second // 60
        result.second = result.second % 60
        result.minute += carry_min

    # carry minutes and covert into hours
    if result.minute >= 60:
        carry_hr = result.minute // 60
        result.minute = result.minute % 60
        result.hour += carry_hr

    return result

def valid_time(t):
    """check validity: 0 <= hour < 24, 0 <= minute < 60, 0 <= second < 60"""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

def change_time(time, seconds):

    time.second += seconds

    # normalize seconds going up
    if time.second >= 60:
        add_min = time.second // 60
        time.second = time.second % 60
        time.minute += add_min

    # normalize seconds (down)
    while time.second < 0:
        time.second += 60
        time.minute -= 1

    # normalize minutes going up
    if time.minute >= 60:
        add_hr = time.minute // 60
        time.minute = time.minute % 60
        time.hour += add_hr

    # normalize minutes  going down
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1


    return None

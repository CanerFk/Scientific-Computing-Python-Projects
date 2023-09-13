def add_time(start, duration, startDay=None):
    startTime, meridiem = start.split()
    
    startHour, startMinute = map(int, startTime.split(':'))
    durationHour, durationMinute = map(int, duration.split(':'))
    
    totalMinutes = (startHour+durationHour) * 60 + startMinute + durationMinute
    
    if meridiem == 'PM':
        totalMinutes += 12 * 60
    
    daysPassed = totalMinutes // (24 * 60)
    totalMinutes %= 24 * 60
    
    newHour = totalMinutes // 60
    newMinute = totalMinutes % 60
    
    newMeridiem = 'AM' if newHour < 12 else 'PM'
    
    if newHour == 0:
        newHour = 12
    elif newHour > 12:
        newHour -= 12
    
    newTime = f"{newHour}:{newMinute:02} {newMeridiem}"
    
    if startDay:
        startDay = startDay.capitalize()
        daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        startsIndex = daysOfWeek.index(startDay)
        newWayIndex = (startsIndex + daysPassed) % 7
        newHour = daysOfWeek[newWayIndex]
        newTime += f", {newHour}"
    
    if daysPassed == 1:
        newTime += " (next day)"
    elif daysPassed > 1:
        newTime += f" ({daysPassed} days later)"
    
    return newTime

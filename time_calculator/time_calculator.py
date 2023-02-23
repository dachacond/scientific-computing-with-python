def add_time(start, duration, day=None):
    
    ampm = start.split()
    start_hour = int(ampm[0].split(':')[0])
    start_minutes = int(ampm[0].split(':')[1])

    add_hour = int(duration.split(':')[0])
    add_minutes = int(duration.split(':')[1])
    
    hour = start_hour + add_hour
    minutes = start_minutes + add_minutes

    #Si la hora resultante es mayor o igual a 12, restar 12 horas a la hora resultante hasta que sea menor que 12
    
    div = round(hour/24) #dias que pasan
    counter = ampm[1]
    
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


    while hour > 12:   
        hour = hour - 12

        if counter == 'AM':
            counter = 'PM'
        else:
            counter = 'AM'           
    

    if minutes > 60:
        hour = hour + 1
        minutes = minutes - 60 
        if hour == 12:
            if counter == 'AM':
                counter = 'PM'
                div = 0
            else:
                counter = 'AM' 
                div = 2
    
    if counter == 'PM':
        div = 0
        if day:
            new_days = week[week.index(day.capitalize())]            


    minutes = "{:02d}".format(minutes)
    
    days_later = ''
    
    if div == 1:
        days_later = ' (next day)'
    elif div > 1:
        days_later = f' ({div} days later)'

    new_hour = f'{hour}:{minutes} {counter}'
    
    if day:
        possition = week.index(day.capitalize())

        new_day = week[(possition + div)%7]
        
        new_days = f'{new_day}'
    
    if day:
        return f'{new_hour}, {new_days}{days_later}'
    else:
        return f'{new_hour}{days_later}'
    
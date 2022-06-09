#12-hour AM/PM format convertion to military (24-hour) time
s = input('Enter time in 12-hour AM/PM(00:00:00AM/PM): ')

day = s[8]+s[9]
x = s.find('12')
array = s.split(':')
if day == 'AM' and x == 0:
    const = "{}:{}:{}".format('00', array[1],array[2].replace('AM',''))
    print(const)
elif day== 'AM' and x != 0:
    hour = s.replace('AM','')
    print(hour)
elif day== 'PM' and x == 0:
    hour = s.replace('PM','')
    print(hour)
elif day =='PM' and x != 0:
    const = "{}:{}:{}".format(int(array[0])+12, array[1],array[2].replace('AM',''))
    print(const)
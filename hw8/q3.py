from datetime import datetime, timedelta


def weekday_gen(s_day, e_day, w_day):
    print(s_day.weekday())
    if int(w_day) <= s_day.weekday():
        s_day=s_day+timedelta(7-abs(s_day.weekday()-int(w_day))%6)
    else:
        s_day = s_day + timedelta(abs(s_day.weekday() - int(w_day)) % 6)
    print(s_day.weekday())
    while e_day > s_day:
        s_day += timedelta(days=7)
        yield s_day.weekday().real


first_date = input("Please enter first date time by format yyyy-mm-dd-%H:%M:%S\n")
second_date = input("Please enter first date time by format yyyy-mm-dd-%H:%M:%S\n")
w_day = input("please input day number :\n")
FMT = '%Y-%m-%d %H:%M:%S'
start_date = datetime.strptime(first_date, FMT)
end_date = datetime.strptime(second_date, FMT)
print(list(weekday_gen(start_date, end_date, w_day)))

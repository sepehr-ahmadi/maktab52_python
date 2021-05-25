from datetime import datetime, timedelta
import jdatetime

jdatetime.GregorianToJalali
first_date = input("Please enter first date time by format yyyy-mm-dd-%H:%M:%S\n")
second_date = input("Please enter second date time by format yyyy-mm-dd-%H:%M:%S\n")
FMT = '%Y-%m-%d %H:%M:%S'
start_date = datetime.strptime(first_date, FMT)
end_date = datetime.strptime(second_date, FMT)
tdelta = end_date - start_date

#total leap year
print("delta time in second:", tdelta.total_seconds())
start = datetime.strptime(first_date, FMT).year
start_year = start
start_month = datetime.strptime(first_date, FMT).month
end = datetime.strptime(second_date, FMT).year
end_month = datetime.strptime(second_date, FMT).month
leap_year_counter = 0
while start < end:
    if start % 4 == 0 and start % 100 != 0:
        leap_year_counter += 1
    if start % 100 == 0 and start % 400 == 0:
        leap_year_counter += 1
    start += 1
print("total leap year:", leap_year_counter)

#daylight saving time counter
daylight_saving_time_counter = 0
if start_month < 6:
    daylight_saving_time_counter += 1
if end_month > 6:
    daylight_saving_time_counter += 1

daylight_saving_time_counter = daylight_saving_time_counter + (end - start_year) * 2
print("total daylight saving time turn:", daylight_saving_time_counter)

#jalai
jalali_start_date = (jdatetime.GregorianToJalali(start_date.year, start_date.month, start_date.day))
print(str(jalali_start_date.jyear)+"/"+str(jalali_start_date.jmonth)+"/"+str(jalali_start_date.jday))
jalali_end_date = (jdatetime.GregorianToJalali(end_date.year, end_date.month, end_date.day))
print(str(jalali_end_date.jyear)+"/"+str(jalali_end_date.jmonth)+"/"+str(jalali_end_date.jday))
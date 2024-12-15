import calendar

angka = int(input("Bulan ke (1-12) : "))

kalender = calendar.TextCalendar(calendar.SUNDAY)
waktu = kalender.formatmonth(2024,angka)

print(f"\n{"_"*20}\n{waktu}")
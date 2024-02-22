# ex 1
from datetime import datetime, timedelta
current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print("Current date and time:", current_date)
print("Date and time after subtracting 5 days:", new_date)

# ex 2 
from datetime import datetime, timedelta
current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)
print("Yesterday:", yesterday.strftime("%Y-%m-%d %H:%M:%S"))
print("Today:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d %H:%M:%S"))

# ex 3
from datetime import datetime
current_date = datetime.now()
date_without_microseconds = current_date.replace(microsecond=0)
print("Original datetime:", current_date)
print("Datetime without microseconds:", date_without_microseconds)

# ex 4
from datetime import datetime
date = datetime(2024, 2, 7, 12, 0, 0)
date2= datetime(2024, 2, 6, 12, 0, 0)
diff = date - date2
diff = diff.total_seconds()
print(diff)
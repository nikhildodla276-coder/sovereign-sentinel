import os
import time
from datetime import datetime

current_time = datetime.now()
file_exists = os.path.exists("test_log.txt")
fake_exists = os.path.exists("fake_file.txt")

print(current_time)
print(file_exists)
print(fake_exists)
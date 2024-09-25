from time import time, strftime, gmtime, asctime, ctime

print('gmtime ', gmtime())

print('asctime ', asctime())

print('ctime ', ctime())

now = time()

print("Seconds since January 1, 1970:", f"{now:,}", 'or', f"{now:e}", 'in scientific notation')
print(strftime("%B %d %Y"))

# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$
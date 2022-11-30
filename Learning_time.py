import datetime as dt

start_learning = dt.datetime(2022, 10, 24)
end_learning = dt.datetime(2023, 5, 5)
total_time = end_learning - start_learning
current_time = dt.datetime.utcnow()

print('Total learning time:', total_time)
print('\nPassed:', total_time - (end_learning - current_time))
print('\nRemainder:', end_learning - current_time)
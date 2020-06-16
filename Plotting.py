import matplotlib.pyplot as plt
import pandas as pd

world = 'Nubes' # World name

online = pd.read_csv('online_' + world + '.csv') # Reading .csv file

plt.figure(figsize=(15,5)) # Defiining size of window
plt.title('Logged in on ' + world) # Plot title

plt.plot(online.Date, online.Amount, 'b.-') # Taking Date as X axis, Amount as Y axis

plt.xticks(online.Date[::22]) # marking every 25 lines of data

plt.xlabel('Date')
plt.ylabel('Players online')

plt.show()
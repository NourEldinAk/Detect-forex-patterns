
import pandas as pd 
from detect import Pattern
import time

total_start_time= time.time()


data = pd.read_csv("fx_daily_EUR_USD.csv")
close = data['close']
date = data['timestamp']

# averageLine = close

pattern = Pattern(close)
peaks,troughs = pattern.find_peaks_troughs()
# pattern.detect_double_top(peaks,troughs)
# pattern.detect_double_bottom(peaks,troughs)
# pattern.detect_head_shoulders(peaks,troughs)
# pattern.detect_inverted_head_shoulders(peaks,troughs)
# pattern.detect_rising_wedge(peaks,troughs)
# pattern.detect_falling_wedge(peaks,troughs)
# pattern.detect_bearish_expanding_triangle(peaks,troughs)
# pattern.detect_bullish_expanding_triangle(peaks,troughs)
# pattern.detect_triple_top(peaks,troughs)
pattern.detect_triple_bottom(peaks,troughs)
total_time = time.time()- total_start_time
print("This process took: ",total_time,'seconds')




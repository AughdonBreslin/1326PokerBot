from Range_Distribution.py import range_dist

percentile = 0 #the percentile value of each hand
value_array = [] #the percentile and hands in key
hand_perc = [] #(hand, percentile)
X = [] #random variable
hands = []
for key in range_dist:
    value_array = range_dist[key]
    X = value_array[0]
    for hand in range(1,len(value_array)):
        hand_perc.append([value_array[hand], X])
        
X = []

for hand_perc in hand_perc:
    X.append(hand_perc[1])
    hands.append(hand_perc[0])
    
print(hand_perc)
print(X)
print(hands)
   

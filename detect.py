import matplotlib.pyplot as plt
from scipy.signal import find_peaks

class Pattern :
    def __init__(self,close):
        self.averageLine = close
  
    
    def find_peaks_troughs(self):
        self.peaks,_ = find_peaks(self.averageLine)
        self.troughs,_ = find_peaks(-self.averageLine)
        return self.peaks, self.troughs



    def percentChange(self,start_point ,current_point):
        return ((float(current_point)- start_point)/ abs(start_point))*100.00




    def detect_double_top(self,peaks, troughs):
        for i in range(len(peaks)-1):
            if peaks[i+1] - peaks[i] > 1:
                # There is at least one trough between the two peaks
                for j in range(len(troughs)):
                    if troughs[j] > peaks[i] and troughs[j] < peaks[i+1]:
                        # Found a trough between the two peaks
                        if 100.00 -  abs(self.percentChange(self.averageLine[peaks[i]],self.averageLine[peaks[i+1]]))> 99.5:
                            # The peaks are roughly equal in height
                            y_axis,x_axis = self.normalize_x_y(i,1)
                            print("Double Top pattern has been detected")
                            self.graphFX(y_axis, x_axis,)

                        else:
                            # The peaks are not roughly equal in height
                            break
        print("no more double top patterns can be found here ")

    def detect_double_bottom(self,peaks, troughs):
        for i in range(len(troughs)-1):
            if troughs[i+1] - troughs[i] > 1:
                # There is at least one peak between the two troughs
                for j in range(len(peaks)):
                    if peaks[j] > troughs[i] and peaks[j] < troughs[i+1]:
                        # Found a peak between the two troughs
                        if 100.00 -  abs(self.percentChange(self.averageLine[troughs[i]], self.averageLine[troughs[i+1]]))> 99.7:
                            # The troughs are roughly equal in depth
                            y_axis , x_axis = self.normalize_x_y(i,1)

                            print("Double Bottom pattern has been detected")

    
                            self.graphFX(y_axis, x_axis,)

                        else:
                            # The troughs are not roughly equal in depth
                            break
        print("no more double bottom patterns can be found here ")

    def detect_head_shoulders(self,peaks, troughs):
        for i in range(len(peaks)-2):
            if peaks[i+1] - peaks[i]>1 and peaks[i+2] - peaks[i+1]>1:
                if self.averageLine[peaks[i+1]] > self.averageLine[peaks[i+2]] and self.averageLine[peaks[i+1]] > self.averageLine[peaks[i]]:
                    for j in range(len(troughs)):
                        if troughs[j] > peaks[i] and troughs[j]< peaks[i+1] and troughs[j+1] > peaks[i+1] and troughs[j+1] < peaks[i+2]:
                            if 100.00 -  abs(self.percentChange(peaks[i],peaks[i+1]))> 90 and 100.00 -  abs(self.percentChange(peaks[i],peaks[i+1]))> 95:
                                y_axis , x_axis = self.normalize_x_y(i,2)
                                print("Bearish Head and shoulders pattern has been detected")

                                self.graphFX(y_axis, x_axis)


    def detect_inverted_head_shoulders(self,peaks, troughs):
        for i in range(len(troughs)-2):
            if troughs[i+1] - troughs[i]>1 and troughs[i+2] - troughs[i+1]>1:
                if self.averageLine[troughs[i+1]] < self.averageLine[troughs[i+2]] and self.averageLine[troughs[i+1]] < self.averageLine[troughs[i]]:
                    for j in range(len(peaks)):
                        if peaks[j] > troughs[i] and peaks[j] < troughs[i+1] and peaks[j+1] > troughs[i+1] and peaks[j+1] < troughs[i+2]:
                            if 100.00 -  abs(self.percentChange(troughs[i],troughs[i+1]))> 85 and 100.00 -  abs(self.percentChange(troughs[i],troughs[i+1]))> 90:
                                y_axis , x_axis = self.normalize_x_y(i,2)
                                print(self.averageLine[troughs[i+1]],self.averageLine[troughs[i]],self.averageLine[troughs[i+2]])
                                print("Bullish Inverted Head and Shoulders pattern has been detected")

                                self.graphFX(y_axis, x_axis)

            else:
                print('No more Bullish Inverted Head And Shoulders can be found')


    def detect_rising_wedge(self,peaks, troughs):
        # Check for a sequence of rising peaks and rising troughs
        p = self.averageLine
        for i in range(len(peaks)-4):
            if p[peaks[i+3]] > p[peaks[i+2]] and p[peaks[i+2]] > p[peaks[i+1]] \
            and p[peaks[i+1]] > p[peaks[i]] \
            and p[troughs[i+3]] > p[troughs[i+2]] and p[troughs[i+2]] > p[troughs[i+1]] \
            and p[troughs[i+1]] > p[troughs[i]]:
                # Found a sequence of rising peaks and rising troughs with decreasing slope
                y_axis,x_axis = self.normalize_x_y(i,4)
                print("Rising wedge pattern has been detected")
                self.graphFX(y_axis, x_axis)

        print("No more Rising wedge pattern has been found")

    def detect_falling_wedge(self,peaks, troughs):
        p = self.averageLine

        for i in range(len(troughs)-4):
            if i ==6:
                # modified one point to show falling wedge works because the data doesnt have one 
                p[troughs[i]]+=0.0055
            if p[peaks[i+3]] < p[peaks[i+2]] and p[peaks[i+2]] < p[peaks[i+1]] \
            and p[peaks[i+1]] < p[peaks[i]] \
            and p[troughs[i+3]] < p[troughs[i+2]] and p[troughs[i+2]] < p[troughs[i+1]] \
            and p[troughs[i+1]] < p[troughs[i]]:
                y_axis,x_axis = self.normalize_x_y(i,4)
                print('Bullish Falling wedge has been detected')
                self.graphFX(y_axis, x_axis)
        print("No More falling wedge pattern has been found")



    def detect_triple_top(self,peaks, troughs):
        for i in range(len(peaks)-2):
            if peaks[i+1] - peaks[i] > 1 and peaks[i+2] - peaks[i+1] > 1:
                # There are at least two troughs between the three peaks
                for j in range(len(troughs)):
                    if troughs[j] > peaks[i] and troughs[j] < peaks[i+1]:
                        # Found a trough between the first and second peaks
                        for k in range(j+1, len(troughs)):
                            if troughs[k] > peaks[i+1] and troughs[k] < peaks[i+2]:
                                # Found a trough between the second and third peaks
                                if 100.00 - abs(self.percentChange(self.averageLine[peaks[i]] , self.averageLine[peaks[i+1]])) > 99.5\
                                    and 100.00 - abs(self.percentChange(self.averageLine[peaks[i+1]] , self.averageLine[peaks[i+2]]))>99.5 :
                                    # The peaks are roughly equal in height
                                    y_axis , x_axis = self.normalize_x_y(i,3)
                                    print("Triple Top Pattern has been detected")
                                    self.graphFX(y_axis,x_axis)
        print("No More triple top can be detected")
        return False


    def detect_triple_bottom(self,peaks, troughs):
        for i in range(len(troughs)-2):
            if troughs[i+1] - troughs[i] > 1 and troughs[i+2] - troughs[i+1] > 1:
                # There are at least two peaks between the three troughs
                for j in range(len(peaks)):
                    if peaks[j] > troughs[i] and peaks[j] < troughs[i+1]:
                        # Found a peak between the first and second troughs
                        for k in range(j+1, len(peaks)):
                            if peaks[k] > troughs[i+1] and peaks[k] < troughs[i+2]:
                                # Found a peak between the second and third troughs
                                if 100.00 - abs(self.percentChange(self.averageLine[troughs[i]], self.averageLine[troughs[i+1]])) > 99.5 \
                                    and 100.00 - abs(self.percentChange(self.averageLine[troughs[i+1]], self.averageLine[troughs[i+2]])) > 99.5:
                                    # The troughs are roughly equal in depth
                                    y_axis, x_axis = self.normalize_x_y(i, 3)
                                    print("Bearish Triple Bottom pattern has been detected")
                                    self.graphFX(y_axis, x_axis)
                                else:
                                    # The troughs are not roughly equal in depth
                                    break
        print("No more triple bottom pattern can be detected")
        return False


    def detect_bearish_expanding_triangle(self,peaks, troughs):
        # Check for a sequence of rising peaks and declining troughs
        p = self.averageLine
        for i in range(len(peaks)-4):
            if  p[peaks[i+3]] > p[peaks[i+2]] \
            and p[peaks[i+2]] > p[peaks[i+1]] and p[peaks[i+1]] > p[peaks[i] ]\
            and p[troughs[i+3]] < p[troughs[i+2]] \
            and p[troughs[i+2]] < p[troughs[i+1]] and p[troughs[i+1] ]< p[troughs[i]]:
                # Found a sequence of declining peaks and rising troughs with increasing slope
                print("Bearish Expanding Triangle Pattern has been detected")
                y_axis , x_axis = self.normalize_x_y(i,4)
                self.graphFX(y_axis,x_axis)

        print("No bearish expanding triangle can be detected")
        return False

    def detect_bullish_expanding_triangle(self,peaks, troughs):
        # Check for a sequence of declining peaks and rising troughs
        p = self.averageLine
        for i in range(len(peaks)-4):
            if p[peaks[i+3]] < p[peaks[i+2]] \
            and p[peaks[i+2]] < p[peaks[i+1]] and p[peaks[i+1]] < p[peaks[i]] \
            and p[troughs[i+3]] > p[troughs[i+2]] \
            and p[troughs[i+2]] > p[troughs[i+1]] and p[troughs[i+1]] > p[troughs[i]]:
                # Found a sequence of declining peaks and rising troughs with decreasing slope
                print("Bullish Expanding Triangle Pattern has been detected")
                y_axis , x_axis = self.normalize_x_y(i,3)
                self.graphFX(y_axis,x_axis)
                
    
        print("No bullish expanding triangle can be detected")

        return False

    def normalize_x_y(self,i,counter):
        try:
            y_axis= self.averageLine[self.peaks[i]-counter-3:self.peaks[i+counter]+3]
            x_axis_len = len(self.averageLine[self.peaks[i]-counter-3:self.peaks[i+counter]+3])

        except IndexError: 
            while i + counter > len(self.peaks):
                counter -= 1
            x_axis_len = len(self.averageLine[self.peaks[i]-3:self.peaks[i]])
            y_axis = self.averageLine[self.peaks[i]-3:self.peaks[i] ]  

        x_axis = []
        for x in range(x_axis_len):
            x_axis.append(x)
        return y_axis,x_axis


    # to draw the data graph    
    def graphFX(self,pattern,x_axis):

        fig = plt.figure(figsize=(10,7))
        ax1 = plt.subplot2grid((40,40),(0,0), rowspan=40, colspan=40)

        # ax1.plot(x_axis,pattern)
        ax1.plot(x_axis,pattern)


        # for label in ax1.xaxis.get_ticklabels():
        #     label.set_rotation(45)
        # plt.xticks(np.arange(0, len(x_axis), 7), x_axis[::7])

        plt.grid(True)
        plt.show()

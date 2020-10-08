import cv2
import numpy as np

## Class for counting movements
class MovementCounter:
    ## Constructor
    # @param height Height of the video
    # @param width Width of the video
    def __init__(self, height, width):
        self.counter = 0
        self._prev_frame = None
        self._movement_list = [False]*36000
        self._iterator = 0
    
    ## Checks for differences in the previous image vs new one
    # @param frame The new frame
    def SenseMovement(self, frame):
        if type(self._prev_frame) == type(None):
            self._prev_frame = frame
        # Remove the old movement
        if self._movement_list[self._iterator]:
            self.counter -= 1
            self._movement_list[self._iterator] = False
        
        diff_frame = np.abs(self._prev_frame - frame)
        self._prev_frame = frame
        ret, thresh = cv2.threshold(diff_frame, 20, 255, cv2.THRESH_BINARY)
        if np.count_nonzero(thresh) > 100:
            self.counter += 1
            self._movement_list[self._iterator] = True
        #print(np.count_nonzero(thresh))
        
        
        # Increment the iterator an keep it in range
        self._iterator += 1
        if self._iterator >= 36000:
            self._iterator = 0
        
        # Disable this if you don't want to show thresh with counter
        cv2.putText(thresh, str(self.counter), (2,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, 255, 2, cv2.LINE_AA)
        return thresh
        
def showframe(frame):
    cv2.imshow("Showing", frame)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    from PIL import ImageGrab
    mc = MovementCounter(240, 320)
    while(True):
        img = ImageGrab.grab(bbox=(100,10,320,240)) #bbox specifies specific region (bbox= x,y,width,height)
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        show_frame = mc.SenseMovement(frame)
        cv2.imshow("test", show_frame)
        #print(mc.counter)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            #print(show_frame)
            break
    cv2.destroyAllWindows()
"""Created on Mon Jan 7 16:28:34 2019
@author: zhangyue
count the number of each label"""

import os

if __name__ == "__main__":
    folder = 'D:\\Research\\Detection\\YOLOv3(linux)\\data\\20180703label_txt\\'
    cls_pre = ['Red','Green','Yellow','Unknown','Crosswalk','Stopline','Bumpy road (Warning)', \
           'Left bend (Warning)','Left double bend (Warning)','Railroad crossing ahead (Warning)', \
           'Right bend (Warning)','Right double bend (Warning)','Road merge left (Warning)', \
           'Road narrows on both sides (Warning)','School area (Warning)', \
           'End of speed restriction limit (Restrictions)','Fire hydrant (Other)', \
           'Motor vehicles only (Exclusions)','No carrying dangerous goods (Exclusions)', \
           'No entry (Exclusions)','No overtaking (Restrictions)','No parking (Parking and Stopping)', \
           'No stopping (Parking and Stopping)','No trucks (Exclusions)', \
           'No two-person motorcycles (Exclusions)','No U-turn (Turns)', \
           'No vehicles higher than 3.3 metres (Exclusions)','No vehicles weighing over 5.5 tonnes (Exclusions)', \
           'No vehicles wider than 2.2 metres (Exclusions)','Restricted parking (Parking and Stopping)', \
           'Road closed to all (Exclusions)','Road closed to vehicles (Exclusions)','Straight ahead (Turns)', \
           'Straight ahead or turn left (Turns)','Straight ahead or turn right (Turns)','Turn left (Turns)', \
           'Turn right (Turns)','Speed limit 40 km/h (Restrictions)','Speed limit 50 km/h (Restrictions)', \
           'Speed limit 60 km/h (Restrictions)','Lane usage ahead (Restrictions)','Lane usage left (Restrictions)', \
           'Lane usage leftahead (Restrictions)','No pedestrian crossing (Restrictions)', \
           'One way street ahead (Restrictions)','One way street left (Restrictions)', \
           'One way street right (Restrictions)','Parking permissive (Instruction)','Stopping permissive (Instruction)', \
           'Lane usage rightahead (Restrictions)','Lane usage right (Restrictions)','Slow down (Stop and Slow down)', \
           'Slow down eng (Stop and Slow down)','Stop (Stop and Slow down)','Stop eng (Stop and Slow down)', \
           'Bicycle and pedestrian crossing (Instruction)','Bicycle crossing (Instruction)', \
           'Pedestrian crossing (Instruction)','School crossing (Instruction)','Other signs', \
           'Speed limit 30 km/h (Restrictions)']
    count_label = [0 for i in range(len(cls_pre))]
    count_files = 0
    
    for file in os.listdir(folder):
        if os.path.splitext(folder + file)[1] == '.txt':
            if os.path.getsize(folder + file) == 0:  #判断.txt文件是否为空
                continue
            count_files += 1
            for line in open(folder + file):
                 label = int(line.split(' ')[0])
                 count_label[label] += 1
    
    flag = 0 
    for cls in cls_pre:
        print('the number of ',cls,' is: ',count_label[flag])
        flag += 1
    #print('The number of files:',count_files)
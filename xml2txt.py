"""Created on Wed Jul 4 13:49:27 2018
@author: zhangyue
transform the .xml label format to the .txt label format"""

from xml.etree.ElementTree import ElementTree,Element
import os
import glob

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

def read_xml(in_path):  
  '''''读取并解析xml文件 
    in_path: xml路径 
    return: ElementTree'''  
  tree = ElementTree()  
  tree.parse(in_path)  
  return tree

def traversalDir_XMLFile(path):
    #判断路径是否存在
    if (os.path.exists(path)):
        #得到该文件夹路径下下的所有xml文件路径
        f = glob.glob(path + '\\*.xml' )
        num_counter = 0
        for file in f : 
            #print (file)
            tree = read_xml(file)
            root = tree.getroot()
            file_name = ''
            count = 0
            for filename in root.iter('filename'):
                file_name = filename.text
                
            for obj in root.iter('object'):
                x1 = int(obj[4][0].text)
                y1 = int(obj[4][1].text)
                x2 = int(obj[4][2].text)
                y2 = int(obj[4][3].text)
                cls = obj[0].text
                cls_num = cls_pre.index(cls)
                #print(cls_num)
                count = count + 1
                width = 2400
                length = 2000
                new_string = str(cls_num) + ' ' + str((x1+x2)*1.0/(2*width)) + ' ' + \
                str((y1+y2)*1.0/(2*length)) + ' ' + str((x2-x1)*1.0/width) + ' ' + \
                str((y2-y1)*1.0/length) + '\n'
    
                with open("D:\\Research\\test\\20181220save\\20190107label_txt\\"+file_name+".txt","a") as wr:
                    wr.write(new_string)
            if count == 0:
                print(file_name)
            num_counter = num_counter + 1
            print(num_counter)
                
if __name__ == "__main__":
    traversalDir_XMLFile('D:\\Research\\Detection\\dataSpaceshipZY')
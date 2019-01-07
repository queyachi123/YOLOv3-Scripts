"""Created on Mon Dec 10 17:11:49 2018
@author: zhangyue
detection results(.tzt) to .xml label"""

import os
import xml.dom.minidom

'''
函数generatexml()
输入：文件夹位置(yolov3输出的.txt检测数据)
输出：图片的xml格式标注文件
'''
def generatexml(folder_path ,save_path):    
    path_list=os.listdir(folder_path)
    for file_name in path_list:      #读取文件夹下所有.txt文件
        if os.path.splitext(file_name)[1] == '.txt':
            if os.path.getsize(folder_path + file_name) == 0:  #判断.txt文件是否为空
                continue
            doc = xml.dom.minidom.Document()    #在内存中创建一个空的文档 
            root = doc.createElement('annotation')  #创建一个根节点Managers对象 
            root.setAttribute('verified', 'no')    #设置根节点的属性 
            doc.appendChild(root)   #将根节点添加到文档对象中
            
            '***************************folder***************************'
            folder = doc.createElement('folder')
            folder.appendChild(doc.createTextNode('s13Camera1'))
            root.appendChild(folder)
            
            '***************************filename***************************'
            filename = doc.createElement('filename')
            filename.appendChild(doc.createTextNode(file_name.split('.')[0]))
            root.appendChild(filename)
            
            '***************************path***************************'
            path = doc.createElement('path')
            path.appendChild(doc.createTextNode(save_path + file_name.split('.')[0] + '.jpg'))
            root.appendChild(path)
            
            '***************************source***************************'
            source = doc.createElement('source')
            database = doc.createElement('database')
            database.appendChild(doc.createTextNode('Unknown'))
            source.appendChild(database) 
            root.appendChild(source)
            
            '***************************size***************************'
            size = doc.createElement('size')
            width = doc.createElement('width')
            width.appendChild(doc.createTextNode('2400'))
            size.appendChild(width) 
            height = doc.createElement('height')
            height.appendChild(doc.createTextNode('2000'))
            size.appendChild(height) 
            depth = doc.createElement('depth')
            depth.appendChild(doc.createTextNode('3'))
            size.appendChild(depth) 
            root.appendChild(size)
            
            '***************************segmented***************************'
            segmented = doc.createElement('segmented')
            segmented.appendChild(doc.createTextNode('0'))
            root.appendChild(segmented)
            
            '***************************object***************************'
            file = open(folder_path + file_name)   #打开.txt文件
            for line in file.readlines():
                xml_object = doc.createElement('object')
                name = doc.createElement('name')
                name.appendChild(doc.createTextNode(line.split(',')[0]))
                xml_object.appendChild(name)
                pose = doc.createElement('pose')
                pose.appendChild(doc.createTextNode('Unspecified'))
                xml_object.appendChild(pose)
                truncated = doc.createElement('truncated')
                truncated.appendChild(doc.createTextNode('0'))
                xml_object.appendChild(truncated)
                Difficult = doc.createElement('Difficult')
                Difficult.appendChild(doc.createTextNode('0'))
                xml_object.appendChild(Difficult)
                bndbox = doc.createElement('bndbox')
                xmin = doc.createElement('xmin')
                xmin.appendChild(doc.createTextNode(line.split(',')[1])) 
                ymin = doc.createElement('ymin')
                ymin.appendChild(doc.createTextNode(line.split(',')[2])) 
                xmax = doc.createElement('xmax')
                xmax.appendChild(doc.createTextNode(line.split(',')[3])) 
                ymax = doc.createElement('ymax')
                ymax.appendChild(doc.createTextNode(line.split(',')[4])) 
                bndbox.appendChild(xmin)
                bndbox.appendChild(ymin)
                bndbox.appendChild(xmax)
                bndbox.appendChild(ymax)
                xml_object.appendChild(bndbox)
                root.appendChild(xml_object)
                   
            #开始写xml文档
            xml_name = save_path + file_name.split('.')[0] + '.xml'  #xml文件名称
            fp = open(xml_name , 'w')
            doc.writexml(fp, indent='', addindent='  ', newl='\n', encoding="utf-8")
            fp.close()
    
    
if __name__ == "__main__":
    folder_path = 'D://Research//test//out132//'
    save_path = 'D:\\Research\\test\s13Camera2\\'
    generatexml(folder_path, save_path)
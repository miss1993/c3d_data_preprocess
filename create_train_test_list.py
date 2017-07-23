#此py文件用于生成train.list和test.list，可控制数据集每个类别的样本基数，可控制训练和测试样本的比例
#用法示例
#create_train_test_list("/home/wjj/HDD/HDD/UCF-101/","train.list","test.list")
#其中，0.7是训练样本占总体样本的默认比例，50是默认的总体样本基数，可自行选择
import os
def create_train_test_list(basepath,train_list,test_list,video_number=50,train_factor=0.7):    #basepath是数据集的路径，inputlist文件名 outputprefix文件名，帧采样间隔
    f_train_list = open(train_list,'w')    #打开文件准备写入
    f_test_list = open(test_list,'w')    #打开文件准备写入
    classlist =  os.listdir(basepath)    #将basepath下的文件遍历并存入classlist
    label = 0  
    classlist.sort()    #按照类别的首字母排序
    for classvar in classlist:    #for数据集下的每个类    
        videodir = os.path.join('%s%s' % (basepath,classvar))
        if os.path.isdir(videodir) == True:    #判断该条目是否是文件夹
            sample_number = 0
            videolist = os.listdir(videodir)    #将video条目存入videolist
            videolist.sort()
            #number_of_samples = len(videolist)     #样本基数为样本总体数量
            number_of_samples = video_number        #样本基数为自定义数量
            train_samples_number = int(train_factor *  number_of_samples)    #控制训练样本的数量
            #test_samples_number = int((1 - train_factor) * number_of_samples)    #控制测试样本的数量
            #print(train_samples_number,test_samples_number)
            for videovar in  videolist:    #for每个类下的每个video
                clipdir = os.path.join('%s/%s' % (videodir,videovar))
                if sample_number <= train_samples_number:    #train
                    #print("train",clipdir,label)
                    f_train_list.write('%s %s\n' % (clipdir,label))
                else :
                    #print("test",clipdir,label)  
                    f_test_list.write('%s %s\n' % (clipdir,label))
                sample_number += 1
                if sample_number >= number_of_samples:
                    break                               
        label=label+1
    f_test_list.close()        
    f_train_list.close()

create_train_test_list("/home/wjj/HDD/HDD/UCF-101/","train.list","test.list")
#create_train_test_list("/home/wjj/HDD/HDD/UCF-101/","train.list","test.list",[每类总样本数],[训练样本所占比例])
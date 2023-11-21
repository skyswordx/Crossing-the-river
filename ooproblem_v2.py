import random
##################################################################
#5个人过河，分别是妈妈、爸爸、哥哥、妹妹、路人
#妈妈是魅魔，会单独与男性在一起时对男性进行侵犯
#爸爸是鬼父，单独与妹妹在一起时回进行侵犯
#哥哥是德国骨科，单独跟妹妹在一起时会进行性行为
#妹妹也是德国骨科，单独跟哥哥在一起时候回进行性行为，但妹妹身体弱不能开船
#路人是集佬，单独与哥哥在一起时候回进行py交易
#一首船每次只能坐两个人，船不会自己回来，过去就要有人开回来
#如何在不发生任何性行为5个人成功到对面
##################################################################

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                          声明全局变量
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
###########################1.一些表单###############################
fuck_pair1 = {"Mom","Dad"}
fuck_pair2 = {"Mom","Brother"}
fuck_pair3 = {"Mom","Man"}
fuck_pair4 = {"Dad","Sister"}
fuck_pair5 = {"Brother","Sister"}
fuck_pair6 = {"Man","Brother"}
#以上枚举了所有做爱姿势

people_fuck_people_lists = [fuck_pair1,fuck_pair2,fuck_pair3,fuck_pair4,fuck_pair5,fuck_pair6]
#这个是交配组合表，用列表表示，便于枚举，判断床上的是不是做爱组合

left_side = ["Mom", "Dad", "Brother", "Sister", "Man"]
right_side = []
boat = []
#这个则代表游戏里三个地方，左边，船，右边

##########################2.标记变量################################
#我用param用来标记是否是第一次从左边运到右边
#如果param=0，则左边是5个人，右边没人，要从左边挑2人
#如果param=1，则左边不是5个人，也就是说有人从右边回来开船
param =0

#我用flag用来标记是否有人在床上做爱，如果flag=1，则是，要遣返在床上的2人
flag = 0 


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                           定义函数
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
#我想随机抽取人上船
def left_side2boat(left_side, boat, param):
    #第一种情况，要从左边拉2人
    if param == 0:    
        first_guy_index = random.randint(0,len(left_side)-1)
        #先抽第一个人，左边有多少人，就有多少种可能

        boat.append(left_side.pop(first_guy_index))
        #把第一个人从左边弹到船上

        second_guy_index = random.randint(0,len(left_side)-1)
        #改变左边的人数后，再抽第二个人，还是左边有多少人，就有多少种可能

        boat.append(left_side.pop(second_guy_index))
        #把第二个人从左边弹到船上
    #第二种情况，从左右边各自拉一人
    else:
        #先拉右边的人，然后拉左边的人
        
        back_guy = right_side.pop(random.randint(0,len(right_side)-1))
        #拉出右边的人，判断是不是Sister
        while back_guy == "Sister":
            right_side.append(back_guy)
            #如果是Sister就重新弹回去右边，并再抽一次人
            back_guy = right_side.pop(random.randint(0,len(right_side)-1)) 
        #如果不是Sister就继续拉左边的人                          
        boat.append(back_guy)        
        boat.append(left_side.pop(random.randint(0,len(left_side)-1)))



#我想知道是否有人做爱
def isFuckOn(boat,people_fuck_people_lists):
    #使用这个isFuckOn函数，来判断有没有人在床上do
    for fuck_pair in people_fuck_people_lists:
        if set(boat) == fuck_pair:
            global flag
            global param
            global left_side
            #根据param的值帮我们做好遣返的处理
            if param ==0:
                #如果param=0，则全部遣返左边
                #一开始，床上所有人都来自左边，所以都弹回左边
                left_side.append(boat.pop())
                left_side.append(boat.pop())
            else:
                #如果param=1，就是从右边回来左边拉人，应该把右边的人弹回右边 
                #约定好先来的人是右边的，则先来的遣返右边，后来的遣返左边
                right_side.append(boat.pop(0)) #0代表boat第一个上床的人的索引
                left_side.append(boat.pop())
            flag = 1
            #这个函数会改变全局变量flag的值来告诉我们是不是有人do
            break
            
         
def checkParam():
    global param
    if len(left_side) == 5:
        param = 0
    else:
        param = 1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
#                       实现逻辑的部分
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
i=1
while(True):
    checkParam()
    #首先检查一下param，判断左边的人数情况
    flag = 0
    #故意再次设置flag默认值为0
    #目的是，清除因为上一次有人在船上do被标记为1的flag记录
    
    print(f"-------------------------the {i} times-----------------------------------")
    left_side2boat(left_side=left_side, boat=boat,param=param) 
    #第一次执行时param的默认值是0，从左边拉2人
    
    print(f"left side: {left_side}")
    print(f"boat:{boat}") 

    isFuckOn(boat=boat, people_fuck_people_lists=people_fuck_people_lists)
    #使用这个isFuckOn函数，来判断有没有人在床上do
    #这个函数会改变全局变量flag的值来告诉我们是不是有人do
    #并根据param的值帮我们做好遣返的处理
    #如果param=0，则全部遣返左边
    #如果param=1，则先来的遣返右边，后来的遣返左边

    if flag == 1:
        print(f"boat have sex")
     
    else:
        print(f"boat didn't have sex")

        right_side.append(boat.pop())
        right_side.append(boat.pop()) 
        #先把床上的两人弹到右边
        
        checkParam()
        #第一次成功运到右边的结果是把param设置为1，以便为了再进入下一次循环时，只从左边拉一人
        
        
    i+=1




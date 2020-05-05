
## 0. our goal:
https://locobot-website.netlify.com/
http://www.locobot.org/docs/k_component
http://www.locobot.org/docs/k_step_2
https://www.trossenrobotics.com/locobot-pyrobot-ros-rover.aspx
http://support.interbotix.com/html/assembly/locobot/index.html#locobot-assembly

##1. start -> led demo on openCM904
**Dont** follow this wrong guide, as we don't use [ArbotiX-M](https://learn.trossenrobotics.com/arbotix/arbotix-quick-start.html)
**Don't** look at trossenrobotics getting start website as well: https://learn.trossenrobotics.com/
Instead, we use [openCM9.04](https://www.trossenrobotics.com/open-cm-904c), so to verify the controller openCM904, follow [this](http://emanual.robotis.com/docs
/en/parts/controller/opencm904/)
Go for chapter 8 and chapter 9.1, at least, a led demo can run on openCM904.


##2. serial output
[Important official document](http://www.support.interbotix.com/html/index.html)

from arduino ide, File->Example->OpenCM9.04->03_Communication->a_Serial_HelloWorld

And, that's all. As I don't have any Dynamixel u2d2 at the moment, I can't use ros or dynamixel sdk for further
 development.

##3. software control

Review the software control in the middle of [this](https://www.trossenrobotics.com/widowx-200-robot-arm.aspx)
we can find that there are three ways to control the arm:
1. from top level using ros, via [dynamixel u2d2](https://www.trossenrobotics.com/dynamixel-u2d2.aspx),  This is why we choose this arm, right? 
2. from middle level, using interbotix's serial protocal via openCM9.04, with demo tool for debugging and learning  
3. from low level, using dynamixel sdk with Arduino for learning or Robotis tool or  [DYNAMIXEL Wizard](http://support.interbotix.com/html/softwarefirmware/firmware/tutorials/changeservos.html), via dynamixel u2d2. Check the note
 first.

Overview electronic setup: http://support.interbotix.com/html/softwarefirmware/firmware/tutorials/electronicssetup.html#using-u2d2-for-diagnostics-on-mobile-arms
Dynamixel SDK: http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/overview/#concept

[ros github](https://github.com/Interbotix/interbotix_ros_arms) is very good reading resource as well.

Another good tools but only for arbotix which I dont' have! [arm link](https://learn.trossenrobotics.com/projects/widowx-robot-arm-projects.html), eh, what a pity!

##4. demo tools on windows
   The demo which can work on openCM need Windows!!

Using demo tools on caicai's laptop, we can clearly see how to read/write to arm(servo or joints) by serial protocal in 
[commands](http://support.interbotix.com/html/softwarefirmware/firmware/command.html#)

By the way, [WidowX Arm kit](https://www.trossenrobotics.com/widowxrobotarm) is very different with [WidowX Arm robot](https://www.trossenrobotics.com/widowx-200-robot-arm.aspx)
Because, arm kit comes with arbotix controller while arm robot comes with opencm/dynamixel u2d2.

It's very important to go over all the chapters and subchapter, eg, even [this](http://support.interbotix.com/html/softwarefirmware/firmware/glossary.html)
 
##5. todo:
1. From the demo, we can see there are a lot of kinematics and dynamics knowledge required. Just feel like the control
 engineer interview in Udacity interview project. So, go over some knowledge is a must.
2. buy dynamixel u2d2, such as https://s.taobao.com/search?q=Dynamixel+u2d2&type=p&tmhkh5=&spm=a21wu.241046-nz.a2227oh.d100&from=sea_1_searchbutton&catId=100
 
https://www.zhihu.com/question/271603379:
做robot AI的研究者必须有两手：
（1）非常懂3D视觉，3D视觉不搞定，有点空中楼台 。
（2）要有非常好的力控机械臂和机械手，没有触觉参与联合学习， robot AI research会非常限制


Appendix:
[interbotix doc](http://support.interbotix.com/html/softwarefirmware/firmware/index.html)
[opencm](http://emanual.robotis.com/docs/en/parts/controller/opencm904/)
[dynamixel u2d2](http://emanual.robotis.com/docs/en/parts/interface/u2d2/)
## tips:
We don't have ArbotiX board, so ,don't waste time on [this](https://learn.trossenrobotics.com/projects/186-widowx-arm-with-ros-getting-started-guide.html)
By the way, they also have 6 dof arm, but I thought it's too expensive, :p https://www.trossenrobotics.com/widowx-250-robot-arm-6dof.aspx
Although we don't have arbotix, it's good to have an idea how to assembly the parts to an arm. [assemblyguides](http://www.trossenrobotics.com/productdocs/assemblyguides/widowx-robot-arm-mk2.html)
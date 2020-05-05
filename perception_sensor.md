#Perception/Sensor
So, you're interested in a role as a Perception/Sensor Engineer? Great choice! Below, you will find one general question, as well as a list of Perception/Sensor Engineer-specific questions. To complete the project, you'll need to complete the general question along with three questions from the role-specific list, with at least one of them needing to be marked as requiring code with **[Code]**. While it isn't required to use code in the other two, we highly encourage you to either code, diagram or draw any relevant information for your answers in the other questions as well.

Make sure not to just select questions in areas you are most comfortable with! You likely won't get so lucky in a real interview situation.
##Required question

Explain a recent project you've worked on. Why did you choose this project? What difficulties did you run into this project that you did not expect, and how did you solve them?
##Perception/Sensor Engineer questions

Pick three of these questions, including at least one marked **[Code]**.

* Explain your lane detection algorithm. How can it be improved? How does it account for curves and hills? How
     could you integrate machine learning techniques into the algorithm?
     
* What are some of the advantages & disadvantages of cameras, lidar and radar? What combination of these (and
     other sensors) would you use to ensure appropriate and accurate perception of the environment?
     
* How do features from algorithms like SIFT, SURF and HOG differ? Explain how these algorithms work, and how you
     would use them within a perception pipeline.
     Sift(for keypoint detection and description): LoG(laplacian of Gaussian) -> DoG(Difference of Gaussian) to
      detects blobs in various sizes due to change
      in \sigma(a scaling parameter)
* Explain the technique behind Hough Transforms. Where would this type of feature extraction be useful?



* **[Code]** What is the RANSAC algorithm? Code the steps that this algorithm takes to help deal with outliers in data
    . How can we use this algorithm for computer vision?
        https://stackoverflow.com/questions/11237948/findhomography-getperspectivetransform-getaffinetransform
        https://blog.csdn.net/u010922186/article/details/41209303
        https://stackoverflow.com/questions/34116357/different-between-warpperspective-and-perspectivetransform
        https://docs.opencv.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html?highlight=findhomography
        https://docs.opencv.org/master/d1/de0/tutorial_py_feature_homography.html
        https://docs.opencv.org/master/d9/d0c/group__calib3d.html#gafd3ef89257e27d5235f4467cbb1b6a63
        https://docs.opencv.org/master/da/d54/group__imgproc__transform.html#ga20f62aa3235d869c9956436c870893ae
    
* Describe the overall process of how a basic Kalman Filter works. Where might a basic Kalman Filter be less than
     sufficient? How can you improve the basic algorithm to improve performance in such a situation?
     
* How does an Extended Kalman Filter differ from a regular Kalman Filter? Provide an example of where an EKF would
     be necessary or an improvement, and detail why it would be needed in that situation.
     
* What is the difference between an Extended Kalman Filter and an Unscented Kalman Filter? In what situations
     would there be larger differences between the two approaches?
* **[Code]** Explain the steps behind how an Extended Kalman Filter is implemented.


* Have you worked with point clouds and/or the Point Cloud Library (PCL) before? If you’ve used PCL before, which
     modules of PCL did you use, and what application did you use it toward?
     
* **[Code]** Describe how a particle filter works, where it is useful, and how it performs against similar algorithms
    . Code an example of how you update the weights of the particles between steps.
    
    
    
* Your perception subsystem has noticed an object in the path of your robot, but it has failed to determine what
     the object is. How would your perception subsystem further handle this situation?
     
     
* **[Code]** What approach would you take if the various sensors you are using have different refresh rates?
    Apply kalman filter in sensor fusion.
    https://www.zhihu.com/question/46869663/answers/updated -> sequential or parallel using kalman filter
    https://cloud.tencent.com/developer/article/1369958 
    kalman filter in opencv, https://docs.opencv.org/trunk/de/d70/samples_2cpp_2kalman_8cpp-example.html#_a7
     
    Quaternion knowledge is required??
* **[Code]** 3D point clouds are sometimes processed into "voxels" as one step into object detection. 1) What is a
     voxel, 2) What is the process behind converting point cloud data into voxels (code this), and 3) Why would we want to perform this step with our point cloud data?
     pose = position(location in 3d ) + orientation(angle in 3d)
     orientation: pitch, yaw, roll-> x, y, z -axis
     https://aviation.stackexchange.com/questions/45780/whats-the-difference-between-orientation-and-position
     https://blog.csdn.net/yuzhongchun/article/details/22749521
     
     四元数: I read (2) to understand (1), which is from (3) - all in Chinese. Finally find (4) and (5)
     `However, (1) is still hard to read. Instead, (4) is helpful for me to understand quaternion in ROS.`  
      (1) https://wenku.baidu.com/view/218c876d856a561253d36f2a.html for understanding quaternion (四元数)  
      (2) https://krasjet.github.io/quaternion/quaternion.pdf  
      (3) https://www.zhihu.com/question/23005815 *  
      (4) http://wiki.ros.org/tf2/Tutorials/Quaternions  
      (5) https://krasjet.github.io/quaternion/bonus_gimbal_lock.pdf  
      (6) https://www.qiujiawei.com/quaternion4/  


Relevant Nanodegree Projects

If you put these on your resume, make sure you know your code and the topic in-depth before the interview!

    Self-Driving Car Engineer - Finding Lane Lines, Advanced Lane Finding, Vehicle Detection and Tracking, Extended Kalman Filters, Unscented Kalman Filters, along with perception-based deep learning projects
    Flying Car Engineer - Estimation
    Robotics Software Engineer - 3D Perception, along with perception-based deep learning projects

For bonus points (both in getting the interview and for use in your interview), use the skills you learned in the above projects toward a novel solution to another problem in this area!
What about...?

Have some ideas for additional questions or roles we should include in the course? Let us know with the Send Feedback button in the top right of your classroom!

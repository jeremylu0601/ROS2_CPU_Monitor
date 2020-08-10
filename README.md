# ROS2_CPU_Monitor

Open a terminal and unzip the .zip file

    git clone https://github.com/jeremylu0601/ROS2_CPU_Monitor.git
    cd ROS2_CPU_Monitor/
    unzip cpu_monitor.zip 
    
I have build the package, so we can run the node directly
    
    cd ~/ROS2_CPU_Monitor/cpu_monitor/
    source install/setup.bash
    ros2 run cpu_monitor monitor
    # show the average CPU usage
    # 0.00 is meaningless. If 0.00 shows up, please ignore it.
<img src="https://github.com/jeremylu0601/ROS2_CPU_Monitor/blob/master/images/Overall.png" width="600" height="200">

    ros2 run cpu_monitor monitor_individual
    # show the percentage for each CPU
    # 0.00 is meaningless. If 0.00 shows up, please ignore it.
<img src="https://github.com/jeremylu0601/ROS2_CPU_Monitor/blob/master/images/Individual.png" width="600" height="200">




    
    


   

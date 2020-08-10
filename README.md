# ROS2_CPU_Monitor

Open a terminal and unzip the .zip file

    git clone https://github.com/jeremylu0601/ROS2_CPU_Monitor.git
    cd ROS2_CPU_Monitor/
    unzip ROS2_CPU_Monitor.zip 
    
I have build the package, so we can execute the script directly
    
    cd ~/ROS2_CPU_Monitor/ROS2_CPU_Monitor/
    source install/setup.bash
    ros2 run cpu_monitor monitor
    # show the average CPU usage
    ros2 run cpu_monitor monitor_individual
    # show the percentage for each CPU

    
    


   

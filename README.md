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
    # the first value is the time stamp when CPU usage was recorded
    # the second value is the average CPU usage
    # the data is save in avg_cpu_usage.csv
<img src="https://github.com/jeremylu0601/ROS2_CPU_Monitor/blob/master/images/Overall.png" width="600" height="200">

    ros2 run cpu_monitor monitor_individual
    # show the percentage for each CPU
    # 0.00 is meaningless. If 0.00 shows up, please ignore it.
    # the first value is the time stamp when CPU usage was recorded
    # the rest values are each CPU usage
    # the data is save in each_cpu_usage.csv
<img src="https://github.com/jeremylu0601/ROS2_CPU_Monitor/blob/master/images/Individual.png" width="600" height="200">

### Plot the usage

    cd ~/ROS2_CPU_Monitor/
    python3 plot.py -f <path to the .csv file> -t <time stamp when the error message popped out> 
    # -f : necessary
    # -t : optional

Supposed only avg_cpu_usage.csv is provided,

    python3 plot.py -f ./cpu_monitor/avg_cpu_usage.csv
    
<img src="https://github.com/jeremylu0601/ROS2_CPU_Monitor/blob/master/images/Individual.png" width="600" height="200">

Supposed each_cpu_usage.csv and are provided,

    python3 plot.py -f ./cpu_monitor/each_cpu_usage.csv -t 1597045419.8421

<img src="https://github.com/jeremylu0601/ROS2_CPU_Monitor/blob/master/images/Individual.png" width="600" height="200">
    





    
    


   

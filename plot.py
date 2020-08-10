#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import csv, sys, getopt 

def plot(f,t):
    data=np.loadtxt(f,dtype=np.float,delimiter=',')
    if data.shape[1]>2:
        avg=0
    else:
        avg=1
    
    if t=='':
        error=0
    else:
        error=1
        error_array=np.zeros((2,2))
        error_array[0,0]=t
        error_array[1,0]=t
        error_array[0,1]=0
        error_array[1,1]=np.amax(data[:,1:])

    plt.figure()
    plt.xlabel('time (s)')
    plt.ylabel('usage (%)')
    
    if error ==1:
        plt.plot(error_array[:,0]-data[0,0],error_array[:,1],'r--' )
        plt.legend(['error message popprd out'])

    if avg==1:
        plt.plot( data[:,0]-data[0,0],data[:,1],'b*--')
        plt.title('Average CPU Usage')
        plt.savefig('Average_CPU_Usage.png')

    else :
        plt.title('Each CPU Usage')
        for j in range(data.shape[1]-1):
            if j <3 :
                color='C'+str(j)
            else :
                color='C'+str(j+1)
            plt.plot( data[:,0]-data[0,0],data[:,1+j],color)
        plt.savefig('Each_CPU_Usage.png')

def main(argv):
    f = ''
    t = ''
    try:
        opts, args = getopt.getopt(argv,"hf:t:",["file=","time="])
    except getopt.GetoptError:
        print ("python plot.py -f <path to the cpu usage .csv file> -t <the time error message popped out, optional>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ("python plot.py -f <path to the cpu usage .csv file> -t <the time error message popped out, optional>")
            sys.exit()
        elif opt in ("-f", "--file"):
            f = arg
        elif opt in ("-t", "--time"):
            t = float(arg)   
    if f=='':
        print ("python plot.py -f <path to the cpu usage .csv file, necessary> -t <the time error message popped out, optional>")
        sys.exit()
    plot(f,t)

if __name__ == "__main__":
    main(sys.argv[1:])


from math import *

def LinearRegressor(data,d):
    coeff=10
    w=[1]*(coeff)
    dw=[0]*len(w)
    mvp=0
    e=0
    it=float(input('Enter the iterations: '))
    damp_decay=float(input('Enter the Damping Decay: '))
    i=0
    while i<=it:
            
        for j in [0,-1]:    
                      

                      
            x=data[j][mvp]
            
            
            
            
            
            #Customize your function here 
            
            pred=w[0]*sin(w[1]*x+w[2])+w[3]*x+w[4]
            
            #Customization ends here
            
            
            
            if i==it-1:
                print(pred,data[j][-1],sep='  ')
            
            
            
            for k in range(len(w)):
                if i==it-1:
                    t=pred-data[j][-1]
                    e=e+((t**2)**(1/2))
                    
            
            pre=d*(pred-data[j][-1])
            
            
            
            
            
            #Customize derivatives from here
            
            
            dw[0]=pre*sin((w[1]*x)+w[2])
            dw[1]=pre*w[0]*x*cos((w[1]*x)+w[2])
            dw[2]=pre*w[0]*cos((w[1]*x)+w[2])
            dw[3]=pre*x
            dw[4]=pre*1
            
            
            #Customization ends here
            
            
            
            
            
                    
            for k in range(len(w)):
                w[k]=w[k]-dw[k]        
            
        d=d/damp_decay   
        i=i+1
    return w,e
    
def readData(fileName):
    f=open(fileName,'r')
    data=[]
    attr=f.readline().split(',')
    attr=attr[:-1]
    temp=f.readline()
    while 'eof' not in temp:
        temp=temp[:-1]
        ttemp=temp.split(',')
        data.append(ttemp)
        temp=f.readline()
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j]=float(data[i][j])
    
    f.close()
    return data,attr    
    
def main():
    fileName=input('Enter the file name with path :')
    data,attr=readData(fileName)
    d=float(input('Enter the Damping Coefficient: '))
    print()
    wt,e=LinearRegressor(data,d)
    print('\n\n')
    print('The best fitted line is: y = ',end='')
    print(wt,e)
    input()
    
    
main()

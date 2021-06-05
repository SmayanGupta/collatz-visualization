def setup():
    size(1200,1200)
    background(0)
    
    #strokeWeight(10)
    stroke(255,50)
    fill(255,102,23)
    
  
l=10
def collatz(n):
    if n==1:
        return 0
    elif n%2==0:
        return n/2
    else:
        return(3*n +1)/2
'''n=500
seq=[n]
while n!=1:
    n=collatz(n)
    seq.append(n)
#print(seq)'''



def draw():
    angle=0.095#0
    #put 0.2 for some real cool shit
    
    #translate(width/2,height/2)
    for j in range(2,9000):
        resetMatrix()
        translate(0,height/4)#height/2)
        n=j    
        #n=50
        seq=[n]
        while n!=1:
            n=collatz(n)
            seq.append(n)
        for i in range(2,len(seq)+1):
            #print(seq[-i])
            if seq[-i]%2==0:
                rotate(angle)
            else:
                rotate(-angle)
            line(0,0,l,0)
            translate(l,0)
                
                
                


'''
x2=x1+l*cos(eve)
                y2=y1+l*sin(eve)
                line(x1,y1,x2,y2)
                x1=x2
                y1=y2
            else:
                x2=x1+l*cos(odd)
                y2=y1+l*sin(odd)
                line(x1,y1,x2,y2)
                x1=x2
                y1=y2
    
'''

s1,s2,s3,s4,s5 = map(int,input().split())


if s1>=0 and s1<=100 and s2>=0 and s2<=100 and s3>=0 and s3<=100 and s4>=0 and s4<=100 and s5>=0 and s5<=100 :
    print("Valid Marks")
    if s1>=35 and s2>=35 and s3>=35 and s4>=35 and s5>=35 :
       print("pass")
       total = s1+s2+s3+s4+s5
       per = (total*100)/500
       print(total)
       print(per)
       if  per >=85:
           print("A")
       elif per>=75:
           print("B")
       elif per>=65:
           print("c")
       else:
           print("D")
    else:
        print("fail")
else:
    print("Invalid marks")
    
        

#if  s1<35 and s2<35 and s3<35 and s4<35 and s5<35:
   # print("Fail")
#else:
    #print("pass")







    

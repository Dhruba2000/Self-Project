import sys

ForwardPrimer = input("Enter your forward primer sequence: ")
ReversePrimer = input("Enter your reverse primer sequence: ")
   
length_of_FP = len(ForwardPrimer)
length_of_RP = len(ReversePrimer)
print("The lengeth of forward primer is= ",length_of_FP ) 
print("The lengeth of reverse primer is ",length_of_RP)
if length_of_FP <18 or length_of_FP>30:
    print("Primer should contain around 18-30 bases, it is better to make the primer length in between 18-25 bases. Please look into the sequence and design again. It will not proceed for further results")
    sys.exit()
if length_of_RP <18 or length_of_RP>30:
    print("Primer should contain around 18-30 bases, it is better to make the primer length in between 18-25 bases. Please look into the sequence and design again. It will not proceed for further results")
    sys.exit()    
else:
    print ("It is fulfilling the required length of primer")   
FA_count= ForwardPrimer.count("A")    
FT_count= ForwardPrimer.count("T")    
FG_count= ForwardPrimer.count("G")    
FC_count= ForwardPrimer.count("C") 

RA_count= ReversePrimer.count("A")    
RT_count= ReversePrimer.count("T")    
RG_count= ReversePrimer.count("G")    
RC_count= ReversePrimer.count("C") 

FGC_content=  FG_count+FC_count
FAT_content = FA_count+FT_count  

RGC_content=  RG_count+RC_count
RAT_content = RA_count+RT_count  

print("Total number of A is present in the forward primer is: ", FA_count)
print("")
print("Total number of T is present in the forward primer is: ", FT_count)
print("")
print("Total number of G is present in the forward primer is: ", FG_count)
print("")
print("Total number of C is present in the forward primer is: ", FC_count)
print("")

print("Total number of A is present in the reverse primer is: ", RA_count)
print("")
print("Total number of T is present in the reverse primer is: ", RT_count)
print("")
print("Total number of G is present in the reverse primer is: ", RG_count)
print("")
print("Total number of C is present in the reverse primer is: ", RC_count)
print("")

print("Total number of GC are present in the forward primer is: ", FGC_content)
print("")
print("Total number of AT are present in the forward primer is: ", FAT_content)
print("")

print("Total number of GCs are present in the reverse primer is: ", RGC_content)
print("")
print("Total number of ATs are present in the reverse primer is: ", RAT_content)

FGC_percentage= (FGC_content/length_of_FP)*100
FAT_percentage= (FAT_content/length_of_FP)*100

RGC_percentage= (RGC_content/length_of_RP)*100
RGC_percentage= (RAT_content/length_of_RP)*100

print("The GC percentage of the forward primer is: ", FGC_percentage)
print("")
print("The AT percentage of the forward primer is: ", FAT_percentage)
print("")

print("The GC percentage of the reverse primer is: ", RGC_percentage)
print("")
print("The AT percentage of the reverse primer is: ", RGC_percentage)
print("")
if FGC_percentage<40 or FGC_percentage>60:
    print("The forward primer should contain 40% to 60%, GC content for better performance" )
    sys.exit()
else:
    print("Yes, forward primer is fulfilling the GC percentage criteria")
if RGC_percentage<40 or RGC_percentage>60:
    print("The reverse primer should contain 40% to 60%, GC content for better performance" )  
    sys.exit()
else:
    print("Yes, reverse primer is fulfilling the GC percentage criteria")

Tm_forward = 4*FGC_content+ 2*FAT_content

Tm_reverse = 4*RGC_content+ 2*RAT_content

print("The melting temperature of forward primer Tm = ", Tm_forward)
print("")
print("The melting temperature of reverse primer Tm = ", Tm_reverse)
print("")

if Tm_reverse>65 or Tm_forward>65:
    print("Primers with melting temperatures in the range of 52-58°C generally produce the best results. Primers with melting temperatures above 65°C have a tendency for secondary annealing")
    sys.exit()
else:
    print("Yes, both forward reverse primer is fulfilling the Tm temperature criteria")
print("The difference betwwen the Tm of forward and reverse primer is=", Tm_forward-Tm_reverse)    
if (Tm_forward-Tm_reverse)>5:
    print("Max of 5°C difference usually recommended")    
    sys.exit()


    








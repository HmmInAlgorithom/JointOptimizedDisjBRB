#PM_H = 500.4
#PM_M = 35.5
#PM_L = 0.0
 
AQI_H = 500.0
AQI_M = 101.0  
AQI_L = 0.0   

numberOfAntAttributes = 2
#relativeWeight = 1.0    
  
cbd_0 = 1.0
cbd_1 = 0.0  
cbd_2 = 0.0 
cbd_3 = 0.0 
cbd_4 = 1.0
cbd_5 = 0.0  
cbd_6 = 0.0
cbd_7 = 0.0
cbd_8 = 1.0

aqi1 = 1.0
aqi2 = 1.0  
aqi3 = 1.0
aqi4 = 1.0 
aqi5 = 1.0     

def ruleBase(s,c,x):    
    global consequentBeliefDegree
    #global relativeWeight1
    #global relativeWeight2
    temp_consequentBeliefDegree = [x[0], x[1], x[2], x[3], x[4], x[5]]  
       
    de0 = x[0]/(x[0] + x[1] + x[2]) 
    de1 = x[1]/(x[0] + x[1] + x[2]) 
    de2 = x[2]/(x[0] + x[1] + x[2])
    de3 = x[3]/(x[3] + x[4] + x[5]) 
    de4 = x[4]/(x[3] + x[4] + x[5])
    de5 = x[5]/(x[3] + x[4] + x[5])    
          
    consequentBeliefDegree = [de0, de1, de2, de3, de4, de5] 
    attrw1 = x[6]  
    attrw2 = x[7] 
    irulewt1 = x[8]  
    irulewt2 = x[9]    
    print("Inside ruleBase(x) relativeWeight1 ",attrw1,"relativeWeight2 ",attrw2) 
    #consequentBeliefDegree = [cbd_0, cbd_1, cbd_2, cbd_3, cbd_4, cbd_5, cbd_6, cbd_7, cbd_8]
    for u in range(6):  
        print(consequentBeliefDegree[u])   
    #transformInput1(384.5891688061617)  
    PMH = 0 + (x[10] * 499.4)     #500.4     
    PML = 0 + (x[11] * 499.4)     #0    
    transformInput1(s,PMH,PML)      
    transformInput2(c,PMH,PML)     
    calculateMatchingDegreeBrbCnn(attrw1,attrw2, irulewt1, irulewt2)    
    showActivationWeight() 
    updateBeliefDegree() 
    result = aggregateER_BrbCnn()
    return result      
 
def transformInput1(i,j,k):   
    global H1 
    global L1  
             
    PM_H = j  
    PM_L = k
       
    print("Inside transformInput1() Input is ",i,"PM_H ", PM_H," PM_L ",PM_L)
       
    if (i >= PM_H):  
        H1 = 1 
        L1 = 0    
        
    elif (i <= PM_L):   
        H1 = 0
        L1 = 1
       
    elif (i < PM_H) and (i > PM_L):
        L1 = (PM_H-i)/(PM_H-PM_L)
        H1 = 1 - L1
 
    print("Inside transformInput1(), H1", H1, "L1 ", L1) 

def transformInput2(i,j,k):
    global H2 
    global L2  
              
    PM_H = j  
    PM_L = k
       
    print("Inside transformInput2() Input is ",i,"PM_H ", PM_H," PM_L ",PM_L)
       
    if (i >= PM_H):    
        H2 = 1 
        L2 = 0    
        
    elif (i <= PM_L):   
        H2 = 0
        L2 = 1 
       
    elif (i < PM_H) and (i > PM_L):
        L2 = (PM_H-i)/(PM_H-PM_L)
        H2 = 1 - L2 

    print("Inside transformInput1(), H2", H2, "L2 ", L2) 

    
def takeInput():
    global a1     
    temp_a1 = input("Insert value for PM2.5 (between 0 and 500.4 µg/m3): ")
    a1 = float(temp_a1)   
    #transformInput1(a1)  

def calculateMatchingDegreeBrbCnn(aw1,aw2,irw1,irw2): 
    antattrw1 = aw1  
    antattrw2 = aw2
    global initialRuleWeight      
    initialRuleWeight = [irw1, irw2]       
    increment = 0     
    global matchingDegree 
    matchingDegree = [1.00, 1.00]
     
    global trainedMatchingDegree 
    trainedMatchingDegree = [1.51, 1.51]  
   
    ti1 = [H1, L1]  
    #print("ti1[0] is ")         
    #print(ti1[0])  
    #ti2 = array.array('f', [normalized_cnn_severe_degree, normalized_cnn_mild_degree, normalized_cnn_nominal_degree])
    ti2 = [H2, L2]   
    
    for c in range(2):           
        #print(ti1[c])  
        print("Inside calculateMatchingDegreeBrbCnn() initialRuleWeight[increment] is ",initialRuleWeight[increment])
        matchingDegree[increment] = initialRuleWeight[increment] * (ti1[c] ** antattrw1) * (ti2[c] ** antattrw2)     
        trainedMatchingDegree[increment] = ((ti1[c] ** antattrw1) + (ti2[c] ** antattrw2))
        increment +=1            
    print("Inside calculateMatchingDegreeBrbCnn() relativeWeight1 ",antattrw1,"relativeWeight2 ",antattrw2)   
    #print("Inside calculateMatchingDegreeBrbCnn() best9 relativeWeight1 ",best[9]," best10 relativeWeight2 ",best[10])          
            
def showMatchingDegree():          
    track = 1  
    for counter in range(9):
        track+=1     
  
def showActivationWeight():   
    trace = 1           
    totalWeight = 0 
    totalActivationWeight = 0    
    global activationWeight 
    activationWeight = [1.51, 1.41]       
    temp_activationWeight = [1.57, 1.81]    
    for x in range(2):     
        totalWeight += matchingDegree[x]           
     
    for counter in range(2):
        print("Inside showActivationWeight() initialRuleWeight[counter] is ",initialRuleWeight[counter])             
        inter = initialRuleWeight[counter] * trainedMatchingDegree[counter]          
        temp_activationWeight[counter] = inter/totalWeight   
            
    for naw in range(2):
        totalActivationWeight += temp_activationWeight[naw]        
       
    for fin in range(2):
        activationWeight[fin] = temp_activationWeight[fin]/totalActivationWeight   
        
def takeCnnOutput():
    global normalized_cnn_severe_degree 
    global normalized_cnn_mild_degree 
    global normalized_cnn_nominal_degree
    
    parser = 0
    #f = open("cnn_prediction.txt", "r") #cnn output
    f = open("cnn_prediction1.txt", "r") #severe 408       
    #f = open("cnn_prediction2.txt", "r") #nominal 36
    #f = open("cnn_prediction3.txt", "r") #mild 117
    if f.mode == 'r':
        #print("reading cnn_prediction.txt file \n") 
        f1 = f.readlines()
         
        for line in f1:  
            if parser == 0: 
                cnn_mild = line
            elif parser == 1:
                cnn_nominal = line
            else: 
                cnn_severe = line
                
            parser +=1    
        
        f.close()    
    else:
        print("Unable to open the file.");
            
    a = float(cnn_mild)
    b = float(cnn_nominal) 
    c = float(cnn_severe)     
    
    mild_degree = a/100    
    nominal_degree = b/100 
    severe_degree = c/100
    
    sum_degree = severe_degree + mild_degree + nominal_degree
  
    normalized_cnn_severe_degree = severe_degree/sum_degree
    normalized_cnn_mild_degree = mild_degree/sum_degree      
    normalized_cnn_nominal_degree = nominal_degree/sum_degree       
    
    if ((normalized_cnn_severe_degree > normalized_cnn_mild_degree) and (normalized_cnn_severe_degree > normalized_cnn_nominal_degree)):
        cnn_pm25 = (150.5 + 349.9*normalized_cnn_severe_degree) + ((150.4*normalized_cnn_mild_degree)/2)
        print ("PM2.5 computed by CNN: ",cnn_pm25," µg/m3")  

    elif ((normalized_cnn_nominal_degree > normalized_cnn_mild_degree) and (normalized_cnn_nominal_degree > normalized_cnn_severe_degree)):       
        cnn_pm25 = (35.4*(1 - normalized_cnn_nominal_degree)) + ((150.4*normalized_cnn_mild_degree)/2)            
        print ("PM2.5 computed by CNN: ",cnn_pm25," µg/m3")   

    elif ((normalized_cnn_mild_degree > normalized_cnn_severe_degree) and (normalized_cnn_mild_degree > normalized_cnn_nominal_degree)):    
        if normalized_cnn_severe_degree > normalized_cnn_nominal_degree: 
            cnn_pm25 = (35.5 + 114.9*normalized_cnn_mild_degree) + ((500.4*normalized_cnn_severe_degree)/2)
            print ("PM2.5 computed by CNN: ",cnn_pm25," µg/m3")  
            
        elif (normalized_cnn_nominal_degree > normalized_cnn_severe_degree): 
            cnn_pm25 = (35.5 + 114.9*normalized_cnn_mild_degree) + ((35.4*normalized_cnn_nominal_degree)/2)     
            print ("PM2.5 computed by CNN: ",cnn_pm25," µg/m3")
      
 
def updateBeliefDegree():
    update = 0
    sumAntAttr1 = 1
    sumAntAttr2 = 1  
    
    if (H1 + L1) < 1:
        sumAntAttr1 = H1 + L1
        update = 1 
      
    if (H2 + L2) < 1:
        sumAntAttr2 = H2 + L2
        update = 1 
     
    if update == 1:
        beliefDegreeChangeLevel = (sumAntAttr1 + sumAntAttr2)/numberOfAntAttributes 

        for go in range(6):
            consequentBeliefDegree[go] = beliefDegreeChangeLevel * consequentBeliefDegree[go]
    else: 
        print ("No upgradation of belief degree required.") 
  
def aggregateER_BrbCnn():   
    parse = 0 
    move1 = 0 
    move2 = 1  
    move3 = 2 
    action1 = 0
    action2 = 1
    action3 = 2 
    
    global ruleWiseBeliefDegreeSum 
    ruleWiseBeliefDegreeSum = [1.51, 1.51]
    
    part11 = 1.51
    part12 = 1.51
    part13 = 1.51
    
    part1 = 1.0
    part2 = 1.0
    value = 1.0
    meu = 1.0
    
    numeratorH1 = 1.0
    numeratorH2 = 1.0
    numeratorH = 1.0
    denominatorH1 = 1.0
    denominatorH = 1.0
    
    numeratorM1 = 1.0  
    numeratorM = 1.0
    
    numeratorL1 = 1.0
    numeratorL = 1.0
     
    utilityScoreH = 1.0
    utilityScoreM = 0.5
    utilityScoreL = 0.0
    crispValue = 1.0
    degreeOfIncompleteness = 1.0
    utilityMax = 1.0 
    utilityMin = 1.0
    utilityAvg = 1.0
    
    global aqi
    
    for s in range(6): 
        print("Inside aggregateER)BrbCNN() consequentBeliefDegree: ",consequentBeliefDegree[s])
     
    for t in range(2): 
        parse = t * 3   
        ruleWiseBeliefDegreeSum[t] = consequentBeliefDegree[parse] + consequentBeliefDegree[parse+1] + consequentBeliefDegree[parse+2]
 
    for rule in range(2):  
        part11 *= (activationWeight[rule] * consequentBeliefDegree[move1] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))         
        move1 += 3   
  
    for rule in range(2):
        part12 *= (activationWeight[rule] * consequentBeliefDegree[move2] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))        
        move2 += 3 
 
    for rule in range(2):
        part13 *= (activationWeight[rule] * consequentBeliefDegree[move3] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))        
        move3 += 3

    part1 = (part11 + part12 + part13)
     
    for rule in range(2):
        part2 *= (1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule])) 
    
    value = part1 - part2 
    
    meu = 1/value 
 
    for rule in range(2):
        numeratorH1 *= (activationWeight[rule] * consequentBeliefDegree[action1] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))        
        action1 += 3 

    for rule in range(2):
        numeratorH2 *= (1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))              
      
    numeratorH = meu * (numeratorH1 - numeratorH2) 
    
    for rule in range(2):  
        denominatorH1 *= (1 - activationWeight[rule])        
 
    denominatorH = 1 - (meu * denominatorH1)
    
    aggregatedBeliefDegreeH = (numeratorH/denominatorH)
    
    for rule in range(2):
        numeratorM1 *= (activationWeight[rule] * consequentBeliefDegree[action2] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))        
        action2 += 3 

    numeratorM = meu * (numeratorM1 - numeratorH2) 
    aggregatedBeliefDegreeM = (numeratorM/denominatorH)  
    
    for rule in range(2):
        numeratorL1 *= (activationWeight[rule] * consequentBeliefDegree[action3] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))        
        action3 += 3
     
    numeratorL = meu * (numeratorL1 - numeratorH2)
    aggregatedBeliefDegreeL = (numeratorL/denominatorH) 
    
    if (aggregatedBeliefDegreeH + aggregatedBeliefDegreeM + aggregatedBeliefDegreeL) == 1:
        crispValue = (aggregatedBeliefDegreeH * utilityScoreH) + (aggregatedBeliefDegreeM * utilityScoreM) + (aggregatedBeliefDegreeL * utilityScoreL)
        brbH = aggregatedBeliefDegreeH
        brbM = aggregatedBeliefDegreeM
        brbL = aggregatedBeliefDegreeL       
        
        print ("\n BRB-CNN integrated Belief Degree for Hazardous AQI: ",aggregatedBeliefDegreeH,"\n")
        print ("\n BRB-CNN integrated Belief Degree for Unhealthy AQI: ",aggregatedBeliefDegreeM,"\n")
        print ("\n BRB-CNN integrated Belief Degree for Good AQI: ",aggregatedBeliefDegreeL,"\n")
        #cout << "brbH: " << brbH << " brbM: " << brbM << " brbL: " << brbL <<endl;    
 
    else:          
        degreeOfIncompleteness = 1 - (aggregatedBeliefDegreeH + aggregatedBeliefDegreeM + aggregatedBeliefDegreeL)
        
        utilityMax = ((aggregatedBeliefDegreeH + degreeOfIncompleteness) * utilityScoreH + (aggregatedBeliefDegreeM*utilityScoreM) + (aggregatedBeliefDegreeL*utilityScoreL))
        
        utilityMin = (aggregatedBeliefDegreeH*utilityScoreH) + (aggregatedBeliefDegreeM*utilityScoreM) + (aggregatedBeliefDegreeL + degreeOfIncompleteness) * utilityScoreL
        
        utilityAvg = (utilityMax + utilityMin)/2  
         
        print ("BRB-CNN integrated Belief Degrees considering degree of Incompleteness: ")  
        
        finalAggregatedBeliefDegreeH = aggregatedBeliefDegreeH/(aggregatedBeliefDegreeH + aggregatedBeliefDegreeM + aggregatedBeliefDegreeL)  
         
        finalAggregatedBeliefDegreeM = aggregatedBeliefDegreeM/(aggregatedBeliefDegreeH + aggregatedBeliefDegreeM + aggregatedBeliefDegreeL)
        
        finalAggregatedBeliefDegreeL = aggregatedBeliefDegreeL/(aggregatedBeliefDegreeH + aggregatedBeliefDegreeM + aggregatedBeliefDegreeL) 
          
        brbH = finalAggregatedBeliefDegreeH
        brbM = finalAggregatedBeliefDegreeM 
        brbL = finalAggregatedBeliefDegreeL       
            
        if (finalAggregatedBeliefDegreeH > finalAggregatedBeliefDegreeM) and (finalAggregatedBeliefDegreeH > finalAggregatedBeliefDegreeL):
            aqi = (201 + 299*finalAggregatedBeliefDegreeH) + ((200*finalAggregatedBeliefDegreeM)/2)
            print ("AQI predicted by BRB-CNN:",aqi)    
            
        elif (finalAggregatedBeliefDegreeL > finalAggregatedBeliefDegreeM) and (finalAggregatedBeliefDegreeL > finalAggregatedBeliefDegreeH): 
            aqi = (100*(1 - finalAggregatedBeliefDegreeL)) + ((200*finalAggregatedBeliefDegreeM)/2) 
            print ("AQI predicted by BRB-CNN:",aqi)
  
        elif (finalAggregatedBeliefDegreeM > finalAggregatedBeliefDegreeH) and (finalAggregatedBeliefDegreeM > finalAggregatedBeliefDegreeL):
            if finalAggregatedBeliefDegreeH > finalAggregatedBeliefDegreeL:
                aqi = (101 + 99*finalAggregatedBeliefDegreeM) + ((500*finalAggregatedBeliefDegreeH)/2)
                print ("AQI predicted by BRB-CNN: ",aqi)
      
            elif (finalAggregatedBeliefDegreeL > finalAggregatedBeliefDegreeH):   
                aqi = (101 + 99*finalAggregatedBeliefDegreeM) + ((100*finalAggregatedBeliefDegreeL)/2)
                print ("AQI predicted by BRB-CNN:",aqi)  
          
        print("aqi ",aqi)     
                
        if aqi >= 301: 
            aqi6 = (aqi- 301)/199.0  
 
        elif (aqi >= 201)and (aqi <= 300.9999999999): 
            aqi6 = (aqi- 201)/99.0     

        elif (aqi >= 151)and (aqi <= 200.9999999999):
            aqi6 = (aqi- 151)/49.0 

        elif((aqi >= 101)and (aqi <= 150.9999999999)): 
            aqi6 = (aqi- 101)/49.0   

        elif((aqi >= 51)and (aqi <= 100.9999999999)): 
            aqi6 = (aqi- 51)/49.0    
 
        elif(aqi <= 50.9999999999):    
            aqi6 = (aqi/49.0)    
             
        print("aqi6 ",aqi6) 
        print ("BRB-CNN integrated Belief Degree for Hazardous AQI:",finalAggregatedBeliefDegreeH*aqi6)   
        print ("BRB-CNN integrated Belief Degree for Very Unhealthy AQI:",finalAggregatedBeliefDegreeH*(1-aqi6)) 
        print ("BRB-CNN integrated Belief Degree for Unhealthy AQI: ",finalAggregatedBeliefDegreeM*aqi6)
        print ("BRB-CNN integrated Belief Degree for Unhealthy (Sensitive Groups) AQI:",finalAggregatedBeliefDegreeM*(1-aqi6)) 
        print ("BRB-CNN integrated Belief Degree for Moderate AQI:",finalAggregatedBeliefDegreeL*aqi6) 
        print ("BRB-CNN integrated Belief Degree for Good AQI:",finalAggregatedBeliefDegreeL*(1-aqi6))
        
        return aqi

#def getAQI(x):     
#    cbd_de0 = x[0] 
#    cbd_de1 = x[1] 
#    cbd_de2 = x[2]
#    ruleBase()
     
    #aqi = x[0] + x[1] + x[2] + x[3]   
    #print("Diff Evo BRB/CNN AQI is ",aqi) 
#   return cbd_de0 + cbd_de1 + cbd_de2   
   
#def main():
#    ruleBase()       
#    takeInput()  
    #showTransformedInput() unnecessary      
#    takeCnnOutput() 
#    calculateMatchingDegreeBrbCnn() 
    #showMatchingDegree() unnecessary
#    showActivationWeight()   
#    updateBeliefDegree()    
#    aggregateER_BrbCnn()
    #getAQI(x) unnecessary

#main()        
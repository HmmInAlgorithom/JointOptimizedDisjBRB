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
    temp_consequentBeliefDegree = [x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17]]   
        
    de0 = x[0]/(x[0] + x[1] + x[2])
    de1 = x[1]/(x[0] + x[1] + x[2])
    de2 = x[2]/(x[0] + x[1] + x[2]) 
    de3 = x[3]/(x[3] + x[4] + x[5]) 
    de4 = x[4]/(x[3] + x[4] + x[5])
    de5 = x[5]/(x[3] + x[4] + x[5])
    de6 = x[6]/(x[6] + x[7] + x[8]) 
    de7 = x[7]/(x[6] + x[7] + x[8])
    de8 = x[8]/(x[6] + x[7] + x[8])
    de9 = x[9]/(x[9] + x[10] + x[11])
    de10 = x[10]/(x[9] + x[10] + x[11])
    de11 = x[11]/(x[9] + x[10] + x[11]) 
    de12 = x[12]/(x[12] + x[13] + x[14])
    de13 = x[13]/(x[12] + x[13] + x[14])
    de14 = x[14]/(x[12] + x[13] + x[14]) 
    de15 = x[15]/(x[15] + x[16] + x[17]) 
    de16 = x[16]/(x[15] + x[16] + x[17]) 
    de17 = x[17]/(x[15] + x[16] + x[17]) 
          
    consequentBeliefDegree = [de0, de1, de2, de3, de4, de5, de6, de7, de8, de9, de10, de11, de12, de13, de14, de15, de16, de17] 
    attrw1 = x[18]    
    attrw2 = x[19] 
    irulewt1 = x[20]      
    irulewt2 = x[21]  
    irulewt3 = x[22]
    irulewt4 = x[23] 
    irulewt5 = x[24] 
    irulewt6 = x[25]
    print("Inside ruleBase(x) relativeWeight1 ",attrw1,"relativeWeight2 ",attrw2) 
    #consequentBeliefDegree = [cbd_0, cbd_1, cbd_2, cbd_3, cbd_4, cbd_5, cbd_6, cbd_7, cbd_8]
    for u in range(18):   
        print(consequentBeliefDegree[u])   
    #transformInput1(384.5891688061617)  
    PMH = 0 + (x[26] * 499.4)
    PMUM = 0 + (x[27] * 499.4)  #500.4     
    PMM = 0 + (x[28] * 499.4)
    PMLM = 0 + (x[29] * 499.4)   #35.5
    PMSL = 0 + (x[30] * 499.4)
    PML = 0 + (x[31] * 499.4) 
    
    transformInput1(s,PMH,PMUM,PMM,PMLM,PMSL,PML)   
    transformInput2(c,PMH,PMUM,PMM,PMLM,PMSL,PML)    
    calculateMatchingDegreeBrbCnn(attrw1,attrw2, irulewt1, irulewt2, irulewt3, irulewt4, irulewt5, irulewt6)    
    showActivationWeight()
    updateBeliefDegree()  
    result = aggregateER_BrbCnn()
    return result       

def transformInput1(i,j,k,l,m,n,p):   
    global H1 
    global UM1  
    global M1   
    global LM1 
    global SL1
    global L1 
             
    PM_H = j
    PM_UM = k 
    PM_M = l
    PM_LM = m
    PM_SL = n 
    PM_L = p
          
    print("Inside transformInput1() Input is ",i,"PM_H ", PM_H,"PM_UM",PM_UM, "PM_M ",PM_M,"PM_LM", PM_LM,"PM_SL", PM_SL, "PM_L ",PM_L) 
        
    if (i >= PM_H): 
        H1 = 1 
        UM1 = 0
        M1 = 0
        LM1 = 0
        SL1 = 0
        L1 = 0

    elif (i == PM_UM):
        H1 = 0 
        UM1 = 1
        M1 = 0
        LM1 = 0
        SL1 = 0
        L1 = 0 

    elif (i == PM_M):
        H1 = 0
        UM1 = 0 
        M1 = 1
        LM1 = 0
        SL1 = 0
        L1 = 0
    
    elif (i == PM_LM):
        H1 = 0
        UM1 = 0 
        M1 = 0
        LM1 = 1
        SL1 = 0
        L1 = 0    

    elif (i == PM_SL):
        H1 = 0
        UM1 = 0 
        M1 = 0
        LM1 = 0
        SL1 = 1  
        L1 = 0        
    
    elif (i <= PM_L):
        H1 = 0
        UM1 = 0       
        M1 = 0
        LM1 = 0
        SL1 = 0
        L1 = 1    
    
    elif (i < PM_H) and (i > PM_UM): 
        UM1 = (PM_H-i)/(PM_H-PM_UM) 
        H1 = 1 - UM1
        M1 = 0.0
        L1 = 0.0         
        LM1 = 0.0
        SL1 = 0.0
   
    elif (i < PM_UM) and (i > PM_M): 
        M1 = (PM_UM-i)/(PM_UM-PM_M)   
        UM1 = 1 - M1
        H1 = 0.0
        L1 = 0.0 
        LM1 = 0.0
        SL1 = 0
 
    elif (i < PM_M) and (i > PM_LM): 
        LM1 = (PM_M-i)/(PM_M-PM_LM)   
        M1 = 1 - LM1 
        H1 = 0.0 
        UM1 = 0.0 
        L1 = 0.0
        SL1 = 0
        
    elif (i < PM_LM) and (i > PM_SL):
        SL1 = (PM_LM-i)/(PM_LM-PM_SL)   
        LM1 = 1 - SL1
        H1 = 0.0
        UM1 = 0.0
        M1 = 0.0 
        L1 = 0.0
      
    elif (i < PM_SL) and (i > PM_L): 
        L1 = (PM_SL-i)/(PM_SL-PM_L)   
        SL1 = 1 - L1
        H1 = 0.0
        UM1 = 0.0
        M1 = 0.0
        LM1 = 0.0
        
    print("Inside transformInput1(), H1", H1, "UM1 ", UM1, "M1 ",M1,"LM1 ", LM1, "SL1 ", SL1, "L1 ", L1)   
   
def transformInput2(i,j,k,l,m,n,p):
    global H2 
    global UM2  
    global M2   
    global LM2 
    global SL2
    global L2 
              
    PM_H = j 
    PM_UM = k 
    PM_M = l
    PM_LM = m
    PM_SL = n 
    PM_L = p
          
    print("Inside transformInput2() Input is ",i,"PM_H ", PM_H,"PM_UM",PM_UM, "PM_M ",PM_M,"PM_LM", PM_LM,"PM_SL", PM_SL, "PM_L ",PM_L) 
        
    if (i >= PM_H): 
        H2 = 1 
        UM2 = 0
        M2 = 0
        LM2 = 0
        SL2 = 0
        L2 = 0

    elif (i == PM_UM):
        H2 = 0 
        UM2 = 1
        M2 = 0
        LM2 = 0
        SL2 = 0
        L2 = 0 

    elif (i == PM_M):
        H2 = 0
        UM2 = 0 
        M2 = 1
        LM2 = 0
        SL2 = 0
        L2 = 0
    
    elif (i == PM_LM):
        H2 = 0
        UM2 = 0 
        M2 = 0
        LM2 = 1
        SL2 = 0
        L2 = 0    

    elif (i == PM_SL):
        H2 = 0
        UM2 = 0 
        M2 = 0
        LM2 = 0
        SL2 = 1  
        L2 = 0        
    
    elif (i <= PM_L):
        H2 = 0
        UM2 = 0       
        M2 = 0
        LM2 = 0
        SL2 = 0
        L2 = 1    
    
    elif (i < PM_H) and (i > PM_UM): 
        UM2 = (PM_H-i)/(PM_H-PM_UM) 
        H2 = 1 - UM2
        M2 = 0.0
        L2 = 0.0         
        LM2 = 0.0
        SL2 = 0.0
   
    elif (i < PM_UM) and (i > PM_M): 
        M2 = (PM_UM-i)/(PM_UM-PM_M)   
        UM2 = 1 - M2
        H2 = 0.0
        L2 = 0.0 
        LM2 = 0.0
        SL2 = 0
 
    elif (i < PM_M) and (i > PM_LM): 
        LM2 = (PM_M-i)/(PM_M-PM_LM)   
        M2 = 1 - LM2 
        H2 = 0.0 
        UM2 = 0.0 
        L2 = 0.0
        SL2 = 0
        
    elif (i < PM_LM) and (i > PM_SL):
        SL2 = (PM_LM-i)/(PM_LM-PM_SL)   
        LM2 = 1 - SL2
        H2 = 0.0
        UM2 = 0.0
        M2 = 0.0 
        L2 = 0.0
       
    elif (i < PM_SL) and (i > PM_L): 
        L2 = (PM_SL-i)/(PM_SL-PM_L)   
        SL2 = 1 - L2
        H2 = 0.0
        UM2 = 0.0
        M2 = 0.0
        LM2 = 0.0
        
    print("Inside transformInput1(), H2", H2, "UM2 ", UM2, "M2 ",M2,"LM2 ", LM2, "SL2 ", SL2, "L2 ", L2)   
     
def takeInput():
    global a1     
    temp_a1 = input("Insert value for PM2.5 (between 0 and 500.4 µg/m3): ")
    a1 = float(temp_a1)   
    #transformInput1(a1)  
  
def calculateMatchingDegreeBrbCnn(aw1,aw2,irw1,irw2,irw3,irw4,irw5,irw6):
    antattrw1 = aw1 
    antattrw2 = aw2
    global initialRuleWeight      
    initialRuleWeight = [irw1, irw2, irw3, irw4, irw5, irw6]      
    increment = 0     
    global matchingDegree 
    matchingDegree = [1.51, 1.51, 1.51, 1.51, 1.51, 1.51]
     
    global trainedMatchingDegree
    trainedMatchingDegree = [1.51, 1.51, 1.51, 1.51, 1.51, 1.51]   
  
    ti1 = [H1, UM1, M1, LM1, SL1, L1]  
    #print("ti1[0] is ")         
    #print(ti1[0])  
    #ti2 = array.array('f', [normalized_cnn_severe_degree, normalized_cnn_mild_degree, normalized_cnn_nominal_degree])
    ti2 = [H2, UM2, M2, LM2, SL2, L2] 
         
    for c in range(6):          
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
    activationWeight = [1.51, 1.41, 1.45, 1.45, 1.45, 1.45]       
    temp_activationWeight = [1.57, 1.81, 1.92, 1.45, 1.45, 1.45]    
    for x in range(6):       
        totalWeight += matchingDegree[x]           
     
    for counter in range(6):
        print("Inside showActivationWeight() initialRuleWeight[counter] is ",initialRuleWeight[counter])             
        inter = initialRuleWeight[counter] * trainedMatchingDegree[counter]          
        temp_activationWeight[counter] = inter/totalWeight   
            
    for naw in range(6):
        totalActivationWeight += temp_activationWeight[naw]        
       
    for fin in range(6):
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
    
    if (H1 + UM1 + M1 + LM1 + SL1 + L1) < 1:
        sumAntAttr1 = H1 + UM1 + M1 + LM1 + SL1 + L1
        update = 1 
      
    if (H2 + UM2 + M2 + LM2 + SL2 + L2) < 1:
        sumAntAttr2 = H2 + UM2 + M2 + LM2 + SL2 + L2
        update = 1 
     
    if update == 1:
        beliefDegreeChangeLevel = (sumAntAttr1 + sumAntAttr2)/numberOfAntAttributes 

        for go in range(18):
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
    ruleWiseBeliefDegreeSum = [1.51, 1.51, 1.51, 1.51, 1.51, 1.51]  
    
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
    
    for s in range(18): 
        print("Inside aggregateER)BrbCNN() consequentBeliefDegree: ",consequentBeliefDegree[s])
     
    for t in range(6): 
        parse = t * 3   
        ruleWiseBeliefDegreeSum[t] = consequentBeliefDegree[parse] + consequentBeliefDegree[parse+1] + consequentBeliefDegree[parse+2]
 
    for rule in range(6):  
        part11 *= (activationWeight[rule] * consequentBeliefDegree[move1] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))         
        move1 += 3 
  
    for rule in range(6):
        part12 *= (activationWeight[rule] * consequentBeliefDegree[move2] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))        
        move2 += 3 
 
    for rule in range(6):
        part13 *= (activationWeight[rule] * consequentBeliefDegree[move3] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))        
        move3 += 3

    part1 = (part11 + part12 + part13)
    
    for rule in range(6):
        part2 *= (1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule])) 
    
    value = part1 - part2 
    
    meu = 1/value 
 
    for rule in range(6):
        numeratorH1 *= (activationWeight[rule] * consequentBeliefDegree[action1] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))        
        action1 += 3

    for rule in range(6):
        numeratorH2 *= (1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))              
      
    numeratorH = meu * (numeratorH1 - numeratorH2) 
    
    for rule in range(6):  
        denominatorH1 *= (1 - activationWeight[rule])        
 
    denominatorH = 1 - (meu * denominatorH1)
    
    aggregatedBeliefDegreeH = (numeratorH/denominatorH)
    
    for rule in range(6):
        numeratorM1 *= (activationWeight[rule] * consequentBeliefDegree[action2] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))        
        action2 += 3 

    numeratorM = meu * (numeratorM1 - numeratorH2) 
    aggregatedBeliefDegreeM = (numeratorM/denominatorH)  
    
    for rule in range(6):
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
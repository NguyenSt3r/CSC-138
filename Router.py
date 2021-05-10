import re

#Used to set the priorities for initial buffer
def setPriorityForBuffer(priorityStr,priorityList):
    counter=0
    outgoingPkt=[]
    #Set priority for H first
    for i in range(0,3):
        if priorityStr[i]=='H':
            outgoingPkt.append(priorityList[counter])
            counter+=1
        else:
            outgoingPkt.append('NA')
    #Set priority for L next
    for i in range(0,3):
        if outgoingPkt[i]=='NA':
            outgoingPkt[i]=priorityList[counter]
            counter+=1
    return outgoingPkt

def getPriority(numPackets,priorityStr):
    outputStr = " " 
    outgoingPkt=[]
    priorityList=[]
    for i in range(0,numPackets):
        priorityList.append(str(i))
    if numPackets<=0:
        return 'Wrong input: the number of packets must be greater than 0.'
    elif numPackets!=len(priorityStr):
        return 'Wrong input: the number of packets is wrong.'
    else:
        pattern = re.compile('^[LH]+$')
        if not re.search(pattern, priorityStr):
            return 'Wrong input: the priority must be H or L'
        if numPackets==3:
            outgoingPkt=setPriorityForBuffer(priorityStr,priorityList)
        elif numPackets>3:
            #For first 3 packets
            outgoingPkt=setPriorityForBuffer(priorityStr,priorityList)
            #For remaining packets
            counter=3
            #Set priority for H first
            for i in range(3,len(priorityStr)):
                if priorityStr[i]=='H':
                    outgoingPkt.append(priorityList[counter])
                    counter+=1
                else:
                    outgoingPkt.append('NA')
            #Set priority for L next
            for i in range(3,len(priorityStr)):
                if outgoingPkt[i]=='NA':
                    outgoingPkt[i]=priorityList[counter]
                    counter+=1
                    
        for i in outgoingPkt:
            outputStr=outputStr+i+" "
            
    return outputStr
                    
def main():
    #Get input from user
    inputStr=input("Input:")
    inputList=inputStr.split(" ")
    numPackets=int(inputList[0])
    priorityStr=inputList[1]
    #Call function and print outgoingpacket string
    print("Output:",getPriority(numPackets,priorityStr))
    

#Driver code
main()

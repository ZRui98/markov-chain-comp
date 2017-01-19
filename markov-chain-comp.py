from midiutil.MidiFile import MIDIFile
from random import randint
lookUp={'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11,0:0.25,1:0.5,2:1,3:2,4:4}
#holds all possible next notes of a certain note
class nextNotes():
    def __init__(self):
        self.nNotes=[0]*640
        self.rests=[0]*5
        self.totalNotes=0

    def addNextNote(self,noteValue):
        self.nNotes[noteValue]+=1
        self.totalNotes+=1
    def addNextRest(self, restValue):
        self.rests[restValue]+=1
        self.totalNotes+=1
    def getRandomNote(self):
        if(self.totalNotes>0):
            randValue = randint(1,self.totalNotes)
            i=0
            while randValue>0 and i<640:
                randValue-=self.nNotes[i]
                i+=1
            if(randValue<=0):
                return i-1
            else:
                i=0
                while randValue>0:
                    randValue-=self.rests[i]
                    i+=1
                return 639+i
        return -1

possibleStarts=[]
def loadMusic(f):
    ns=f.read().split()
    for i in range(len(ns)):
        ns[i]=ns[i].split(';')
    if(ns[0][0]=='R'):
        possibleStarts.append(640+int(ns[0][1]))
    else:
        possibleStarts.append(lookUp[ns[0][0]]+int(ns[0][1])*12+int(ns[i][2])*128)
    for i in range(len(ns)-1):

        if(ns[i][0]=='R' and ns[i+1][0]=='R'):
            ajm[640+int(ns[i][1])].addNextRest(int(ns[i+1][1]))
        elif(ns[i][0]=='R'):
            ajm[640+int(ns[i][1])].addNextNote(lookUp[ns[i+1][0]]+int(ns[i+1][1])*12+int(ns[i+1][2])*128)
        elif(ns[i+1][0]=='R'):
            ajm[lookUp[ns[i][0]]+int(ns[i][1])*12+int(ns[i][2])*128].addNextRest(int(ns[i+1][1]))
        else:
            ajm[lookUp[ns[i][0]]+int(ns[i][1])*12+int(ns[i][2])*128].addNextNote(lookUp[ns[i+1][0]]+int(ns[i+1][1])*12+int(ns[i+1][2])*128)

#adjacency matrix that holds # of occurrences of every note from each note
ajm={}
for i in range(645):
    ajm[i]=nextNotes()

while True:
    fileName= input("Enter the location of the music data or type 'f' to finish: ")
    if(fileName=='f'):
        break
    loadMusic(open(fileName))

mf = MIDIFile(1)
tempo=int(input("Enter the tempo in bpm: "))
mf.addTempo(0, 0, tempo)
volume = 100

duration =int(input("Enter the duration in minutes: "))
#starting note
currentNote=possibleStarts[randint(0,len(possibleStarts)-1)]
restShift=0
time=0
while time<tempo*duration:
    print(time,currentNote,currentNote//128)
    if(currentNote>639):
        time+=(lookUp[currentNote-640])
    else:
        mf.addNote(0,0,currentNote%128,time,lookUp[currentNote//128],volume)
        time+=lookUp[currentNote//128]
    nextNote=ajm[currentNote].getRandomNote()
    if(nextNote==-1):
        print("No Notes After",currentNote)
        break
    currentNote=nextNote
with open("algo-comp.mid", 'wb') as outf:
    mf.writeFile(outf)
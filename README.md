#Markov Chain Algorithmic Compositions
Using Markov Chains and MIDIUtil to generate MIDI files

#Usage
If music data is ever to be added, the syntax is written as the 'X;O;L' for notes where X is one of 
C,C\#,D,D\#,E,F,F\#,G,G\#,A,A\#,B, O is the octave of the midi note ranging from 0-10, and L specifies 
the length of the note, ranging from 0-4, where the following array at index L is the length [0.25,0.5,1,2,4](1 is one beat). 
The syntax for rests is 'R;L', where L is the length of the rest, following the same rules as the length
variable of the note. The R distinguishes that the data entry is a rest. Spaces are used to seperate these
elements.


#Libraries
MIDIUtil: https://pypi.python.org/pypi/MIDIUtil/1.1.1
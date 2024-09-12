import re

# Input song text
song_text = """
[Intro]
Bm F# A E
G D Em F#7
Bm F# A E
G D Em
F#7

[Verse 1]
Bm                         F#
  On a dark desert highway,  
cool wind in my hair.
A                      E
 Warm smell of colitas, rising up
 through the air.
G                         D
 Up ahead in the distance, I saw a
 shimmering light.
Em
  My head grew heavy and my 
sight grew dim,
F#7
   I had to stop for the night.
Bm                               F#
  There she stood in the doorway;  
I heard the mission bell,
A                                  
 And I was thinking to myself, 
           E
"this could be heaven or this could
 be hell".
G                        D
 Then she lit up a candle and she
 showed me the way.
Em                         
  There were voices down 
           F#7
the corridor,   I thought I
 heard them say...

[Chorus]
G                            D   
 Welcome to the Hotel California,
        F#7                  Bm
 such a lovely place, such a 
lovely face.
G                           
Plenty of room at the Hotel 
       D        Em          
California, any time of 
          F#7
year, you can find it here.

[Verse 2]
Bm                           F#
  Her mind is Tiffanytwisted,  
she got the Mercedes bends.
A                               
 She got a lot of pretty, pretty
      E
 boys, that she calls friends.
G                                
 How they dance in the courtyard,
 D
 sweet summer sweat.
Em                       F#7
  Some dance to remember,   
some dance to forget.
Bm                           
  So I called up the Captain,
F#
  "please bring me my wine".
       A                           
He said "we haven't had that spirit
           E
 here since nineteen sixty nine".
G                                  
 And still those voices are calling
      D
 from far away.
Em                               
  Wake you up in the middle of 
       F#7
the night   just to hear them 
say...

[Chorus]
G                            D   
 Welcome to the Hotel California,
        F#7                  Bm
 such a lovely place, such a 
lovely face.
     G                         
They living it up at the Hotel 
       D           Em          
California. What a nice 
              F#7
surprise, bring your alibis.

[Verse 3]
Bm                       F#
  Mirrors on the ceiling,  the 
pink champagne on ice.
            A                 
And she said "we are all just 
               E
prisoners here, of our own 
device".
G                             
 And in the master's chambers,
D
 they've gathered for the 
feast.
Em                             
  They stab it with their 
                   F#7
steely knives, but they just 
can't kill the beast.
Bm                            
  Last thing I remember, I was
F#
  running for the door.
A                                 
 I had to find the passage back to
     E
 the place I was before.
G                                  
 "Relax" said the night man, we are
D
 programmed to receive.
Em                             
  You can check out any time 
       F#7
you like,   but you can never 
leave.

[Guitar Solo]
Bm F# A E
G D Em F#7
Bm F# A E
G D Em F#7
Bm F# A E
G D Em F#7

[Outro]
Bm F# A E
G D Em F#7
Bm F# A E
G D Em F#7
"""

def convert_to_chordpro(song_text):
    # Split the text into lines
    lines = song_text.strip().split('\n')
    chordpro_lines = []
    
    # Process each line
    for line in lines:
        # Check if line is a section (e.g., [Verse], [Chorus])
        if re.match(r'^\[.*\]$', line):
            chordpro_lines.append(line.strip())
        # Check if line is a chord line (contains only chords)
        elif re.match(r'^[A-G][#bm7dim/]*\s*$', line.strip()):
            chords = line.strip().split()
            chordpro_line = ' '.join([f'[{chord}]' for chord in chords])
            chordpro_lines.append(chordpro_line)
        else:
            # Process lyrics with chords
            words = line.strip().split()
            chordpro_line = ''
            for word in words:
                if re.match(r'^[A-G][#bm7dim/]*$', word):
                    chordpro_line += f'[{word}] '
                else:
                    chordpro_line += f'{word} '
            chordpro_lines.append(chordpro_line.strip())
    
    return '\n'.join(chordpro_lines)

# Convert song text to ChordPro format
chordpro_text = convert_to_chordpro(song_text)

# Output the ChordPro formatted song
print(chordpro_text)

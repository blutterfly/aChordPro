import os
import re

def convert_to_chordpro(song_text):
    """
    Convert song text to ChordPro format, preserving chord placement directly above lyrics
    and enclosing chords in brackets while keeping the original spaces.
    """
    # Split the text into lines
    lines = song_text.strip().split('\n')
    chordpro_lines = []
    previous_chords_line = None  # Storage for the previous chords line
    
    # Process each line
    for line in lines:
        line = line.rstrip()
        # Check if line is a section (e.g., [Verse], [Chorus])
        if re.match(r'^\[.*\]$', line):
            chordpro_lines.append(line.strip())
            previous_chords_line = None  # Reset chord line for new section
        # Check if line is a chord line (contains only chords)
        elif all(re.match(r'^[A-G][#bm7dim/]*$', word) for word in line.strip().split()):
            # Store the chord line to be placed above the next lyrics line
            previous_chords_line = line
        else:
            # It's a lyrics line
            if previous_chords_line:
                # Create a new line for chords to align above the lyrics
                chords_line = previous_chords_line
                
                # Insert brackets around each chord, keeping the spaces intact
                bracketed_chords_line = re.sub(r'([A-G][#bm7dim/]*)', r'[\1]', chords_line)

                # Append the chords and lyrics lines in order
                chordpro_lines.append(bracketed_chords_line)
                chordpro_lines.append(line)
                previous_chords_line = None  # Clear after use
            else:
                # If no chords line, just add the lyrics line
                chordpro_lines.append(line)
    
    return '\n'.join(chordpro_lines)

def process_files_in_directory(directory):
    """
    Process all .txt files in the specified directory, convert them to ChordPro format,
    and save them as .chordpro files.
    """
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            txt_file_path = os.path.join(directory, filename)
            
            # Read the content of the .txt file
            with open(txt_file_path, 'r') as file:
                song_text = file.read()
            
            # Convert the content to ChordPro format
            chordpro_text = convert_to_chordpro(song_text)
            
            # Create the output filename with .chordpro extension
            chordpro_filename = filename.replace('.txt', '.chordpro')
            chordpro_file_path = os.path.join(directory, chordpro_filename)
            
            # Save the ChordPro formatted song to a new file
            with open(chordpro_file_path, 'w') as file:
                file.write(chordpro_text)
            
            print(f"Converted '{filename}' to '{chordpro_filename}'.")

if __name__ == "__main__":
    # Specify the directory containing the .txt files
    directory = '.'

    # Process all .txt files in the directory
    process_files_in_directory(directory)

    print("All .txt files have been successfully converted to ChordPro format.")

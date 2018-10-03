# Plagiarism Detection

## Instruction
- To run this file, simply do a command "python solution.py". Then, type in the input according to the format (syns, file1, file2, _optional: tuple size_) Ex. "python solution.py syns.txt file1.txt file2.txt 3"
- Note: drag the syns, file1, file2 to the root directory. Or else, you have to locate them in the input.

## Design
- Created a SynsDict class that takes in all the synonyms and stores them in a dictionary (hashmap) individually. Ex. `run jog sprint` will be stored as `run: [jog, sprint]`, `jog: [run, sprint]`, and `sprint: [run, jog]`.
- The dic variable inside SynsDict is a **class variable**. It is shared among all the instances of the class.
- The reason behind that is to support constant lookup time for each word. 
- Using sliding window technique to solve the n-tuple problem. (The window size is the tuple size.) Given the window size, you slide through the whole line. Upon each slide, you check the tuples to see if they are the same.
- Using composition class design. You pass in the class SynsDic into NTuple to support the dictionary lookup.
- Throw error upon two conditions:
	- files failed to open
	- tuple size is bigger than the size of the whole line 

## Assumption
- For file1 and file2, each line has the same length and there should be the same number of lines.
- Tuple size entered is an integer.
- When comparing two words to see if they are synonyms, if one of them is not in the dictionary, then it sets to `False` on default.
- I am comparing words by words. So "go for a run" and "for a run go" will result in a low percentage.
- All the files are in the right format
	- One line at a time
	- words are separated by space 

## Limitation
- Different language is not supported
- Only work with the assumption listed above 
- Special character is not supported. Ex. `go for a run, man` and `go for a run man` would fail because `run,` is compared to `run`.

## Test
- 1) Default case: `go for a run` vs. `go for a jog`
- 2) Two synonyms in the line
- 3) All synonyms in diff order: `tic tac toe` vs. `toe tic tac`
- 4) No synonym
- 5) Long line
- 6) Re use synonyms: `run` vs `ran` (`run` is listed above already with `jog` and `sprint`)

## Down the Road
- Could make the SynsDic class more abstract. Then, implement different sub-classes that support different languages.
- Could store the synonyms in a persistent database for future reuseability.
- Could implement a better txt file parser. Specifically for reusing the program on different platform, such as web scraping. 


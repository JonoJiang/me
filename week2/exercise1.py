"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# I think this defines a sentence
some_words = ['what', 'does', 'this', 'line', 'do', '?'] #It defined the list of words
#Replace a specific word with another
for word in some_words: #it printed the words in a column
    print(word)
#Replace a specific letter with another
for x in some_words: #it printed the words in a column
    print(x)
#Will print the sentence with any adjustments made
print(some_words) #it printed the list of words
#prints sentence if the length of the sentence is more than 3 words
if len(some_words) > 3: #checked if the list had more than 3 words
    print('some_words contains more than 3 words') #printed the sentence as there were >3
#orints the system, node, release, version, machine, and processor.
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) #displayed this computer's specifications

usefulFunction() #displayed current directory

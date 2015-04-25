def c_html(title, desc):
	html_t1 = """
<div class="art">
   <h4>""" + title + "</h4>"
	html_t2 = """
   <p>""" + desc + "</p>"
	html_t3 = """
</div> """

	html_all = html_t1 + html_t2 + html_t3
	return html_all

def pull_head(notes):
    start_location = notes.find('HEAD:')
    end_location = notes.find('DESC:')
    head = notes[start_location+6 : end_location-1]
    return head

def pull_desc(notes):
    start_location = notes.find('DESC:')
    desc = notes[start_location+6:]
    return desc
    
def pull_concept_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('HEAD:')
        next_concept_end = text.find ('HEAD:', next_concept_start + 1)
        if next_concept_end >= 0:
            notes = text[next_concept_start:next_concept_end]
        else:
            next_concept_end = len(text)
            notes = text[next_concept_start:]
        text = text[next_concept_end:]
    return notes


text_html = """HEAD: Computer Programming and Computer Science 
DESC: Computer Programming  - is the process of designing, writing, testing, debugging, and maintaining the source code of computer programs. 
Computer Science  - is the study of computers and their architecture, languages, and applications, in all aspects, as well as the mathematical structures that relate to computers and computation.
HEAD: Programming Language
DESC: Programming Language is a formal constructed language designed to communicate instructions to a machine, particularly a computer.  Programming languages can be used to create programs to control the behavior of a machine or to express algorithms.
HEAD: Backus-Naur Form
DESC: The purpose of Backus Naur Form is to precisely describe exactly the language in a way thats very simple and concise.  BNF is often used to describe the syntax of languages used in computing, such as computer programming languages, document formats, instruction sets and communication protocols.  <em>non-terminal -> replacement -> terminal</em> 
HEAD: Python
DESC: Python  is a widely used general-purpose, high-level programming language.   Python interpreter  is a program that reads Python programs and carries out their instructions.
HEAD: The Variable
DESC: 1. What is a Variable?  A symbolic name for (or reference to) information.  The variable's name represents what information the variable contains.  In Python you can use a variable to create a name and use the name to refer to a variable.  Variables can vary in that it will refer to the most recent value given to the referenced variable.   2.What does it mean to assign a value to a variable?  It means to symbolically associate a specific piece of information with a name.  Any operations that are applied to this "name" (or variable) must hold true for any possible values.   3.What is the difference between what the equals (=) means in math versus in programming?   In math = is used for equality or sum where in coding it means assignment.  Think of it as an arrow &lt;-.
HEAD: Strings
DESC: A  String  is a sequence of characters surrounded by quotes.  Ex: 'i am a string'.  Double quotes can be used but must begin and end with double quotes.  Ex: "i perfer to use double quote!"   You can concatenate 2 strings using the + operator.  You cannot concatenate a string and an integer.   You can also multiply strings using the *. 
HEAD: Index Strings
DESC: You can extract subsequences from a string by indexing.  Using the square brackets [] after a string will enable you to extract parts of that string.  The characters of a string are indexed starting with the leftmost character being 0 and ascending (left to right).  The characters can also be selected from the rightmost starting at -1 and descending (right to left).  Ex: &lt;string&gt; [&lt;expression&gt;] -&gt; one-character string 
HEAD: Selecting Sub Sequences
DESC: You can select subsequences from a string by creating a start and stop expression, where your starting position start and ending on position stop -1.  This will basically allow you to select a subsequence of continuous characters in a string.  &lt;string&gt;[&lt;expression&gt;:&lt;expression&gt;]         Word = 'assume'   Word [4:6] - &gt; me
HEAD: Find Strings in String
DESC: The  Find  operation gives us the ability to find a substring in a big string.  Find is a procedure that works on strings.  Find gives the number of the first postion (number) in the search string where the targert string occurs.  If the number is not found it will return a -1.  Ex: Pythagoras = 'There is a geometry in the humming of the strings, there is music in the spacing of the spheres.'   print pythagoras.find ('string') = 40
HEAD: Function
DESC: A  Function  is a type of procedure or routine.  Some programming languages make a distinction between a function, which returns a value, and a procedure, which performs some operation but does not return a value.  Inputs can also be referred to as operands or arguments.
HEAD: The Difference Between Making and Using a Function
DESC: When you  Make  a function you define a procedure or code block to perform a task.  Ex: def sum(x,x):.  When you  Use  a function you call on a particular procedure previously defined.  Ex: print sum(x,x).
HEAD: How Functions Help Programmers Avoid Repetition
DESC: Functions help programmers avoid repetition in that when there are some type of operation or calculation to be repeated numerous times. We can define it as a function or procedure and then call on it as needed.
HEAD: A Function Without a Return Statement
DESC: A  Return Statement  causes your function to exit and hands back a value to its caller.  If the return statement is not used the output value will be  None .
HEAD: Boolean
DESC: Boolean expressions are expressions that result in the value of either TRUE or FALSE.  Boolean consist of operators such as AND, OR, and NOT.
HEAD: If and Else
DESC: IF  is a statement used to make comparison.  You make your code do something different based on the results of the comparison.  IF statement can be followed by and else statement, which executes when the Boolean expression is false.  An  else  statement contains the block of code that executes if the conditional expression in the IF statement resolves to 0 or a false value.   Ex: if &lt;testexpression&gt;:               <br>  &lt;block&gt;
HEAD: OR
DESC: If the first expression evlauates to True, the value is true and the second expression is not evaluated.   Ex: print True or False - Value is True.   If the first expression evaluates to False, the value is the value of the second expression.   Ex: print False or False - Value is False.
HEAD: Comparison Operators
DESC: ==  Checks if the value of two operands are equal or not, if yes then condition becomes true.  !=  Checks if the value of tow operands are equal or not, if the values are not equal then the condition becomes true.  &lt;  Checks if the value of left operand is greater than the value of the right operand, if yes then condition becomes true.  &gt;  Checks if the value of the left operand is less than the vaule of the right operand, if yes then the condition becomes true.
HEAD: While Loops
DESC: A  While  loop statement in Python repeatedly executes a target statement as long as a given condition is true.  Ex: while &lt;testexpression&gt;:
<br> &lt;block&gt;  Break statement gives us a way to stop the loop even when test condition is true.  Ex: while &lt;testexpression&gt;:
<br>               &lt;code&gt;
<br>               if&lt;breaktest&gt;:            
<br>               break             
<br>             &lt;morecode&gt;             
<br>             &lt;afterwhile&gt;                                           
HEAD: Debugging
DESC: Traceback tells you what line code crashed on, what file it was running, and how it got there.  The information given especially the line number and function name can focus your attention on the line of code that maybe going wrong.  Even if it is not on the line given it is upstream of that line.  Print  statements can be used to assist with finding bugs but remember to remove them when finished.  Debugging isn't just correcting errors, it is a scientific process of examing code to discover things you didn't expect in it.
HEAD: Debugging Strategies
DESC: 1. Examine error messages when programs crash.  The last line of Python Tracebacks will tell you what went wrong. Reading backwards from there will tell you more about where the problem occurred. 2. Work from example code.   If your modified code doesn't work, comment it out and do step-by-step modifications to the example code until it does what you want.   3. Make sure examples work.   Just because you find example code doesn't mean it will work in your system. Check the example code you're using to make sure it behaves the way you expect.   4. Check (print) intermediate results.  When your code doesn't crash, but doesn't behave as expected, add print statements to your program to see where in the code things stop behaving correctly.  5. Keep and compare old versions.  When you have a working version of your code, save it before you add to the code.  This will give you something to go back to if you introduce too many new bugs.
HEAD: Difference in List and Strings
DESC: The difference between  strings  and list is tha strings you are limited to sequence of characters where a  list  is a sequence of anything.  List are more powerful than strings, where in string all the elements had to be characters, in a list the elements can be anything like characters, strings, numbers, and other lists.  Ex list: p = ['y','a','b','b','a','!']  Ex list: p[2:4] = ['b','b'] (instead of returning a string it returns a list)
HEAD: Mutation
DESC: A  Mutation  is the ability to change the value of a list after it has been created.  So if you had the following list p = ['H','E','L','L','O'] you could replace the  H  with a  Y  by changing the first character using p[0] = 'Y'.  The [0] indicates what positon H is referenced.
HEAD: Aliasing
DESC: Aliasing  is when you have two different ways to refer to the same object.  The example given is like James Bond you have 2 ways of referring to that person.  You can refer to that person by his name James Bond or his code name 007.  The same idea applies where if you change either one it will change the other.
HEAD: Append
DESC: Append is a method that will add a new element to the end of a list.  Ex: &lt;list&gt;.append(&lt;element&gt;)
HEAD: Plus (+)
DESC: The plus is similar to concatenation in that it will combined two list together.
HEAD: Length
DESC: Length function will return the number of items in a list.  If you have levels of list within a list such as when you append a list to an existing list, the appended list will count as one position.  Ex: len(&lt;list&gt;)
Ex: len([0,1]) will return 2
Ex: len([0,1,[2,3]]) will return 3
HEAD: Append vs Plus
DESC: Append will keep the levels of the lists or in other words insert a list as a new position in an existing list.  While Plus will join the two list or add one list to another.
HEAD: For Loop
DESC: A simple way for python to loop through elements on a list is by using the function  For loop .  This will basically repeat a specific block of code for each element in a list.  Ex: for&lt;name&gt;in&lt;list&gt;: &lt;block&gt;
HEAD: Index
DESC: Index  is similar to .find.  If the value is in the list, returns the first position where the value is found in the list otherwise produces an error.   &lt;list&gt;.index(&lt;value&gt;)           
HEAD: In and Not In
DESC: In  Evaluates to true if it finds a variable in the specified sequence and false otherwise.   Not In  Evaluates to true if it does not find a variable in the specific sequence and false otherwise.  Ex: &lt;value&gt; in &lt;list&gt; Ex: &lt;value&gt; not in &lt;list&gt;"""





def generate_all_html(text):
    current_concept_number = 1
    notes = pull_concept_number(text, current_concept_number)
    all_html = ''
    while notes != '':
        head = pull_head(notes)
        desc = pull_desc(notes)
        concept_html = c_html(head, desc)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        notes =  pull_concept_number(text, current_concept_number)
    return all_html

print generate_all_html(text_html)

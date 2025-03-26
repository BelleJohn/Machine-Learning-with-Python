
# coding: utf-8

# <h3>A Brief Introduction to Python</h3>
# 
# Python is an interpreted high-level general-purpose programming language. Contrary to C-like languages, it uses the off-side rule: blocks in Python are expressed by their indentation. An increase in indentation comes after certain statements; a decrease in indentation signifies the end of the current block. Have a look at the following Python code block:

# <h1>Image Processing and Handling WS 2018/19</h1>
# 
# Exercise instructor: Marko Jovanović, mjovanovic@mi.rwth-aachen.de
# 
# <strong style="color: red">Notice: </strong>Attendance to <strong>all</strong> exercises sessions <strong>is mandatory</strong>. However, submitted exercise solutions aren't graded nor they present a prerequiste for the exam, but you will receive feedback on your submitted solutions.
# 
# The exercise sessions are held from 12.30-14.00 on the following dates at COMA 1:
# 
# <strong>22.10.2018 - OpenCV and Python intro (this session)</strong><br />
# 05.11.2018 - Image Enhancement<br />
# 19.11.2018 - Fourier Transform<br />
# 03.12.2018 - Visualization<br />
# 17.12.2018 - Automation<br />
# 14.01.2019 - Low-level Image Segmentation<br />
# 21.01.2019 - High-level Image Segmentation<br />
# 28.01.2019 - Solving a Problem<br />
# 
# The topics are an orientation and subject to change, in accordance with the lectures.
# 
# <h2>Exercise 1: Introduction to OpenCV and Python</h2>
# 
# Due date: <strong>29.10.2018</strong>
# 
# <h3>List of Tasks</h3>
# <ul>
#     <li><a href="#task1">Task 1 for Warming Up: Basic Image Manipulation</a></li>
#     <li><a href="#task2">Task 2: Basic Adjustments of Brightness and Contrast</a></li>
#     <li><a href="#task3">Task 3: Image Rotation</a></li>
# </ul>
# 
# In this course, you will get introduced to Python and OpenCV. Python is a popular interpreted programming language, which is designed with readability in mind and is relatively easy for beginners to grasp. OpenCV is a popular computer vision library, with bindings for C++, Python and Java.
# 
# You won't need anything else than this Jupyter notebook in order to write and execute your code. Code you write in the code cells here can be directly executed by selecting a cell and hitting the run button in the main menu. Do not hesitate to contact your course instructor, in case you are experiencing any technical difficulties with Jupyter Notebook.

# In[2]:


def is_even(a):
    if a % 2 == 0:
        print('Even!')
        return True
    print('Odd!')
    return False


# Python is meant to be an easily readable language. In the above example, the colons (:) are part of the Python langage syntax for readability and are obligatory (see http://effbot.org/pyfaq/why-are-colons-required-for-the-if-while-def-class-statements.htm ). On the other hand, semicolons (;) after statements are optional. 
# 
# Python does have a lot going for it in terms of simplicity. There is a rich set of modules associated with it. In many ways, it is "easier" to do things in Python, but you still have to seek out the libraries, learn what's available, and work through writing code to implement whatever problem you are trying to solve.
# 
# <h4>The Python Interpreter</h4>
# Python comes with an interactive interface, which allows you to evaluate statements on the fly. Python starts a prompt with '>>>'. To exit the Python interactive interface, press Ctrl-D.
# 
# To run a python script, simply type in your shell (for this, you need to open a shell on your computer with Python installed):
# <code>$ python filename.py</code>
# 
# <h4>Python Libraries You Will Need for the Exercises</h4>
# If you want to run your code on your own computer, here is a list of Python libraries you woud need to install additionally to installing Python:
# 
# <h5>NumPy</h5>
# NumPy is a scientific computing package for Python. It provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and a plethora of routines for fast operations on arrays: mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier Transforms, basic linear algebra, basic statistics, random simulation and many more. Thus it resembles a Matlab-ish way of thinking and operation.
# 
# At the core of the NumPy package is the <em>ndarray</em> object. This encapsulates n-dimensional arrays of homogeneous data types, with many operations being performed in compiled code for performance. There are some important differences to standard Python which you need to bear in mind when working with NumPy:
# <ul>
# <li>NumPy arrays have a fixed size at creation, unlike Python lists
# (which can grow dynamically). Changing the size of an <em class="xref py py-obj">ndarray</em> will
# create a new array and delete the original.</li>
# <li>The elements in a NumPy array are all required to be of the same
# data type, and thus will be the same size in memory.  The exception:
# one can have arrays of (Python, including NumPy) objects, thereby
# allowing for arrays of different sized elements.</li>
# <li>NumPy arrays facilitate advanced mathematical and other types of
# operations on large numbers of data.  Typically, such operations are
# executed more efficiently and with less code than it is possible using
# Python’s built-in sequences.</li>
# <li>A growing plethora of scientific and mathematical Python-based
# packages are using NumPy arrays; though these typically support
# Python-sequence input, they convert such input to NumPy arrays prior
# to processing, and they often output NumPy arrays.  In other words,
# in order to efficiently use much (perhaps even most) of today’s
# scientific/mathematical Python-based software, just knowing how to
# use Python’s built-in sequence types is insufficient - one also
# needs to know how to use NumPy arrays.</li>
# </ul>
# 
# <h5>matplotlib</h5>
# Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shells, the Jupyter notebook, web application servers, and four graphical user interface toolkits.
# 
# Matplotlib tries to make easy things easy and hard things possible. You can generate plots, histograms, power spectra, bar charts, errorcharts, scatterplots, etc., with just a few lines of code. For examples, see the <a href="https://matplotlib.org/tutorials/introductory/sample_plots.html" target="_blank">sample plots</a> and <a href="https://matplotlib.org/gallery/index.html" target="_blank">thumbnail gallery</a>.
# 
# <h5>OpenCV</h5>
# <a href="https://opencv.org" target="_blank">OpenCV</a> (Open Source Computer Vision Library) is a cross-platform image processing library which is free for both academic and commercial use under the open-source BSD license. OpenCV is written in C++ and its primary interface is in C++, but it still retains a C interface. However, there are also several bindings available: Python, Java, MATLAB/OCTAVE. Enabled with OpenCL, it can take advantage of the hardware acceleration of the underlying heterogeneous compute platform. Usage ranges from interactive art, to mines inspection, stitching maps on the web or through advanced robotics. We will make extensive use of some of OpenCV's capabilities throughout this exercise course.
# 
# <h4>Python Basics</h4>
# 
# In order to get started with writing your code in Python, we are giving you here a short introductory tutorial on Python syntax. However, this tutorial is very basic and we strongly encourage you though to look for further tutorials online.
# 
# Python has <strong>no mandatory statement termination characters</strong> and <strong>blocks are specified by indentation.</strong> 
# 
# <h5>A Fairly Easy, Self-Explanatory Code Sample</h5>

# In[ ]:


x = 34 - 23             # A comment.
y = "Hello"             # Another one.
z = 3.45
if z == 3.45 or y == "Hello":
  x = x + 1
  y = y + "World"       # String concat.
print(x)
print(y)


# To see the output of the above code example, first click on the above cell to select it and then click on the Run button in your Jupyter notebook's main menu. Note that the parentheses in print() are obligatory in Python 3, but in Python 2 they can be omitted.
# 
# Let's continue with the introduction of some basic operators:
# <ul>
#     <li>Assignment uses <code>=</code> and comparison uses <code>==</code></li>
#     <li>For numbers <code>+ - * / %</code> are as expected.</li>
#     <li>Special use of <code>+</code> for string concatenation.</li>
#     <li>Special use of <code>%</code> for string formatting (as with printf in C)</li>
#     <li>Logical operators are the words: <code>and, or, not</code> (not symbols)</li>
#     <li>The basic printing command is <code>print</code></li>
#     <li>The first assignment to a variable creates it.</li>
#     <li>Variable types don’t need to be declared.</li>
#     <li>Python figures out the variable types on its own (Python features a dynamic type system).</li>
# </ul>
# 
# <h5>Basic Datatypes</h5>
# <ul>
#     <li>Integers (which are default for numbers!)
#         <code>z = 5 / 2    # Answer is 2, integer division.</code>
#     </li>
#     <li>Floats
#         <code>x = 3.14159</code>
#     </li>
#     <li>Strings
#         Both single and double quotes are allowed to specify:
#         <code>"abc"</code> and <code>'abc'</code> represent the same string.
#         Unmatched quotes are allowed to occur in a string: <code>"OpenCV's great"</code>
#         Multiline strings or strings that containg both single and double quotes make use of triple double-quotes:
#         <code>"""a'b"c"""</code>
# </ul>

# In[ ]:


# Run this example to see the output of a
a = """a'b"c""
XYZ""";
print(a)


# <h5>Whitespace in Python</h5>
# 
# Unlike in C-like languages, whitespace has a special meaning in Python and needs to be used with care:
# <ul>
#     <li>Use a newline to end a line of code.
#         If you need to go to next line prematurely, end line with a <code>\</code>
#     </li>
#     <li>Python never uses braces <code>{ }</code> to mark blocks of code in Python. Instead, Python uses <em>consistent</em> indentation: The first line with <em>less</em> indentation is outside of the block. The first line with <em>more</em> indentation starts a nested block.
#     </li>
#     <li>Often, a colon appears at the start of a new block (e.g. for function and class definitions).</li>
# </ul>
# 
# <h5>Comments</h5>
# <ul>
#     <li>Start comments with a <code>#</code>. A comment started with a <code></code> ends at the end of the line</li>
#     <li>Can include a "documentation string" as the first line of any new function or class you define. The dev environment, debugger, and other tools use it: it's considered good style to include one.</li>
# </ul>

# In[4]:


def my_function(x, y):
  """This is the docstring. This 
  function does blah blah blah."""
  # The code would go here...


# <h5>Variable assignment</h5>
# 
# Binding a variable in Python means setting a <em>name</em> to hold a <em>reference</em> to some <em>object</em>. Assignments create references, not copies.

# In[ ]:


a = [1, 2, 3] # a now references the list [1, 2, 3]
b = a         # b now references what a references
a.append(4)   # this changes the list a references 
print(b)      # b is a reference to the same list


# Names in Python do not have an intrinsic type. Objects have types. Python determines the type of the reference automatically based on the data object assigned to it.
# 
# You create a name the first time it appears on the left side of an assignment expression: <pre>x = 3</pre>
# 
# A reference is deleted via garbage collection after any names bound to it have passed out of scope. Trying to access a name before it's been properly created (by placing it on the left side of an assignment), you'll get an error.

# In[5]:


nonexistingvar


# In[6]:


nonexistingvar = 3
nonexistingvar


# Assigning multiple names at the same time is a nice Python feature:

# In[7]:


x, y = 2, 3
print(x)
print(y)


# Names are case sensitive and cannot start with a number. They can contain letters, numbers and underscores:
# <code>mip Mip _mip _18_mip_ mip_18 MiP18</code>
# The following is a list of reserved words in Python:
# <code>and, assert, break, class, continue, def, del, elif, 
# else, except, exec, finally, for, from, global, if, 
# import, in, is, lambda, not, or, pass, print, raise, 
# return, try, while</code>
# 
# <h5>Sequence Types</h5>
# Python offers several sequence types:
# 
# <ul>
#     <li>
#         <strong>Tuples</strong><br />
#         A simple <em>immutable</em> ordered sequence of items. The items can be of mixes types, including collection types.
#     </li>
#     <li>
#         <strong>Strings</strong><br />
#         Immutable, and conceptually very similar to tuples.
#     </li>
#     <li>
#         <strong>List</strong><br />
#         <em>Mutable</em> ordered sequence of items of mixed types
#     </li>
# </ul>
# 
# All three sequence types (tuples, strings and lists) share much of the same syntax and functionality. The key difference is that tuples and strings are immutable whereas lists are mutable. Immutable types can't be cahnged. If you need to change an immutable type, you would need to make a fresh tuple and assign its reference to a previously used name.
# 
# Let's have a look on how to define each of the sequence types:

# In[8]:


# tuples are defined using parentheses:
tu = (23, 'abc', 4.56, (2,3), 'def')

# lists are defined using square brackets:
li = ["abc", 2.71, 42]

# strings are defined using quotes (", ', or """):
st1 = "Hello World"
st2 = 'Hello World'
st_multiline = """This is a multi-line
string that spans
three lines"""


# Access of elements of a tuple, list or string is <strong>zero-based</strong>:

# In[10]:


print(tu[1]) # second item in tuple
print(li[2]) # third item in list
print(st1[0]) # first character in the string


# Python, however, allows <strong>negative indices</strong> too! Negative indices count from right, starting with -1:

# In[11]:


print(tu[-1])


# You can also return copies of subsets. This operation is called <strong>slicing</strong> in Python:

# In[12]:


tu[1:4]


# Slicing supports <strong>negative indices</strong>, too:

# In[16]:


tu[1:-1]


# Note that slicing starts copying at the first index, and stops copying <em>before</em> the second index.
# 
# Omitting indices is also possible. Omit the first index to make a copy from the beginning of the container. Omit the last index to make a copy until the end of the container. Omit both to make a <em>copy</em> of the entire sequence.

# In[19]:


tu[:3]


# In[20]:


tu[-3:]


# In[18]:


tu[:]


# Unlike immutable tuples and strings, <strong>lists can be changed in place</strong>:

# In[21]:


li[1]
li.append('newelement')
li.insert(2, 653)
li


# Further, we have <code>append</code>, <code>extend</code> and the <code>+</code> operator. The <code>+</code> operator creates a new list, with a new memory reference, whereas <code>extend</code> operates in place:

# In[22]:


li.extend([77,88,99])
li


# In[23]:


li.append(['alfa','beta','gamma'])
li


# Note the difference: Whereas <code>extend</code> takes a list as an argument and appends every list item to the list to be extended, <code>append</code> takes a singleton as an argument, and adds the singleton as a single item to the original list.
# 
# Here are some further useful operations, which are self-explanatory:

# In[24]:


li = ['a','b','c','d']
li.index('b')


# In[25]:


li.count('b')


# In[26]:


li.remove('b')
li


# In[27]:


li.reverse()
li


# In[28]:


li.sort()
li


# Takeaway message: lists perform slower but are more powerful than tuples. Unlike tuples, lists can be modified. When needed, one can convert between tuples and lists using the <code>list()</code> and <code>tuple()</code> functions:
# <pre>
# li = list(tu)
# tu = tuple(li)
# </pre>
# 
# <h5>Functions</h5>
# 
# Functions are declared with the <code>def</code> keyword. Optional arguments are set in the function declaration after the mandatory arguments are being assigned a default value. For named arguments, the name of the argument is assigned a value. Functions can return a tuple (and using tuple unpacking you can effectively return multiple values).
# 
# Lambda functions are ad hoc functions that are comprised of a single statement. Parameters are passed by reference, but immutable types (tuples, ints, strings, etc) cannot be changed in the caller by the callee. This is because only the memory location of the item is passed, and binding another object to a variable discards the old one, so immutable types are replaced.
# 
# Have a look at the following code example:

# In[ ]:


# Same as def funcvar(x): return x + 1

funcvar = lambda x: x + 1
print(funcvar(1))
# 2

# an_int and a_string are optional, they have default values
# if one is not passed (2 and "A default string", respectively).

def passing_example(a_list, an_int=2, a_string="A default string"):
    a_list.append("A new item")
    an_int = 4
    return a_list, an_int, a_string

my_list = [1, 2, 3]
my_int = 10
print(passing_example(my_list, my_int))
# ([1, 2, 3, 'A new item'], 4, "A default string")
my_list
# [1, 2, 3, 'A new item']
my_int
# 10


# <h5>Classes</h5>
# 
# This introductory tutorial on Python does not cover the OOP paradigm.

# <h3>Example 1: Working with Images in OpenCV and Python</h3>
# Have a look at the following simple python script. It draws one red and one green bar on a white canvas by setting the color of individual pixels on the canvas. Remember that in Python in order to make use of OpenCV you need to include the opencv2 library, and both numpy and matplotlib for convenience and image plotting.

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Create image: it contains only white pixels
height, width = 400, 200
img = np.zeros((height,width,3), np.uint8)

# Output the image dimensions
print(len(img), len(img[0]), len(img[0][0]))

# Output empty image data as a multidimensional array of RGB pixels
print(img)

# Fill image with a red and a green bar
img[:, 0 : int(0.5 * width)] = (255,0,0)
img[:, int(0.5*width) : width] = (0,255,0)

plt.imshow(img)
plt.title('New Image: Half Red, Half Green'), plt.xticks([]), plt.yticks([]);


# <strong>Hint:</strong> Run the above code by selecting the above cell and clicking on the Run button on the main menu of Jupyter Notebook to see the output.

# You can run the above example by first clicking on its cell to select the cell, and then clicking on the Run button on Jupyter's main menu above.
# 
# The first line of code, <code>%matplotlib inline</code>, is a so-called <em>magic function</em> in the IPython shell, which is used by the Jupyter Notebook you are using right now. Without going into many details, we'll just say that with this backend, the output of plotting commands is displayed inline within frontends like the Jupyter notebook, directly below the code cell that produced it.
# 
# The import statements import necessary modules. We won't go at this point further into Python modules and importing, but we encourage you to have a look <a href="https://docs.python.org/2/tutorial/modules.html">here</a> if you are interested into more details about Python modules.
# 
# In general, when working with OpenCV, you could display an image with the following code block:
# 
# <code>cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# </code>
# 
# The above code block would display an image in a window. The window would automatically fit the window size.
# 
# However, we will be using a slightly different approach, in order to plot the images with matplotlib inline in Jupyter Notebook with 
# 
# <code>plt.imshow(img)</code>
# 
# For more information on pyplot and some useful examples refer to https://matplotlib.org/users/pyplot_tutorial.html

# <h3>Example 2: Reading and Outputting an Image</h3>
# 
# The following code sample shows how to read in an image and display it using matplotlib. Please note that it may take a couple of seconds for the server to render the image and send it back to your browser.

# In[ ]:


# The matplotlib magic function and library imports
get_ipython().run_line_magic('matplotlib', 'inline')
import cv2
import matplotlib.image as mpimg
import numpy as np
from matplotlib import pyplot as plt

# Read in castle.jpg. The file is located in your Notebook's folder for this exercise session.
img = mpimg.imread('castle.jpg')

# Use the following line of code to set the image output size. The numbers represent the image's width and height
# in inches. The original aspect ratio is nevertheless preserved and actual output size is adjusted automatically.
plt.rcParams["figure.figsize"] = (20,15)

# Output the image
plt.imshow(img)


# <a name="task1"></a><h3 style="color: red">Task 1 for Warming Up: Basic Image Manipulation</h3>
# 
# First, read the following tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html
# 
# <strong style="color: red">Programming Task:</strong> Write a program which crops and flips horizontally the image, and outputs both images. Browse online for more tutorials on how to achieve that, if you are unsure.

# In[ ]:


# The matplotlib magic function and library imports
get_ipython().run_line_magic('matplotlib', 'inline')
import cv2
import matplotlib.image as mpimg
import numpy as np
from matplotlib import pyplot as plt

img = mpimg.imread('castle.jpg')
plt.rcParams["figure.figsize"] = (20,15)

# Start typing your code here.

# img_cropped = ...
# img_flipped = ...

# End of your code

# Output the original image, and its cropped and flipped variants
plt.imshow(img)
plt.imshow(img_cropped)
plt.imshow(img_flipped)


# <a name="task2"></a><h3 style="color: red">Task 2: Basic Adjustments of Brightness and Contrast</h3>
# 
# Brightness is an attribute of visual perception in which a source appears to be radiating or reflecting light. Contrast is the difference in brightness between objects or regions, that makes the objects distinguishable in the image. For example, a white rabbit running across a snowy field has poor contrast, while a black dog against the same white background has good contrast. 
# 
# <strong style="color: red">Programming Task:</strong> Write a program which adjusts the images brightness and contrast. Find suitable parameters for the adjustment. Look up online the necessary functions. Note that there are several possible ways to achieve brightness and contrast adjustment.

# In[ ]:


# The matplotlib magic function and library imports
get_ipython().run_line_magic('matplotlib', 'inline')
import cv2
import matplotlib.image as mpimg
import numpy as np
from matplotlib import pyplot as plt

img = mpimg.imread('mammogram1.png')
plt.rcParams["figure.figsize"] = (20,15)

# Start typing your code here.

# img_brightness = ...
# img_contrast = ...

# End of your code

# Output the original and brightness- and contrast-adjusted images
plt.imshow(img)
plt.imshow(img_brightness)
plt.imshow(img_contrast)


# <a name="task3"></a><h3 style="color: red">Task 3: Image Rotation</h3>
# 
# The image you have just loaded and rendered appears to have been rotated counter-clockwise by 90 degrees. As a warm-up task, you should write a python script which rotates the image back clockwise by 90 degrees.
# 
# Rotation is a type of a linear geometric transform. In two dimensions, linear geometric transforms can be represented by a 2x2 matrix.
# 
# Rotation can be represented by the following matrix: 
# 
# $
# M =
#   \begin{bmatrix}
#     \cos\theta & -\sin\theta\\
#     \sin\theta & \cos\theta
#   \end{bmatrix}
# $
# 
# where the center of rotation lies in the image center coordinates (width/2, height/2).
# 
# However, OpenCV provides scaled rotation with adjustable center of rotation so that you can rotate your image at any location you prefer. Thus, we have a modified transformation matrix given by:
# 
# $
# M = 
# \begin{bmatrix}
#     \alpha & \beta & (1-\alpha)center_x - \beta center_y\\
#     -\beta & \alpha & \beta center_x+(1-\alpha)center_u
#   \end{bmatrix}
# $
# 
# where
# 
# $\alpha = scale \cos\theta$,
# 
# $\beta = scale \sin\theta$
# 
# To find this transformation matrix, OpenCV provides a function <code>cv2.getRotationMatrix2D</code>.
# 
# <strong style="color: red">Programming Task:</strong><br />Look up online which parameters the function does accept and how to apply the obtained rotation matrix in order to have the castle image rotated by 90 degrees.
# 
# What happens if you rotate the image by angles other than multiples of 90 degrees? Is there any loss in the transformed image? If so, try to come up with a solution which preserves the whole image when rotating images by values other than multiples of 90 degrees.
# 
# For the sake of convenience, we have already written the necessary library import statements and statements for image output for you.

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
import cv2
import matplotlib.image as mpimg
import numpy as np
from matplotlib import pyplot as plt

img = mpimg.imread('castle.jpg')
rows, cols, depth = img.shape

# Start typing your code here

# End of your code

plt.rcParams["figure.figsize"] = (15, 20)
imgplotst = plt.imshow(dst)


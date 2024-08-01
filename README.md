# matplot

What is the Matplotlib package and how to install it. Dependencies that are installed together with this package. 
Which backends are used and how to set them using the use() function. 
The main components of the graph are: Figure, Axes, Legend, Grid, Artist.

1.The first introduction to the pyplot module.

2.Plot Function.
   How to use the plot() function to display one or more two-dimensional graphs in coordinate axes. 
   It talks about ways to change the styles and colors of lines in graphs (including through the setp() function),
   and about changing the markers of graph points.  
   The main named parameters of the setp() and plot() functions are given.
   You will learn about the work of the fill_between() function for filling areas of the graph.

3.Multiple graphs (coordinate axes)
   How to display multiple graphs (coordinate axes) on one figure.
   The functions subplot() and subplots() are considered.
   A way to create an additional window using the figure() function and place coordinate axes in it 
   (methods: add_axes() and add_subplot()). Learn about the GridSpec class
   for convenient layout of coordinate axes spanning multiple cells

4.Axes limits
    Set boundaries (limits) when displaying graphs along axes using the functions and methods: 
    set(), set_xlim(), set_ylim(), xlim() and ylim().
    We control the position of labels on coordinate axes using the methods: set_major_locator() and set_minor_locator(),
    using the following classes of locators: Nullocator, LinearLocator, MultipleLocator, IndexLocator,
    FixedLocator, LogLocator, MaxNLocator

5.Displaying labels format
  Displaying labels  axes format using the set_xticklabels(), set_yticklabels() methods,
  as well as the following formatters: NullFormatter, FormatStrFormatter, FuncFormatter, FixedFormatter.
  The set_major_formatter() method for assigning a coordinate axis formatter.


6.Axes coord log scale
  display graphs on a logarithmic scale. Get acquainted with the semilogx() and semilogy() functions,
  the set_xscale() and set_yscale() methods and their parameters: 'linear', 'log', 'symlog', 
  as well as named parameters: base, subs, linthresh, linscale. The loglog() function

7.Standard text elements
  The methods are considered: grid(), figtext(), suptitle(), set_xlabel(), set_ylabel(), xlabel(), ylabel(), text(),
  annotate(). Properties for the design of text elements: alpha, backgroundcolor, color, fontsize, fontweight, position,
  visible and others. For more information about them, see the documentation.





















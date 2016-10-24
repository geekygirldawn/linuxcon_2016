# Linux Kernel Examples for Gource

By: [Dawn M. Foster](http://fastwonderblog.com). 
PhD student at the [University of Greenwich, Centre for Business Network Analysis](http://www2.gre.ac.uk/about/faculty/business/research/centres/cbna/home) 
and [open source / community building consultant](http://fastwonderblog.com/consulting/) 
at [The Scale Factory](http://www.scalefactory.com/).


### Linuxing in London

* [Meetup Details](https://www.meetup.com/Linuxing-In-London/events/234931498/) - 25 October 18:15
* [Presentation Slides - coming soon]()

**NOTE: See the [README.md file](https://github.com/geekygirldawn/linuxcon_2016)
in the main repo for more details and other examples.**
This README.md contains only a small number of details.

Linux Kernel Stable Tree Code Repo
----------------------------------

Caveat: The kernel source code trees are enormous and Gource has to parse the git log before it
can visualize the data. By limiting the log to one month, it can parse the data quickly enough for
me to demo it :)

Too much info - even limited to one month!

    $ gource --start-date '2015-01-01' --stop-date '2015-01-31'

Maybe you only want some of the information. You can use regular expressions (regex) to exclude some information.
For example, you can exclude the ".c" and ".h" files:

    $ gource --start-date '2015-01-01' --stop-date '2015-01-31' --file-filter '\.(c|h)'

Gource only lets you exclude files, but you can abuse regex a bit to match anything except a string, and then
with the double negative of excluding via --file-filter, you can get all of the commits related to sound:

    $ gource --start-date '2015-01-01' --stop-date '2015-01-31' --file-filter '^((?!sound).)*$' -s 30

Now you can make it look a bit nice by slowing things down, adding a date format, increasing the font size,
changing the font color, and adding title and logo.

    $ gource --start-date '2015-01-01' --stop-date '2015-01-31' --file-filter '^((?!sound).)*$' -s 30 --date-format "%A, %d %B %Y" --font-size 22 --font-colour FF9900 --logo ~/gitrepos/linuxcon_2016/kernel_example/images/tux.png --title "Linux Kernel Stable Tree"




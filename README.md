# LinuxCon: Visualize Your Code Repos and More with Gource

**NOTE: This is work in progress as I prepare for my talks.
Right now, this repo is a mess as I pull things together from other talks
and add new material.**

By: [Dawn M. Foster](http://fastwonderblog.com). 
PhD student at the [University of Greenwich, Centre for Business Network Analysis](http://www2.gre.ac.uk/about/faculty/business/research/centres/cbna/home) 
and consultant at [The Scale Factory](http://www.scalefactory.com/)


### LinuxCon North America - Toronto 2016

* [Session Info and Abstract](http://sched.co/7JWe)
* Presentation Slides - coming soon
* When: Tuesday, August 23. 2:10pm - 3:00pm
* Room: Marine

### LinuxCon Europe - Berlin 2016

* [Session Info and Abstract](http://sched.co/7o95)
* Presentation Slides - coming soon
* When: Thursday, October 6. 11:15am - 12:05pm
* Room: Potsdam III

Additional Info
---------------

My slides will be available on [slideshare](http://www.slideshare.net/geekygirldawn)
shortly after the presentations.

This github repo contains all of the scripts, data, instructions, and other 
technical materials that you can use to reproduce what I did in the sessions.
If I do this well, you'll be able to use these tools to gather data and 
perform similar analysis using your own community data. 

This README file is where you can find most of the instructions for replicating the
data and analysis from the presentations along with some extra material.

Using Gource
-------

[Gource](http://gource.io/) is a visualization tool most often used to
visualize source code repositories.

###Examples

If you aren’t already familiar with Gource, here are a few interesting videos of how 
other people have used Gource to get you thinking about how you might use it!

* [Tribute to Seth Vidal](https://www.youtube.com/watch?v=OARZB0jGziQ), lead developer of the Yum project and long time Fedora contributor, shortly after he was killed by a hit-and-run driver while riding his bike. Seth’s contributions to Yum are in blue, while contributions from others are in white.
* [Linux Kernel Development](https://www.youtube.com/watch?v=5iFnzr73XXk), 1991-2015. Visualize the full development history of any open source project, the Linux kernel in this example.
* [Population Dynamics](https://www.youtube.com/watch?v=yh9IW9dXFQw) 1970-2010. A visualization of population dynamics.

###Useful Gource Info

* [Gource website](http://gource.io/) for downloads and general info.
* [Gource github repo](https://github.com/acaudwell/Gource)
* [Gource wiki](https://github.com/acaudwell/Gource/wiki) for documentation, how-to, and videos
* [Control page](https://github.com/acaudwell/Gource/wiki/Controls) for a list of all of the 
controls you can use to speed up / slow down or show / hide to get something that 
looks good with your data. 
* [Templates](https://github.com/FOSSRIT/gourciferous/tree/develop/Templates) with recommended 
configurations for different types of data (large projects, long-lived projects, etc.)
* [Gourciferous](https://github.com/FOSSRIT/gourciferous) for visualizing multiple
repos in a single visualization using the custom log format.

Code Repositories
-----------------

If you've never run Gource on your code repositories, you should!

It's easy to run:

    $ gource </path/to/repo> 

However, repos vary dramatically in size, activity, etc., so the default options probably
won't be ideal. 

###Make it look great

There are a number of options you can use to make your Gource visualization look better.
Here are a few that you probably want to use most of the time.

**Date Format**

You may want to look at the 
[strftime manual](http://pubs.opengroup.org/onlinepubs/007908799/xsh/strftime.html) 
for valid format strings.

Display only the Month (name) and Year for busy repositories.

    --date-format "%B %Y"

Display the date without minutes / seconds.

    --date-format "%A, %d %B %Y"

**Title**

    --title "My Awesome Project"

**Font for Date and Title**

    --font-size 22 --font-colour FF9900

**Logo**

    --logo images/bitergia-logo.png

You can also get a little creative with the logo option to create a banner image
to give you more control over the title or anything else you want to display at 
the bottom of the screen.

    --logo images/bitergia-banner.png

**Other Options not in this example**

Here are a few other options that I'm not using here, but might be useful for you,
and other options for changing the appearance can be found on the 
[wiki](https://github.com/acaudwell/Gource/wiki/Controls) or by using gource -H

Background color (hex value)

    gource --background 555555 

Background image

    gource --background-image background.png

**Examples: Make it look great**

Using Logo and Title:

    gource -a 1 -s .3 --date-format "%A, %d %B %Y" --font-size 22 --font-colour FF9900 
    --title "MailingListStats aka mlstats" --logo ~/gitrepos/linuxcon_2016/images/bitergia-logo.png 
    ~/gitrepos/MailingListStats/

Using banner image logo to replace title

    gource -a 1 -s .3 --date-format "%A, %d %B %Y" --font-size 22 --font-colour FF9900 
    --logo ~/gitrepos/linuxcon_2016/images/bitergia-banner.png ~/gitrepos/MailingListStats/


###Display Additional Information

**Key**

Add a file extension key to show which colors are used for each file extension. You 
can also toggle this on or off by typing the "K" key while gource is running. 

    --key

**Captions**

These are great for narrating important milestones or other activities in the project:
release dates, people joining the project, major refactoring, etc.

First, you need a pipe separated file with unix timestamp|description (one per line):

    1373850061|Kris begins work on the website
    1375750861|Dawn fixes some typos
    1379120461|Richard makes everything look nice

Tell gource where to find the file:

    --caption-file linuxcon_2016/data/captions.log

Specify the duration of the caption display in seconds (default is 10 seconds):

    --caption-duration 4

Hex value for the caption font color:

    --caption-colour FF9900

Font size for caption:

    --caption-size 20

**Example: Captions**

    gource -a 1 -s .3 --key --caption-file ~/gitrepos/linuxcon_2016/data/captions.log 
    --caption-duration 4 --caption-colour FF9900 --caption-size 20 ~/gitrepos/cfgmgmtcamp.github.io/

**ADD STUFF HERE**

**ADD CAPTION FILES: https://github.com/acaudwell/Gource/wiki/Captions**

Data Gathering to use the Gource Custom Log Format
--------------------------------------------------

More details about Using the Gource [custom log format](https://github.com/acaudwell/Gource/wiki/Custom-Log-Format)
option.

If you are gathing data from open source communities, your best friend is
the [MetricsGrimoire](https://github.com/MetricsGrimoire) suite of tools. This presentation
uses [mlstats](https://github.com/MetricsGrimoire/MailingListStats) for mailing lists
and [bicho](https://metricsgrimoire.github.io/Bicho/) for bug data.

Mailing Lists
-------------

###Step 1: Get your mailing list data into a database using mlstats.

a) Install [mlstats](https://github.com/MetricsGrimoire/MailingListStats)

    $ python setup.py install

b) Log into mysql and create the database

    mysql> create database mlstats;

c) Import your mailing list data by running mlstats

    $ mlstats --db-user=USERNAME --db-password=PASS http://URLOFYOURLIST

Note: this can take a long time depending on how long your mailing list 
has been around and the number of messages.

###Step 2: Run database queries to extract your data

This is the "do it yourself" method and requires a bit manual / scripting work on your part. See Step 2 (alternative) below for a Python script that does this for you.

A good list of starter queries can be found on the 
[mlstats wiki](https://github.com/MetricsGrimoire/MailingListStats/wiki/Queries) and
you'll want to look at the [database schema](https://github.com/MetricsGrimoire/MailingListStats/wiki/Database-Schema) as well

To get the data for the Gource custom log, you would need something like this,
but you would need to re-format it into a pipe-separated file that Gource can read 
(see Python script alternative below):

    SELECT unix_timestamp(DATE_ADD(m.first_date, interval m.first_date_tz second)) 
    AS unix_date, mp.email_address AS sender, (SELECT mp2.email_address FROM 
    messages m2, messages_people mp2 WHERE m2.is_response_of=m.is_response_of AND 
    mp2.message_id=m2.is_response_of limit 1) AS receiver FROM messages_people mp, 
    messages m WHERE YEAR(m.first_date)=2015 AND MONTH(m.first_date)=1 AND 
    mp.message_id=m.message_id; 

###Step 2 (alternative): Use a Python script to easily run the database query and re-format the data a bit.

Run linuxcon.py:

    $ python linuxcon.py -o <outputfiledir> -d <database> 

What linuxcon.py does:

* Gathers information about where to put output files and the database being used. 
(Note: assumes you have a my.cnf file to authenticate to the database.)
* Runs the query.
* Strips the email down to the username (everything before @example.com) to have a 
shorter identifier for the users.
* Formats the output into a nice Gource custom log format sorted by time
as gource_output.log

CAVEAT: I am not a real programmer; the code is ugly; and it may or may not work for 
you without some tweaking. However, I will be doing more Python programming, and I 
appreciate **helpful** suggestions about how to improve :)

###Gource - Mailing List Options

I also added a few other options to make it look a bit nicer:

Time files remain idle (default 0). This allows people being replied to
       to disappear after 10 seconds to clean up a bit and make it more readable.

* -i : Time files remain idle (default 0). This allows people being replied to 
       to disappear after 10 seconds to clean up a bit and make it more readable.
* --max-user-speed : Speed users can travel per second (default: 500). I slowed 
       this down to 100 to make it easier to see the users.
* -a 1 : Auto skip to next entry if nothing happens for a number of seconds (default: 3)
         sped this up a bit.
* --highlight-users : keeps the usernames for the people sending emails from
                      disappearing. I would have liked to have the same for filenames
                      which are the people being replied to, but can't seem to find
                      at option for that
* -s 30 : seconds per day. Not used here, but when you run these yourself, you might
          want to slow things down a bit so you can better see what's going on.

    $ gource -i 5 --max-user-speed 100 -a 1 --highlight-users gource_output.log

Bug Data
--------

There are (at least) two options for getting your bug data:

1. Query your bug database directly. This is probably the quickest and easiest option,
but it assumes that you have access to submit queries directly against your bug database.
The [Gource Wiki](https://github.com/acaudwell/Gource/wiki/Custom-Log-Format) has an example 
of a query that you can use for Bugzilla. Unfortunately, most of us don't have this access, 
so we are left with option 2.
2. Use [Bicho](https://metricsgrimoire.github.io/Bicho/) to download bug data into a 
database that you can query. The rest of this section assumes that you are using Bicho.

###Step 1: Get your bug data into a database using Bicho

a) Install [Bicho](https://metricsgrimoire.github.io/Bicho/)

Note: See instructions at the link above for dependencies you might need to install first.

    $ python setup.py install

b) Log into mysql and create the database 

    $ mysql> create database bicho;

c) Import your bug data by running Bicho (**see instructions at link above - varies by bug tracker**)

    $ bicho --db-user-out=[USER] --db-password-out=[PASS] --db-database-out=bicho -d 15 -b jira -u [URL]

Note: this can take a long time depending on how long your mailing list 
has been around and the number of messages.

###Step 2: Run database queries to extract your data

These database queries are for a Bicho database; however, if you have direct access to your bug database, 
it might be easier to run queries on your bug database directly as mentioned above. 
 
Notes:

* These are queries for JIRA, since it's what I had handy, but others would be very similar.
* issues_ext_jira.issue_key AS bug is only for debugging purposes, since it's a handy way to double check the data.

New Issues (A)

    SELECT unix_timestamp(issues.submitted_on) AS unix_date, 
    issues.submitted_by AS submitter_id, 
    (SELECT people.user_id FROM people, issues WHERE people.id = submitter_id limit 1) AS submitter, 
    issues.id AS id,
    issues_ext_jira.component AS path,
    issues_ext_jira.issue_key AS bug
    FROM issues, issues_ext_jira
    WHERE issues.id = issues_ext_jira.issue_id
    ORDER BY unix_date;

Modified Issues (M) - non-comment changes

    SELECT unix_timestamp(changes.changed_on) AS unix_date, 
    changes.changed_by AS submitter_id, 
    (SELECT people.user_id FROM people, changes WHERE people.id = submitter_id limit 1) AS submitter, 
    changes.issue_id AS id,
    issues_ext_jira.component AS path,
    issues_ext_jira.issue_key AS bug
    FROM changes, issues_ext_jira
    WHERE changes.issue_id = issues_ext_jira.issue_id
    ORDER BY unix_date;

Modified Issues (M) - comments

    SELECT unix_timestamp(comments.submitted_on) AS unix_date, 
    comments.submitted_by AS submitter_id, 
    (SELECT people.user_id FROM people, changes WHERE people.id = submitter_id limit 1) AS submitter, 
    comments.issue_id AS id,
    issues_ext_jira.component AS path,
    issues_ext_jira.issue_key AS bug
    FROM comments, issues_ext_jira
    WHERE comments.issue_id = issues_ext_jira.issue_id
    ORDER BY unix_date;


Data and Examples
-----------------

###Mailing List Data

The data used in the examples comes from the Linux kernel 
[IOMMU list](http://lists.linuxfoundation.org/pipermail/iommu/) for January 2015.
[IOMMU](https://en.wikipedia.org/wiki/IOMMU) (Input/Output Memory Management Unit) is used in 
the Linux kernel to map the virtual memory accessible by devices to physical memory for security
and other reasons. I selected this list for a few reasons:

* I'm studying the Linux kernel community at the University of Greenwich, so I wanted to pick something 
from the Linux kernel, but there are [over 150 mailing lists](http://vger.kernel.org/vger-lists.html)
documented for the Linux kernel (and not all of them are listed at that link).  
* The IOMMU list is lower volume than many of the kernel lists (651 posts for January), so it's more
manageable as an example.
* It is a mailman list, which has nicely formatted, clean logs that import well using mlstats.
Many of the kernel lists have other ways of logging (Gmane, etc.) that aren't quite as clean
when imported. 

###Bug Data

The bug data is courtesy of [Dr. Guido Conaldi](http://www.gre.ac.uk/business/study/ibe/staff/guido-conaldi), Senior Lecturer at The University of Greenwich. This dataset came from one of his research projects using network analysis on bug tracker data.

ADD DETAILS HERE.

License and Copyright
---------------------

Code is licensed under [GNU General Public License (GPL), version 3 or later](http://www.gnu.org/licenses/gpl.txt).

Other content, including the tutorial materials in this README and data files are licensed under a 
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

Copyright (C) 2016 Dawn M. Foster


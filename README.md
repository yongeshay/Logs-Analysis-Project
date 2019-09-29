---


---

<h1 id="project-overview">Project Overview</h1>
<blockquote>
<p>You’ve been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You’ve been asked to build an <strong>internal reporting tool</strong>  that will use information from the database to discover what kind of articles the site’s readers like.</p>
<p>The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site’s user activity.</p>
<p>The program you write in this project will run from the command line. It won’t take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.</p>
</blockquote>
<h2 id="why-this-project">Why this project?</h2>
<p>In this project, I stretch your SQL database skills. I practice interacting with a live database both from the command line and from my code. I explore a large database with over a million rows. And I build and refine complex queries and use them to draw business conclusions from data.</p>
<h1 id="so-what-are-we-reporting-anyway">So what are we reporting, anyway?</h1>
<p>Here are the questions the reporting tool should answer. The example answers given aren’t the right ones, though!</p>
<p><strong>1. What are the most popular three articles of all time?</strong>  Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.</p>
<p><strong>Example:</strong></p>
<ul>
<li>“Princess Shellfish Marries Prince Handsome” — 1201 views</li>
<li>“Baltimore Ravens Defeat Rhode Island Shoggoths” — 915 views</li>
<li>“Political Scandal Ends In Political Scandal” — 553 views</li>
</ul>
<p><strong>2. Who are the most popular article authors of all time?</strong>  That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.</p>
<p><strong>Example:</strong></p>
<ul>
<li>Ursula La Multa — 2304 views</li>
<li>Rudolf von Treppenwitz — 1985 views</li>
<li>Markoff Chaney — 1723 views</li>
<li>Anonymous Contributor — 1023 views</li>
</ul>
<p><strong>3. On which days did more than 1% of requests lead to errors?</strong>  The log table includes a column status that indicates the HTTP status code that the news site sent to the user’s browser. (Refer to  <a href="https://classroom.udacity.com/courses/ud303/lessons/6ff26dd7-51d6-49b3-9f90-41377bff4564/concepts/75becdb9-da2a-4fbf-9a30-5f3ccd1aa1d6">this lesson</a>  for more information about the idea of HTTP status codes.)</p>
<p><strong>Example:</strong></p>
<ul>
<li>July 29, 2016 — 2.5% errors</li>
</ul>
<h1 id="prepare-the-software-and-data">Prepare the software and data</h1>
<p>To start on this project, you’ll need database software (provided by a Linux virtual machine) and the data to analyze.</p>
<h2 id="the-virtual-machine">The virtual machine</h2>
<p>This project makes use of a Linux-based virtual machine (VM).</p>
<p>If you don’t already have Vagrant and VirtualBox installed, please install them now.</p>
<p>This will give you the PostgreSQL database and support software needed for this project. If you have used an older version of this VM, you may need to install it into a new directory.</p>
<p>If you need to bring the virtual machine back online (with  <code>vagrant up</code>), do so now. Then log into it with  <code>vagrant ssh</code>.</p>
<p><a href="https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/bc938915-0f7e-4550-a48f-82241ab649e3/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91#"></a></p>
<p><img src="https://video.udacity-data.com/topher/2017/April/58fa90dd_screen-shot-2017-04-21-at-16.06.30/screen-shot-2017-04-21-at-16.06.30.png" alt="A terminal in which we've successfully logged into the virtual machine using &quot;vagrant ssh&quot;."></p>
<p><em>Successfully logged into the virtual machine.</em></p>
<h2 id="download-the-data">Download the data</h2>
<p>Next,  <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">download the data here.</a>  You will need to unzip this file after downloading it. The file inside is called  <code>newsdata.sql</code>. Put this file into the  <code>vagrant</code>  directory, which is shared with your virtual machine.</p>
<p>To build the reporting tool, you’ll need to load the site’s data into your local database. Review how to use the  <code>psql</code>  command in this lesson:  <a href="https://classroom.udacity.com/nanodegrees/nd004-ent/parts/72d6fe39-3e47-45b4-ac52-9300b146094f/modules/0f94ae26-c39d-4231-924b-b1eb6e06cf41/lessons/96869cfc-c67e-4a6c-9df2-9f93267b7be5/concepts/0b4079f5-6e64-4dd8-aee9-5c3a0db39840?contentVersion=1.0.0&amp;contentLocale=en-us">(FSND version)</a></p>
<p>To load the data,  <code>cd</code>  into the  <code>vagrant</code>  directory and use the command  <code>psql -d news -f newsdata.sql</code>.<br>
Here’s what this command does:</p>
<ul>
<li><code>psql</code>  — the PostgreSQL command line program</li>
<li><code>-d news</code>  — connect to the database named news which has been set up for you</li>
<li><code>-f newsdata.sql</code>  — run the SQL statements in the file newsdata.sql</li>
</ul>
<p>Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.</p>
<h2 id="getting-an-error">Getting an error?</h2>
<p>If this command gives an error message, such as —<br>
<code>psql: FATAL: database "news" does not exist</code><br>
<code>psql: could not connect to server: Connection refused</code><br>
— this means the database server is not running or is not set up correctly. This can happen if you have an  <em>older version</em>  of the VM configuration from before this project was added. To continue,  <a href="https://classroom.udacity.com/nanodegrees/nd004-ent/parts/72d6fe39-3e47-45b4-ac52-9300b146094f/modules/0f94ae26-c39d-4231-924b-b1eb6e06cf41/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0">download the virtual machine configuration</a>  into a fresh new directory and start it from there.</p>
<h2 id="explore-the-data">Explore the data</h2>
<p>Once you have the data loaded into your database, connect to your database using  <code>psql -d news</code>  and explore the tables using the  <code>\dt</code>  and  <code>\d table</code>  commands and  <code>select</code>  statements.</p>
<ul>
<li><code>\dt</code>  — display tables — lists the tables that are available in the database.</li>
<li><code>\d table</code>  — (replace  <em>table</em>  with the name of a table) — shows the database schema for that particular table.</li>
</ul>
<p>Get a sense for what sort of information is in each column of these tables.</p>
<p>The database includes three tables:</p>
<ul>
<li>The  <code>authors</code>  table includes information about the authors of articles.</li>
<li>The  <code>articles</code>  table includes the articles themselves.</li>
<li>The  <code>log</code>  table includes one entry for each time a user has accessed the site.</li>
</ul>
<h1 id="how-to-run-this-project">How To Run This Project</h1>
<p>Here’s what you should do:</p>
<ol>
<li>Follow all of the steps listed above regarding installing your Virtual Machine and dowloading the Database</li>
<li>Clone this GitHub repo</li>
<li>Unzip and place this application locally in your FSND-Virtual-Machine folder</li>
<li>Run this application within the VM <code>python newsdata1.py</code></li>
</ol>


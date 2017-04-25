<html><body><p>One of the most tedious tasks of working with databases is to write and maintain documentation, in particular writing reports from tables and views.

So why not try to make this task a bit less heavy by using Python?
</p><h6>Step0-The input and the output</h6>
The script requires that the views are created using create view.
Example:
<h5>Right click on view</h5>
<img class="alignnone  wp-image-107" src="/2017/02/img1.png" alt="img1" width="477" height="298">
<h5>Copy view</h5>
<img class="alignnone size-full wp-image-110" src="/2017/02/img2.png" alt="img2" width="440" height="237">
<h5>Output view after python script</h5>
<img class="alignnone size-full wp-image-121" src="/2017/02/img3.png" alt="img3" width="424" height="224">

<hr>

<h6>Step1 - Extract Columns Function</h6>
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#66d9ef;">def</span> <span style="color:#a6e22e;">extract_columns</span><span style="color:#f8f8f2;">(in_txt):</span>
    <span style="color:#e6db74;">"""Simple function to extract columns between select and from"""</span>
    <span style="color:#75715e;"># Splitting by select i only choose text after select</span>
    <span style="color:#f8f8f2;">out_view</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">re</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">split(</span><span style="color:#e6db74;">r'(?i)\bselect\b'</span><span style="color:#f8f8f2;">,in_txt)[</span><span style="color:#ae81ff;">1</span><span style="color:#f8f8f2;">]</span>
    <span style="color:#75715e;"># Splitting by from i only choose text before from</span>
    <span style="color:#f8f8f2;">out_view</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">re</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">split(</span><span style="color:#e6db74;">r'(?i)\bfrom\b'</span><span style="color:#f8f8f2;">,out_view)[</span><span style="color:#ae81ff;">0</span><span style="color:#f8f8f2;">]</span>
    <span style="color:#75715e;"># Cleaning extra spaces and tabs</span>
    <span style="color:#f8f8f2;">out_view</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">strip()</span>
    <span style="color:#66d9ef;">return</span> <span style="color:#f8f8f2;">out_view</span>
</pre>
Let's start by defining a function with the purpose of extracting only the columns from the script of a view. Thus ignoring everything before the Select statement and everything after the From statement.

<hr>

<h6>Step2 -Let's start from the variables</h6>
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#f92672;">import</span> <span style="color:#f8f8f2;">re</span>

<span style="color:#75715e;"># We open the file containing the view</span>
<span style="color:#f8f8f2;">view</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">extract_columns(open(</span><span style="color:#e6db74;">'input.txt'</span><span style="color:#f8f8f2;">,</span><span style="color:#e6db74;">'r'</span><span style="color:#f8f8f2;">,encoding</span><span style="color:#f92672;">=</span><span style="color:#e6db74;">'utf-8'</span><span style="color:#f8f8f2;">)</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">read())</span>
<span style="color:#75715e;"># Now we insert text into the list and we create a new list</span>
<span style="color:#f8f8f2;">view_l</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">view</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">split(</span><span style="color:#e6db74;">'</span><span style="color:#ae81ff;">\n</span><span style="color:#e6db74;">'</span><span style="color:#f8f8f2;">)</span>
<span style="color:#f8f8f2;">out_l</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">[]</span>
</pre>
Now we declare the variables we are going to use.
<ul>
	<li>view: contains the input text</li>
	<li>view_l: is a list created by splitting text by line</li>
	<li>out_l: is the output list</li>
</ul>

<hr>

<h6>Step3-Main Code</h6>
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#75715e;"># Now we loop through all the lines of the view</span>
<span style="color:#66d9ef;">for</span> <span style="color:#f8f8f2;">num,line</span> <span style="color:#f92672;">in</span> <span style="color:#f8f8f2;">enumerate(view_l):</span>
    <span style="color:#75715e;"># Clean extra spaces</span>
    <span style="color:#f8f8f2;">line</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">line</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">strip()</span>
    <span style="color:#75715e;"># Remove Comments</span>
    <span style="color:#f8f8f2;">line</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">line</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">split(</span><span style="color:#e6db74;">'--'</span><span style="color:#f8f8f2;">)[</span><span style="color:#ae81ff;">0</span><span style="color:#f8f8f2;">]</span>
    <span style="color:#75715e;"># Remove Commas</span>
    <span style="color:#f8f8f2;">line</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">line</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">replace(</span><span style="color:#e6db74;">','</span><span style="color:#f8f8f2;">,</span><span style="color:#e6db74;">''<span style="color:#ffffff;">,</span>1</span><span style="color:#f8f8f2;">)</span>
    <span style="color:#75715e;"># Substitute Tabs with Spaces</span>
    <span style="color:#f8f8f2;">line</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">line</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">replace(</span><span style="color:#e6db74;">'</span><span style="color:#ae81ff;">\t</span><span style="color:#e6db74;">'</span><span style="color:#f8f8f2;">,</span><span style="color:#e6db74;">' '</span><span style="color:#f8f8f2;">)</span>
    <span style="color:#75715e;"># While two spaces are in line we substitute the with one space</span>
    <span style="color:#66d9ef;">while</span> <span style="color:#e6db74;">'  '</span> <span style="color:#f92672;">in</span> <span style="color:#f8f8f2;">line:</span>
        <span style="color:#f8f8f2;">line</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">line</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">replace(</span><span style="color:#e6db74;">'  '</span><span style="color:#f8f8f2;">,</span><span style="color:#e6db74;">' '</span><span style="color:#f8f8f2;">)</span>
    <span style="color:#75715e;"># Remove [ and ]</span>
    <span style="color:#f8f8f2;">line</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">line</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">replace</span> <span style="color:#f8f8f2;">(</span><span style="color:#e6db74;">'['</span><span style="color:#f8f8f2;">,</span><span style="color:#e6db74;">''</span><span style="color:#f8f8f2;">)</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">replace(</span><span style="color:#e6db74;">']'</span><span style="color:#f8f8f2;">,</span><span style="color:#e6db74;">''</span><span style="color:#f8f8f2;">)</span>
    <span style="color:#75715e;"># If line is not empty</span>
    <span style="color:#66d9ef;">if</span> <span style="color:#f8f8f2;">len(line)</span><span style="color:#f92672;">&gt;</span><span style="color:#ae81ff;">0</span><span style="color:#f8f8f2;">:</span>
        <span style="color:#75715e;"># If line is not a comment</span>
        <span style="color:#66d9ef;">if</span> <span style="color:#f8f8f2;">line[</span><span style="color:#ae81ff;">0</span><span style="color:#f8f8f2;">]</span><span style="color:#f92672;">!=</span><span style="color:#e6db74;">'-'</span><span style="color:#f8f8f2;">:</span>
            <span style="color:#75715e;"># We add the new line to out_l</span>
            <span style="color:#f8f8f2;">out_l</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">append(re</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">split(</span><span style="color:#e6db74;">r'(?i)\bas\b'</span><span style="color:#f8f8f2;">,line))</span>
</pre>
Finally we come to the main code.
The first part is a For loop, using the list we created in step2.
For each line the script removes useless characters and comments and then adds the line to the new list.

<hr>

<h6>Step4-Output Text</h6>
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#75715e;"># Open output file</span>
<span style="color:#66d9ef;">with</span> <span style="color:#f8f8f2;">open(</span><span style="color:#e6db74;">'out.txt'</span><span style="color:#f8f8f2;">,</span><span style="color:#e6db74;">'w'</span><span style="color:#f8f8f2;">)</span> <span style="color:#66d9ef;">as</span> <span style="color:#f8f8f2;">out_txt:</span>
    <span style="color:#75715e;"># For line in output list</span>
    <span style="color:#66d9ef;">for</span> <span style="color:#f8f8f2;">line</span> <span style="color:#f92672;">in</span> <span style="color:#f8f8f2;">out_l:</span>
        <span style="color:#75715e;"># Try / Except to output all the values to the file separated by ','</span>
        <span style="color:#66d9ef;">print</span><span style="color:#f8f8f2;">(line)</span>
        <span style="color:#66d9ef;">if</span> <span style="color:#f8f8f2;">len(line)</span><span style="color:#f92672;">&gt;</span><span style="color:#ae81ff;">1</span><span style="color:#f8f8f2;">:</span>
            <span style="color:#f8f8f2;">out_txt</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">write(</span><span style="color:#e6db74;">'as'</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">join(line[</span><span style="color:#ae81ff;">0</span><span style="color:#f8f8f2;">:</span><span style="color:#f92672;">-</span><span style="color:#ae81ff;">1</span><span style="color:#f8f8f2;">])</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">strip()</span><span style="color:#f92672;">+</span><span style="color:#e6db74;">'|'</span><span style="color:#f92672;">+</span><span style="color:#f8f8f2;">str(line[</span><span style="color:#f92672;">-</span><span style="color:#ae81ff;">1</span><span style="color:#f8f8f2;">])</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">strip()</span><span style="color:#f92672;">+</span><span style="color:#e6db74;">'</span><span style="color:#ae81ff;">\n</span><span style="color:#e6db74;">'</span><span style="color:#f8f8f2;">)</span>
        <span style="color:#66d9ef;">else</span><span style="color:#f8f8f2;">:</span>
            <span style="color:#f8f8f2;">out_txt</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">write(str(line[</span><span style="color:#ae81ff;">0</span><span style="color:#f8f8f2;">])</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">strip()</span><span style="color:#f92672;">+</span><span style="color:#e6db74;">'|'</span><span style="color:#f92672;">+</span><span style="color:#f8f8f2;">str(line[</span><span style="color:#ae81ff;">0</span><span style="color:#f8f8f2;">])</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">strip()</span><span style="color:#f92672;">+</span><span style="color:#e6db74;">'</span><span style="color:#ae81ff;">\n</span><span style="color:#e6db74;">'</span><span style="color:#f8f8f2;">)</span>
</pre>
In the last part we write to an external file using a Try/Except to avoid IndexErrors.

This article is also available on <a href="https://powerbloggerbi.com">PowerBloggerBI</a></body></html>
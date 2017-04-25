<html><body><p>Last time we learned how to use stopwords with NLTK, today we are going to take a look at counting frequencies with NLTK.

You can find the project <a href="https://github.com/Inzaniak/pybistuff/tree/master/NLTK%20Freq">here</a>.

To start we need some text to analyze. We could use some of the books which are integrated in NLTK, but I prefer to read from an external file.
The best source of free ebooks to practice your text analysis skills is <a href="http://www.gutenberg.org">gutenberg</a>. Project Gutenberg is an awesome "open source" project that offers more than 53.000 free ebooks. For this tutorial we are going to use <a href="http://www.gutenberg.org/ebooks/345">Dracula</a> by Bram Stoker, you can download it as a UTF-8 txt.

For this project we are going to create the folders like this:
<img class="alignnone size-full wp-image-404" src="/2017/04/2017-04-20-15_16_25-prompt-dei-comandi.png" alt="2017-04-20 15_16_25-Prompt dei comandi" width="155" height="117">

You just need to download the utf-8 version of a book of your choice and save it as ebook.txt in data folder inside your project. You can download the stopwords from <a href="https://github.com/Inzaniak/pybistuff/tree/master/NLTK%20Freq">here</a>.

Let's start coding!
</p><pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#f92672;">import</span> <span style="color:#f8f8f2;">nltk</span>

<span style="color:#75715e;"># Let's declare a function to get word index</span>
<span style="color:#66d9ef;">def</span> <span style="color:#a6e22e;">get_index</span><span style="color:#f8f8f2;">(in_list,in_string):</span>
    <span style="color:#66d9ef;">for</span> <span style="color:#f8f8f2;">num,row</span> <span style="color:#f92672;">in</span> <span style="color:#f8f8f2;">enumerate(in_list):</span>
        <span style="color:#66d9ef;">if</span> <span style="color:#f8f8f2;">in_string</span> <span style="color:#f92672;">in</span> <span style="color:#f8f8f2;">row:</span>
            <span style="color:#66d9ef;">return</span> <span style="color:#f8f8f2;">num</span>

<span style="color:#75715e;"># Let's open the book we downloaded</span>
<span style="color:#f8f8f2;">book</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">open(</span><span style="color:#e6db74;">'data/ebook.txt'</span><span style="color:#f8f8f2;">,</span><span style="color:#e6db74;">'r'</span><span style="color:#f8f8f2;">)</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">read()</span>
<span style="color:#75715e;"># Divide text by rows</span>
<span style="color:#f8f8f2;">rows</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">book</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">split(</span><span style="color:#e6db74;">'</span><span style="color:#ae81ff;">\n</span><span style="color:#e6db74;">'</span><span style="color:#f8f8f2;">)</span>
</pre>
<code>
import nltk</code>
We import the necessary library as usual

<code>get_index()</code>
We define a simple function which helps us find the index of a word inside of a list. We loop for every row and if we find the string we return the index of the string

<code>open() and split()</code>
We load the book into a variable as a string and then we split it into lines
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#75715e;"># Search for START and END tags to remove useless parts</span>
<span style="color:#f8f8f2;">start_idx</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">get_index(rows,</span><span style="color:#e6db74;">'*** START'</span><span style="color:#f8f8f2;">)</span>
<span style="color:#f8f8f2;">end_idx</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">get_index(rows,</span><span style="color:#e6db74;">'*** END'</span><span style="color:#f8f8f2;">)</span>
<span style="color:#f8f8f2;">rows</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">rows[start_idx</span><span style="color:#f92672;">+</span><span style="color:#ae81ff;">1</span><span style="color:#f8f8f2;">:end_idx]</span>
</pre>
Now we look for START and END tags in our list and we redefine the list omitting the lines which are added by gutemberg.org.
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#75715e;"># Create a list of words by converting to lowercase and splitting</span>
<span style="color:#f8f8f2;">words</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">[s</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">lower()</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">split()</span> <span style="color:#66d9ef;">for</span> <span style="color:#f8f8f2;">s</span> <span style="color:#f92672;">in</span> <span style="color:#f8f8f2;">rows</span> <span style="color:#66d9ef;">if</span> <span style="color:#f8f8f2;">s]</span>
<span style="color:#75715e;"># Convert the list of lists into a flat list</span>
<span style="color:#f8f8f2;">words</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">[sublist</span> <span style="color:#66d9ef;">for</span> <span style="color:#f8f8f2;">l</span> <span style="color:#f92672;">in</span> <span style="color:#f8f8f2;">words</span> <span style="color:#66d9ef;">for</span> <span style="color:#f8f8f2;">sublist</span> <span style="color:#f92672;">in</span> <span style="color:#f8f8f2;">l]</span>

<span style="color:#75715e;"># Import the stopwords</span>
<span style="color:#f8f8f2;">stop</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">open(</span><span style="color:#e6db74;">'data/stop.txt'</span><span style="color:#f8f8f2;">,</span><span style="color:#e6db74;">'r'</span><span style="color:#f8f8f2;">)</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">read()</span>
<span style="color:#75715e;"># Split the stopwords by line</span>
<span style="color:#f8f8f2;">stop</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">stop</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">split(</span><span style="color:#e6db74;">'</span><span style="color:#ae81ff;">\n</span><span style="color:#e6db74;">'</span><span style="color:#f8f8f2;">)</span>

<span style="color:#75715e;"># Remove punctuation and numbers from words</span>
<span style="color:#f8f8f2;">words</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">[</span><span style="color:#e6db74;">''</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">join(c</span> <span style="color:#66d9ef;">for</span> <span style="color:#f8f8f2;">c</span> <span style="color:#f92672;">in</span> <span style="color:#f8f8f2;">w</span> <span style="color:#66d9ef;">if</span> <span style="color:#f8f8f2;">c</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">isalpha())</span> <span style="color:#66d9ef;">for</span> <span style="color:#f8f8f2;">w</span> <span style="color:#f92672;">in</span> <span style="color:#f8f8f2;">words]</span>
<span style="color:#75715e;"># Remove stopwords and blanks from words</span>
<span style="color:#f8f8f2;">words</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">[w</span> <span style="color:#66d9ef;">for</span> <span style="color:#f8f8f2;">w</span> <span style="color:#f92672;">in</span> <span style="color:#f8f8f2;">words</span> <span style="color:#66d9ef;">if</span> <span style="color:#f8f8f2;">w</span> <span style="color:#f92672;">not</span> <span style="color:#f92672;">in</span> <span style="color:#f8f8f2;">stop</span> <span style="color:#f92672;">and</span> <span style="color:#f8f8f2;">w</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">isalpha()]</span>
</pre>
We create a list of words by following these steps:
<ul>
	<li>Convert all the rows to lowercase and split the row into words</li>
	<li>Flatten the list of lists into a single list of words</li>
	<li>Load the stopwords and split them by line</li>
	<li>Remove punctuation from words</li>
	<li>Remove stopwords and empty elements from words</li>
</ul>
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#75715e;"># Let's load the word into NLTK</span>
<span style="color:#f8f8f2;">text</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">nltk</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">Text(words)</span>

<span style="color:#75715e;"># Calculate Frequency distribution</span>
<span style="color:#f8f8f2;">freq</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">nltk</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">FreqDist(text)</span>

<span style="color:#75715e;"># Print and plot most common words</span>
<span style="color:#f8f8f2;">freq</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">most_common(</span><span style="color:#ae81ff;">20</span><span style="color:#f8f8f2;">)</span>
<span style="color:#f8f8f2;">freq</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">plot(</span><span style="color:#ae81ff;">10</span><span style="color:#f8f8f2;">)</span>
</pre>
Now we can load our words into NLTK and calculate the frequencies by using FreqDist(). After this we can use .most_common(20) to show in console 20 most common words or .plot(10) to show a line plot representing word frequencies:
<img class="alignnone size-full wp-image-449" src="/2017/04/2017-04-20-15_47_21-figure-1.png" alt="2017-04-20 15_47_21-Figure 1" width="642" height="580">

Pretty boring words, how can we improve the output?
We can use bigrams to show more relevant data. From Wikipedia: A <b>bigram</b> or <b>digram</b> is a sequence of two adjacent elements from a string of tokens, which are typically letters, syllables, or words.
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#75715e;"># Get Bigrams from text</span>
<span style="color:#f8f8f2;">bigrams</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">nltk</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">bigrams(text)</span>

<span style="color:#75715e;"># Calculate Frequency Distribution for Bigrams</span>
<span style="color:#f8f8f2;">freq_bi</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">nltk</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">FreqDist(bigrams)</span>

<span style="color:#75715e;"># Print and plot most common bigrams</span>
<span style="color:#f8f8f2;">freq_bi</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">most_common(</span><span style="color:#ae81ff;">20</span><span style="color:#f8f8f2;">)</span>
<span style="color:#f8f8f2;">freq_bi</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">plot(</span><span style="color:#ae81ff;">10</span><span style="color:#f8f8f2;">)</span>
</pre>
After creating the bigrams we can plot them:
<img class="alignnone size-full wp-image-458" src="/2017/04/2017-04-20-15_56_03-figure-1.png" alt="2017-04-20 15_56_03-Figure 1.png" width="749" height="772">

Pretty cool, right?

That's it for today. Have fun experimenting with word frequencies</body></html>
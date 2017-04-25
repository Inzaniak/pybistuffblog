<html><body><p>One of the most tedious task in Text Analytics is cleaning raw text.
Fortunately NLTK has a lot of tools to help you in this task. One of the most important is <strong>nltk.corpus.stopwords</strong> which contains stopwords for 11 languages.

Let's start coding:
</p><pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#f92672;">import</span> <span style="color:#f8f8f2;">nltk</span>
<span style="color:#f8f8f2;">nltk</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">download()</span>
</pre>
First step is to install the stopwords so we run <strong>nltk.download()</strong>.

<img class="alignnone size-full wp-image-367" src="/2017/04/2017-04-18-12_48_29-nltk-downloader.png" alt="2017-04-18 12_48_29-NLTK Downloader" width="757" height="597">

Then we choose Corpora -&gt; Stopwords -&gt; Download

<img class="alignnone size-full wp-image-370" src="/2017/04/2017-04-18-12_50_19-nltk-downloader.png" alt="2017-04-18 12_50_19-NLTK Downloader.png" width="757" height="597">

Back to coding!
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#f92672;">from</span> <span style="color:#f8f8f2;">nltk.corpus</span> <span style="color:#66d9ef;">import</span> <span style="color:#f8f8f2;">stopwords</span>
<span style="color:#f8f8f2;">stop</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">stopwords</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">words(</span><span style="color:#e6db74;">'english'</span><span style="color:#f8f8f2;">)</span>
<span style="color:#f8f8f2;">print(stop[</span><span style="color:#ae81ff;">0</span><span style="color:#f8f8f2;">:</span><span style="color:#ae81ff;">5</span><span style="color:#f8f8f2;">])</span>
<span style="color:#75715e;"># ['i', 'me', 'my', 'myself', 'we']</span>
<span style="color:#f8f8f2;">print(type(stop))</span>
<span style="color:#75715e;"># &lt;class 'list'&gt;</span>
</pre>
The first line imports the corpus.reader, then we store into a variable the words contained in "English Stopwords". The words are returned as a list, so we can easily navigate them.

But how do we use them?
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#f8f8f2;">sentence</span> <span style="color:#f92672;">=</span> <span style="color:#e6db74;">'NLTK is a leading platform for building Python programs to work with human language data.'</span>
<span style="color:#75715e;"># With Generator</span>
<span style="color:#f8f8f2;">keywords</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">[w</span> <span style="color:#66d9ef;">for</span> <span style="color:#f8f8f2;">w</span> <span style="color:#f92672;">in</span> <span style="color:#f8f8f2;">sentence</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">split()</span> <span style="color:#66d9ef;">if</span> <span style="color:#f8f8f2;">w</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">lower()</span> <span style="color:#f92672;">not</span> <span style="color:#f92672;">in</span> <span style="color:#f8f8f2;">stop]</span>
<span style="color:#f8f8f2;">print(keywords)</span>
<span style="color:#75715e;"># ['NLTK', 'leading', 'platform', 'building', 'Python', 'programs', 'work', 'human', 'language', 'data.']</span>

<span style="color:#75715e;"># Without Generator</span>
<span style="color:#f8f8f2;">keywords</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">[]</span>
<span style="color:#66d9ef;">for</span> <span style="color:#f8f8f2;">word</span> <span style="color:#f92672;">in</span> <span style="color:#f8f8f2;">sentence</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">split():</span>
    <span style="color:#66d9ef;">if</span> <span style="color:#f8f8f2;">word</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">lower()</span> <span style="color:#f92672;">not</span> <span style="color:#f92672;">in</span> <span style="color:#f8f8f2;">stop:</span>
        <span style="color:#f8f8f2;">keywords</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">append(word)</span>
<span style="color:#f8f8f2;">print(keywords)</span>
<span style="color:#75715e;"># ['NLTK', 'leading', 'platform', 'building', 'Python', 'programs', 'work', 'human', 'language', 'data.']</span>
</pre>
We use a simple sentence as input. Then we use a generator or a "for loop" to create a list of keywords, by ignoring all the words that are not in our stopwords list.
We use word.lower() because all the words in the stopwords list are lowercase.

That's it, this is the fastest way to implement stopwords using NLTK.
Have fun</body></html>
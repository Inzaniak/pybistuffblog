<html><body><p>One of the most used format these days (especially online) is the Javascript Object Notation (JSON). At first sight it can be a little confusing, but after using it a few times it won't be a problem anymore.

So what's the best way to read Json in Python?
Luckily for you (and me) there is an awesome library integrated within Python named "json".

Let's start with a Json available on <a href="http://json.org/example.html">http://json.org/example.html</a>:
</p><pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#f8f8f2;">{</span>
    <span style="color:#f92672;">"glossary"</span><span style="color:#f8f8f2;">:</span> <span style="color:#f8f8f2;">{</span>
        <span style="color:#f92672;">"title"</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"example glossary"</span><span style="color:#f8f8f2;">,</span>
		<span style="color:#f92672;">"GlossDiv"</span><span style="color:#f8f8f2;">:</span> <span style="color:#f8f8f2;">{</span>
            <span style="color:#f92672;">"title"</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"S"</span><span style="color:#f8f8f2;">,</span>
			<span style="color:#f92672;">"GlossList"</span><span style="color:#f8f8f2;">:</span> <span style="color:#f8f8f2;">{</span>
                <span style="color:#f92672;">"GlossEntry"</span><span style="color:#f8f8f2;">:</span> <span style="color:#f8f8f2;">{</span>
                    <span style="color:#f92672;">"ID"</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"SGML"</span><span style="color:#f8f8f2;">,</span>
					<span style="color:#f92672;">"SortAs"</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"SGML"</span><span style="color:#f8f8f2;">,</span>
					<span style="color:#f92672;">"GlossTerm"</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"Standard Generalized Markup Language"</span><span style="color:#f8f8f2;">,</span>
					<span style="color:#f92672;">"Acronym"</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"SGML"</span><span style="color:#f8f8f2;">,</span>
					<span style="color:#f92672;">"Abbrev"</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"ISO 8879:1986"</span><span style="color:#f8f8f2;">,</span>
					<span style="color:#f92672;">"GlossDef"</span><span style="color:#f8f8f2;">:</span> <span style="color:#f8f8f2;">{</span>
                        <span style="color:#f92672;">"para"</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"A meta-markup language, used to create markup languages such as DocBook."</span><span style="color:#f8f8f2;">,</span>
						<span style="color:#f92672;">"GlossSeeAlso"</span><span style="color:#f8f8f2;">:</span> <span style="color:#f8f8f2;">[</span><span style="color:#e6db74;">"GML"</span><span style="color:#f8f8f2;">,</span> <span style="color:#e6db74;">"XML"</span><span style="color:#f8f8f2;">]</span>
                    <span style="color:#f8f8f2;">},</span>
					<span style="color:#f92672;">"GlossSee"</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"markup"</span>
                <span style="color:#f8f8f2;">}</span>
            <span style="color:#f8f8f2;">}</span>
        <span style="color:#f8f8f2;">}</span>
    <span style="color:#f8f8f2;">}</span>
<span style="color:#f8f8f2;">}</span>
</pre>
There are a few tools that help you format and read Json, these are the ones i use often:
<ul>
	<li><a href="http://jsonviewer.stack.hu">http://jsonviewer.stack.hu</a>: This is a really awesome site which helps you understand the content of the Json</li>
	<li><a href="http://atom.io">atom.io</a>: An awesome text editor that supports a lot of extension. I really suggest you to take a look at it</li>
</ul>
So let's take a look at this Json structure on Jsonviewer:

<img class="alignnone size-full wp-image-202" src="/2017/03/jsonviewer.png" alt="Jsonviewer" width="723" height="416">

Now, what are the first steps to import this data structure into our python script?
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#f92672;">import</span> <span style="color:#f8f8f2;">json</span>

<span style="color:#f8f8f2;">json_string</span> <span style="color:#f92672;">=</span> <span style="color:#e6db74;">"""</span>
<span style="color:#e6db74;">{</span>
<span style="color:#e6db74;">    "glossary": {</span>
<span style="color:#e6db74;">        "title": "example glossary",</span>
<span style="color:#e6db74;">		"GlossDiv": {</span>
<span style="color:#e6db74;">            "title": "S",</span>
<span style="color:#e6db74;">			"GlossList": {</span>
<span style="color:#e6db74;">                "GlossEntry": {</span>
<span style="color:#e6db74;">                    "ID": "SGML",</span>
<span style="color:#e6db74;">					"SortAs": "SGML",</span>
<span style="color:#e6db74;">					"GlossTerm": "Standard Generalized Markup Language",</span>
<span style="color:#e6db74;">					"Acronym": "SGML",</span>
<span style="color:#e6db74;">					"Abbrev": "ISO 8879:1986",</span>
<span style="color:#e6db74;">					"GlossDef": {</span>
<span style="color:#e6db74;">                        "para": "A meta-markup language, used to create markup languages such as DocBook.",</span>
<span style="color:#e6db74;">						"GlossSeeAlso": ["GML", "XML"]</span>
<span style="color:#e6db74;">                    },</span>
<span style="color:#e6db74;">					"GlossSee": "markup"</span>
<span style="color:#e6db74;">                }</span>
<span style="color:#e6db74;">            }</span>
<span style="color:#e6db74;">        }</span>
<span style="color:#e6db74;">    }</span>
<span style="color:#e6db74;">}</span>
<span style="color:#e6db74;">"""</span>

<span style="color:#f8f8f2;">my_json</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">json</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">loads(json_string)</span>
<span style="color:#f8f8f2;">print(my_json)</span>
</pre>
The first step is to import the library we are going to use: "json". Then we create a string which contains the Json we are going to read. Now that we have our Json we load it into a variable by using <em>json.loads() </em>and print the result:

<img class="alignnone size-full wp-image-211" src="/2017/03/jsonout1.png" alt="JsonOut1" width="1564" height="175">

We can see that the Json we loaded is outputted as a python Dict, which is convenient for us.
To navigate it you just need to use the syntax you'll use with a Dict:
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#f8f8f2;">print(my_json[</span><span style="color:#e6db74;">'glossary'</span><span style="color:#f8f8f2;">][</span><span style="color:#e6db74;">'title'</span><span style="color:#f8f8f2;">])</span>
<span style="color:#75715e;"># returns: example glossary</span>
<span style="color:#f8f8f2;">print(my_json[</span><span style="color:#e6db74;">'glossary'</span><span style="color:#f8f8f2;">][</span><span style="color:#e6db74;">'GlossDiv'</span><span style="color:#f8f8f2;">])</span>
<span style="color:#75715e;"># returns: a dict</span>
</pre>
That's pretty awesome right? But what if i need to output the json as is? There is a simple method in the json library named <em>dumps()</em> that does just what we need:
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#f8f8f2;">print(json</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">dumps(my_json))</span>
<span style="color:#f92672;">&gt;&gt;</span><span style="color:#f8f8f2;">{</span><span style="color:#e6db74;">"glossary"</span><span style="color:#f8f8f2;">:</span> <span style="color:#f8f8f2;">{</span><span style="color:#e6db74;">"title"</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"example glossary"</span><span style="color:#f8f8f2;">,</span> <span style="color:#e6db74;">"GlossDiv"</span><span style="color:#f8f8f2;">:</span> <span style="color:#f8f8f2;">{</span><span style="color:#e6db74;">"title"</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"S"</span><span style="color:#f8f8f2;">,</span> <span style="color:#e6db74;">"GlossList"</span><span style="color:#f8f8f2;">:</span> <span style="color:#f8f8f2;">{</span><span style="color:#e6db74;">"GlossEntry"</span><span style="color:#f8f8f2;">:</span> <span style="color:#f8f8f2;">{</span><span style="color:#e6db74;">"ID"</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"SGML"</span><span style="color:#f8f8f2;">,</span> <span style="color:#e6db74;">"GlossTerm"</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"Standard Generalized Markup Language"</span><span style="color:#f8f8f2;">,</span> <span style="color:#e6db74;">"Acronym"</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"SGML"</span><span style="color:#f8f8f2;">,</span> <span style="color:#e6db74;">"GlossSee"</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"markup"</span><span style="color:#f8f8f2;">,</span> <span style="color:#e6db74;">"SortAs"</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"SGML"</span><span style="color:#f8f8f2;">,</span> <span style="color:#e6db74;">"Abbrev"</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"ISO 8879:1986"</span><span style="color:#f8f8f2;">,</span> <span style="color:#e6db74;">"GlossDef"</span><span style="color:#f8f8f2;">:</span> <span style="color:#f8f8f2;">{</span><span style="color:#e6db74;">"GlossSeeAlso"</span><span style="color:#f8f8f2;">:</span> <span style="color:#f8f8f2;">[</span><span style="color:#e6db74;">"GML"</span><span style="color:#f8f8f2;">,</span> <span style="color:#e6db74;">"XML"</span><span style="color:#f8f8f2;">],</span> <span style="color:#e6db74;">"para"</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"A meta-markup language, used to create markup languages such as DocBook."</span><span style="color:#f8f8f2;">}}}}}}</span>
</pre>
 

I think that's all for this session! Thanks for reading.</body></html>
<html><body><p>One of the most annoying things that happens to me when i'm working with json extracted from social networks is the absence of some of the keys from the json.

If you try to read that the usual way:
</p><pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#f92672;">import</span> <span style="color:#f8f8f2;">json</span>

<span style="color:#f8f8f2;">user_id</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">{</span>
    <span style="color:#ae81ff;">101</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"Mario"</span><span style="color:#f8f8f2;">,</span>
    <span style="color:#ae81ff;">102</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"John"</span><span style="color:#f8f8f2;">,</span>
    <span style="color:#ae81ff;">103</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"Lewis"</span><span style="color:#f8f8f2;">,</span>
    <span style="color:#ae81ff;">105</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"Andrew"</span>
<span style="color:#f8f8f2;">}</span>

<span style="color:#66d9ef;">for</span> <span style="color:#f8f8f2;">i</span> <span style="color:#f92672;">in</span> <span style="color:#f8f8f2;">range(</span><span style="color:#ae81ff;">101</span><span style="color:#f8f8f2;">,</span><span style="color:#ae81ff;">106</span><span style="color:#f8f8f2;">):</span>
    <span style="color:#66d9ef;">print</span><span style="color:#f8f8f2;">(user_id[i])</span>
</pre>
You will have this error:

<img class="alignnone size-full wp-image-139" src="/2017/03/img1.png" alt="img1" width="872" height="206">
Because you are referencing an element that doesn't exists.

You could solve this problem by using a Try - Except statement, but that will make the code longer and less readable.

The best way to fix this is by using .get():
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#f92672;">import</span> <span style="color:#f8f8f2;">json</span>

<span style="color:#f8f8f2;">user_id</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">{</span>
    <span style="color:#ae81ff;">101</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"Mario"</span><span style="color:#f8f8f2;">,</span>
    <span style="color:#ae81ff;">102</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"John"</span><span style="color:#f8f8f2;">,</span>
    <span style="color:#ae81ff;">103</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"Lewis"</span><span style="color:#f8f8f2;">,</span>
    <span style="color:#ae81ff;">105</span><span style="color:#f8f8f2;">:</span> <span style="color:#e6db74;">"Andrew"</span>
<span style="color:#f8f8f2;">}</span>

<span style="color:#66d9ef;">for</span> <span style="color:#f8f8f2;">i</span> <span style="color:#f92672;">in</span> <span style="color:#f8f8f2;">range(</span><span style="color:#ae81ff;">101</span><span style="color:#f8f8f2;">,</span><span style="color:#ae81ff;">106</span><span style="color:#f8f8f2;">):</span>
    <span style="color:#66d9ef;">print</span><span style="color:#f8f8f2;">(user_id</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">get(i,</span><span style="color:#e6db74;">"ND"</span><span style="color:#f8f8f2;">))</span>
</pre>
The method: ".get()" extract the element from the json as usual, but when the value doesn't exit it returns a value chosen by the user.

This is really lifesaving when working with json.</body></html>
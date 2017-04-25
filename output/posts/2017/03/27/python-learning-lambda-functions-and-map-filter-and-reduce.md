<html><body><p>Python supports the creation of anonymous functions at runtime, using a construct called "<strong>lambda</strong>".

Let's see an example:
</p><pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#75715e;"># Standard way to define a function</span>
<span style="color:#66d9ef;">def</span> <span style="color:#a6e22e;">my_func</span><span style="color:#f8f8f2;">(in_num):</span>
    <span style="color:#66d9ef;">return</span> <span style="color:#f8f8f2;">in_num</span><span style="color:#f92672;">*</span><span style="color:#f8f8f2;">in_num</span>
    
<span style="color:#75715e;"># Lambda way</span>
<span style="color:#f8f8f2;">my_func_l</span> <span style="color:#f92672;">=</span> <span style="color:#66d9ef;">lambda</span> <span style="color:#f8f8f2;">x:</span> <span style="color:#f8f8f2;">x</span><span style="color:#f92672;">*</span><span style="color:#f8f8f2;">x</span></pre>
Both of the functions return the same result, but are declared in different ways.<img class="alignnone size-full wp-image-233" src="/2017/03/result.png" alt="result" width="159" height="77">

So the question is: "When is it useful to use a lambda function?".
I find it particularly useful when i'm working on "dynamic" functions:
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#66d9ef;">def</span> <span style="color:#a6e22e;">my_func</span><span style="color:#f8f8f2;">(n):</span>
    <span style="color:#66d9ef;">return</span> <span style="color:#66d9ef;">lambda</span> <span style="color:#f8f8f2;">x:x</span><span style="color:#f92672;">*</span><span style="color:#f8f8f2;">n</span>

<span style="color:#75715e;"># This creates the anonymous function by defining the n value</span>
<span style="color:#f8f8f2;">f</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">my_func(</span><span style="color:#ae81ff;">2</span><span style="color:#f8f8f2;">)</span>
<span style="color:#f8f8f2;">g</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">my_func(</span><span style="color:#ae81ff;">4</span><span style="color:#f8f8f2;">)</span>

<span style="color:#75715e;"># This calls the function by passing the parameter x</span>
<span style="color:#f8f8f2;">f(</span><span style="color:#ae81ff;">5</span><span style="color:#f8f8f2;">)</span>
<span style="color:#f8f8f2;">g(</span><span style="color:#ae81ff;">3</span><span style="color:#f8f8f2;">)</span>

<span style="color:#75715e;"># You can also call the function without assigning it</span>
<span style="color:#f8f8f2;">my_func(</span><span style="color:#ae81ff;">2</span><span style="color:#f8f8f2;">)(</span><span style="color:#ae81ff;">8</span><span style="color:#f8f8f2;">)</span>
</pre>
But Lambdas functions are often used with map, filter and reduce.
<h2>Map</h2>
<strong>Map</strong> applies a function to all the items in an input_list.
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#75715e;"># Let's declare a simple list of number</span>
<span style="color:#f8f8f2;">items</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">[</span><span style="color:#ae81ff;">1</span><span style="color:#f8f8f2;">,</span> <span style="color:#ae81ff;">2</span><span style="color:#f8f8f2;">,</span> <span style="color:#ae81ff;">3</span><span style="color:#f8f8f2;">,</span> <span style="color:#ae81ff;">4</span><span style="color:#f8f8f2;">,</span> <span style="color:#ae81ff;">5</span><span style="color:#f8f8f2;">]</span>
<span style="color:#75715e;"># We create a Lambda that does the square for the number</span>
<span style="color:#75715e;"># and apply it to the list by using map</span>
<span style="color:#f8f8f2;">list(map(</span><span style="color:#66d9ef;">lambda</span> <span style="color:#f8f8f2;">x:x</span><span style="color:#f92672;">*</span><span style="color:#f8f8f2;">x,items))
<span style="color:#ffcc99;">Out[354]: [1, 4, 9, 16, 25]</span></span>
</pre>
This is a really fast way to apply a function on a list. It is really useful if you need to use it once.
<h2>Filter</h2>
<strong>Filter </strong>creates a list of elements for which a function returns true.
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#75715e;"># Let's declare a simple list of number</span>
<span style="color:#f8f8f2;">items</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">[</span><span style="color:#ae81ff;">1</span><span style="color:#f8f8f2;">,</span> <span style="color:#ae81ff;">2</span><span style="color:#f8f8f2;">,</span> <span style="color:#ae81ff;">3</span><span style="color:#f8f8f2;">,</span> <span style="color:#ae81ff;">4</span><span style="color:#f8f8f2;">,</span> <span style="color:#ae81ff;">5</span><span style="color:#f8f8f2;">]</span>
<span style="color:#75715e;"># We create a Lambda that check if the number is even</span>
<span style="color:#75715e;"># and apply it to the list by using filter</span>
<span style="color:#f8f8f2;">list(filter(</span><span style="color:#66d9ef;">lambda</span> <span style="color:#f8f8f2;">x:</span> <span style="color:#f8f8f2;">x</span><span style="color:#f92672;">%</span><span style="color:#ae81ff;">2</span> <span style="color:#f92672;">==</span> <span style="color:#ae81ff;">0</span><span style="color:#f8f8f2;">,</span> <span style="color:#f8f8f2;">items))</span>
<span style="color:#ffcc99;">Out[356]: [2, 4]
</span></pre>
By using filter you can clean your list easily.
<h2>Reduce</h2>
<strong>Reduce </strong>is a really useful function for performing some computation on a list and returning the result.
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#75715e;"># We need to import reduce from functools library</span>
<span style="color:#f92672;">from</span> <span style="color:#f8f8f2;">functools</span> <span style="color:#66d9ef;">import</span> <span style="color:#f8f8f2;">reduce</span>
<span style="color:#75715e;"># Let's declare a simple list of number</span>
<span style="color:#f8f8f2;">items</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">[</span><span style="color:#ae81ff;">1</span><span style="color:#f8f8f2;">,</span> <span style="color:#ae81ff;">2</span><span style="color:#f8f8f2;">,</span> <span style="color:#ae81ff;">3</span><span style="color:#f8f8f2;">,</span> <span style="color:#ae81ff;">4</span><span style="color:#f8f8f2;">,</span> <span style="color:#ae81ff;">5</span><span style="color:#f8f8f2;">]</span>
<span style="color:#75715e;"># We create a Lambda that compute the product of the integers</span>
<span style="color:#75715e;"># and apply it to the list by using reduce</span>
<span style="color:#f8f8f2;">reduce(</span><span style="color:#66d9ef;">lambda</span> <span style="color:#f8f8f2;">x,y:</span> <span style="color:#f8f8f2;">x</span><span style="color:#f92672;">*</span><span style="color:#f8f8f2;">y,</span> <span style="color:#f8f8f2;">items)
<span style="color:#ffcc99;">Out[363]: 120</span></span>
</pre>
 

And that's all for today!</body></html>
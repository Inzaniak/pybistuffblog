<html><body><p>With this VB script you can create a simple searchbox:

<img class="alignnone size-full wp-image-41" src="/2017/02/excsearch.gif" alt="excsearch" width="285" height="265">
</p><pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><span style="color:#66d9ef;">Private</span> <span style="color:#66d9ef;">Sub</span> <span style="color:#a6e22e;">Worksheet_Change</span><span style="color:#f8f8f2;">(</span><span style="color:#66d9ef;">ByVal</span> <span style="color:#f8f8f2;">Target</span> <span style="color:#f92672;">As</span> <span style="color:#f8f8f2;">Range)</span>
  <span style="color:#75715e;">'Variable to clear filters on table</span>
  <span style="color:#66d9ef;">Dim</span> <span style="color:#f8f8f2;">tableNum</span> <span style="color:#f92672;">As</span> <span style="color:#66d9ef;">Integer</span>
  <span style="color:#75715e;">'Variable containing searchbox position</span>
  <span style="color:#66d9ef;">Dim</span> <span style="color:#f8f8f2;">searchBoxPos</span> <span style="color:#f92672;">As</span> <span style="color:#66d9ef;">String</span>
  <span style="color:#f8f8f2;">searchBoxPos</span> <span style="color:#f92672;">=</span> <span style="color:#e6db74;">"B2"</span>
  <span style="color:#75715e;">'Var containing the first element of the column affected by the search</span>
  <span style="color:#66d9ef;">Dim</span> <span style="color:#f8f8f2;">colToSearch</span> <span style="color:#f92672;">As</span> <span style="color:#66d9ef;">String</span>
  <span style="color:#f8f8f2;">colToSearch</span> <span style="color:#f92672;">=</span> <span style="color:#e6db74;">"B4"</span>
  
  <span style="color:#75715e;">'Check if searchbox cell is edited</span>
  <span style="color:#66d9ef;">If</span> <span style="color:#66d9ef;">Not</span> <span style="color:#f8f8f2;">Application.Intersect(Target,</span> <span style="color:#f8f8f2;">Range(searchBoxPos))</span> <span style="color:#f92672;">Is</span> <span style="color:#66d9ef;">Nothing</span> <span style="color:#66d9ef;">Then</span>
  <span style="color:#f8f8f2;">Range(Range(colToSearch),</span> <span style="color:#f8f8f2;">Range(colToSearch).End(xlDown)).AutoFilter</span> <span style="color:#f8f8f2;">Field:</span><span style="color:#f92672;">=</span><span style="color:#ae81ff;">1</span><span style="color:#f8f8f2;">,</span> <span style="color:#f8f8f2;">Criteria1:</span><span style="color:#f92672;">=</span><span style="color:#e6db74;">"*"</span> <span style="color:#f92672;">&amp;</span> <span style="color:#f8f8f2;">Range(searchBoxPos).Value</span> <span style="color:#f92672;">&amp;</span> <span style="color:#e6db74;">"*"</span><span style="color:#f8f8f2;">,</span> <span style="color:#66d9ef;">Operator</span><span style="color:#f8f8f2;">:</span><span style="color:#f92672;">=</span><span style="color:#f8f8f2;">xlAnd</span>
  <span style="color:#75715e;">'If searchbox is empty remove all filters</span>
  <span style="color:#66d9ef;">If</span> <span style="color:#f8f8f2;">Range(searchBoxPos).Value</span> <span style="color:#f92672;">=</span> <span style="color:#e6db74;">""</span> <span style="color:#66d9ef;">Then</span>
  <span style="color:#f8f8f2;">tableNum</span> <span style="color:#f92672;">=</span> <span style="color:#ae81ff;">1</span>
  <span style="color:#66d9ef;">For</span> <span style="color:#66d9ef;">Each</span> <span style="color:#f8f8f2;">element</span> <span style="color:#f92672;">In</span> <span style="color:#f8f8f2;">ActiveSheet.ListObjects</span>
  <span style="color:#f8f8f2;">ActiveSheet.ListObjects(tableNum).Range.AutoFilter</span>
  <span style="color:#f8f8f2;">tableNum</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">tableNum</span> <span style="color:#f92672;">+</span> <span style="color:#ae81ff;">1</span>
  <span style="color:#66d9ef;">Next</span> <span style="color:#f8f8f2;">element</span>
  <span style="color:#66d9ef;">End</span> <span style="color:#66d9ef;">If</span>
  <span style="color:#66d9ef;">End</span> <span style="color:#66d9ef;">If</span>
  <span style="color:#66d9ef;">End</span> <span style="color:#66d9ef;">Sub</span>
</pre></body></html>
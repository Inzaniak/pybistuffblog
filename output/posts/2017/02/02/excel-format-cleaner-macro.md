<html><body><p>A simple VBA script to clean all the formatting in cells.
<img class=" size-full wp-image-60 aligncenter" src="/2017/02/textclean.gif" alt="textclean" width="479" height="119">
</p><pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#66d9ef;">Sub</span> <span style="color:#a6e22e;">CleanTxt</span><span style="color:#f8f8f2;">()</span>
    <span style="color:#f8f8f2;">Selection.Font.Bold</span> <span style="color:#f92672;">=</span> <span style="color:#66d9ef;">False</span>
    <span style="color:#f8f8f2;">Selection.Font.Italic</span> <span style="color:#f92672;">=</span> <span style="color:#66d9ef;">False</span>
    <span style="color:#f8f8f2;">Selection.Font.Underline</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">xlUnderlineStyleNone</span>
    <span style="color:#f8f8f2;">Selection.Borders(xlDiagonalDown).LineStyle</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">xlNone</span>
    <span style="color:#f8f8f2;">Selection.Borders(xlDiagonalUp).LineStyle</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">xlNone</span>
    <span style="color:#f8f8f2;">Selection.Borders(xlEdgeLeft).LineStyle</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">xlNone</span>
    <span style="color:#f8f8f2;">Selection.Borders(xlEdgeTop).LineStyle</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">xlNone</span>
    <span style="color:#f8f8f2;">Selection.Borders(xlEdgeBottom).LineStyle</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">xlNone</span>
    <span style="color:#f8f8f2;">Selection.Borders(xlEdgeRight).LineStyle</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">xlNone</span>
    <span style="color:#f8f8f2;">Selection.Borders(xlInsideVertical).LineStyle</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">xlNone</span>
    <span style="color:#f8f8f2;">Selection.Borders(xlInsideHorizontal).LineStyle</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">xlNone</span>
    <span style="color:#66d9ef;">With</span> <span style="color:#f8f8f2;">Selection.Interior</span>
        <span style="color:#f8f8f2;">.Pattern</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">xlNone</span>
        <span style="color:#f8f8f2;">.TintAndShade</span> <span style="color:#f92672;">=</span> <span style="color:#ae81ff;">0</span>
        <span style="color:#f8f8f2;">.PatternTintAndShade</span> <span style="color:#f92672;">=</span> <span style="color:#ae81ff;">0</span>
    <span style="color:#66d9ef;">End</span> <span style="color:#66d9ef;">With</span>
    <span style="color:#66d9ef;">With</span> <span style="color:#f8f8f2;">Selection.Font</span>
        <span style="color:#f8f8f2;">.ColorIndex</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">xlAutomatic</span>
        <span style="color:#f8f8f2;">.TintAndShade</span> <span style="color:#f92672;">=</span> <span style="color:#ae81ff;">0</span>
    <span style="color:#66d9ef;">End</span> <span style="color:#66d9ef;">With</span>
<span style="color:#66d9ef;">End</span> <span style="color:#66d9ef;">Sub</span>
</pre></body></html>
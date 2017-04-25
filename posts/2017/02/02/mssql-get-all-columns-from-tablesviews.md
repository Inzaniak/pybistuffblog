<html><body><p>When developing a database, it can be useful to be aware of column names on tables, in case one wants to check for aliasing errors or search for a specific column.

To retrieve them, you just need to read from some system views.
</p><ul>
	<li>sys.columns: Contains the list of columns contained within the DB.</li>
	<li>sys.tables: Contains the list of tables contained within the DB.</li>
	<li>sys.schemas: Contains a list of the schemas contained within the DB.</li>
	<li>sys.types: Contains the list of data types contained within the DB.</li>
	<li>sys.views: Contains the list of views contained within the DB.</li>
</ul>
Launching one of these two scripts you will get the list of tables or views with their schemas and their columns with data types

<b>Version with tables:</b>
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#66d9ef;">select</span>   <span style="color:#f8f8f2;">s.name</span>   <span style="color:#66d9ef;">as</span> <span style="color:#f8f8f2;">[</span><span style="color:#66d9ef;">Schema</span><span style="color:#f8f8f2;">]</span>
  <span style="color:#f8f8f2;">,t.name</span>   <span style="color:#66d9ef;">as</span> <span style="color:#f8f8f2;">[</span><span style="color:#66d9ef;">Table</span><span style="color:#f8f8f2;">]</span>
  <span style="color:#f8f8f2;">,</span><span style="color:#66d9ef;">c</span><span style="color:#f8f8f2;">.name</span>   <span style="color:#66d9ef;">as</span> <span style="color:#f8f8f2;">[</span><span style="color:#66d9ef;">Column</span><span style="color:#f8f8f2;">]</span>
  <span style="color:#f8f8f2;">,tp.name</span>  <span style="color:#66d9ef;">as</span> <span style="color:#f8f8f2;">[</span><span style="color:#66d9ef;">Type</span><span style="color:#f8f8f2;">]</span>
  <span style="color:#f8f8f2;">,</span><span style="color:#66d9ef;">c</span><span style="color:#f8f8f2;">.max_length</span> <span style="color:#66d9ef;">as</span> <span style="color:#f8f8f2;">[</span><span style="color:#66d9ef;">Length</span><span style="color:#f8f8f2;">]</span>
<span style="color:#66d9ef;">from</span> <span style="color:#f8f8f2;">sys.columns</span> <span style="color:#66d9ef;">c</span>
<span style="color:#66d9ef;">join</span> <span style="color:#f8f8f2;">sys.tables</span> <span style="color:#f8f8f2;">t</span>
<span style="color:#66d9ef;">on</span> <span style="color:#66d9ef;">c</span><span style="color:#f8f8f2;">.object_id</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">t.object_id</span>
<span style="color:#66d9ef;">join</span> <span style="color:#f8f8f2;">sys.schemas</span> <span style="color:#f8f8f2;">s</span>
<span style="color:#66d9ef;">on</span> <span style="color:#f8f8f2;">s.schema_id</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">t.schema_id</span>
<span style="color:#66d9ef;">join</span> <span style="color:#f8f8f2;">sys.types</span> <span style="color:#f8f8f2;">tp</span>
<span style="color:#66d9ef;">on</span> <span style="color:#66d9ef;">c</span><span style="color:#f8f8f2;">.system_type_id</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">tp.system_type_id</span>
</pre>
 

<b>Version with Views:</b>
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#66d9ef;">select</span>   <span style="color:#f8f8f2;">s.name</span>   <span style="color:#66d9ef;">as</span> <span style="color:#f8f8f2;">[</span><span style="color:#66d9ef;">Schema</span><span style="color:#f8f8f2;">]</span>
  <span style="color:#f8f8f2;">,v.name</span>   <span style="color:#66d9ef;">as</span> <span style="color:#f8f8f2;">[</span><span style="color:#66d9ef;">View</span><span style="color:#f8f8f2;">]</span>
  <span style="color:#f8f8f2;">,</span><span style="color:#66d9ef;">c</span><span style="color:#f8f8f2;">.name</span>   <span style="color:#66d9ef;">as</span> <span style="color:#f8f8f2;">[</span><span style="color:#66d9ef;">Column</span><span style="color:#f8f8f2;">]</span>
  <span style="color:#f8f8f2;">,tp.name</span>  <span style="color:#66d9ef;">as</span> <span style="color:#f8f8f2;">[</span><span style="color:#66d9ef;">Type</span><span style="color:#f8f8f2;">]</span>
  <span style="color:#f8f8f2;">,</span><span style="color:#66d9ef;">c</span><span style="color:#f8f8f2;">.max_length</span> <span style="color:#66d9ef;">as</span> <span style="color:#f8f8f2;">[</span><span style="color:#66d9ef;">Length</span><span style="color:#f8f8f2;">]</span>
<span style="color:#66d9ef;">from</span> <span style="color:#f8f8f2;">sys.columns</span> <span style="color:#66d9ef;">c</span>
<span style="color:#66d9ef;">join</span> <span style="color:#f8f8f2;">sys.views</span> <span style="color:#f8f8f2;">v</span>
<span style="color:#66d9ef;">on</span> <span style="color:#66d9ef;">c</span><span style="color:#f8f8f2;">.object_id</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">v.object_id</span>
<span style="color:#66d9ef;">join</span> <span style="color:#f8f8f2;">sys.schemas</span> <span style="color:#f8f8f2;">s</span>
<span style="color:#66d9ef;">on</span> <span style="color:#f8f8f2;">s.schema_id</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">v.schema_id</span>
<span style="color:#66d9ef;">join</span> <span style="color:#f8f8f2;">sys.types</span> <span style="color:#f8f8f2;">tp</span>
<span style="color:#66d9ef;">on</span> <span style="color:#66d9ef;">c</span><span style="color:#f8f8f2;">.system_type_id</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">tp.system_type_id</span>
</pre></body></html>
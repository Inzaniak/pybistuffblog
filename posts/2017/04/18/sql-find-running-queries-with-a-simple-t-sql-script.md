<html><body><p>Today i want to share a simple snippet of code which I find useful from time to time.
With this code you can check if a query is running on your db in a quick and effective way.
</p><pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#66d9ef;">SELECT</span> 
	<span style="color:#f8f8f2;">sqltext.TEXT,</span> 
	<span style="color:#f8f8f2;">req.session_id,</span> 
	<span style="color:#f8f8f2;">req.status,</span> 
	<span style="color:#f8f8f2;">req.command,</span> 
	<span style="color:#f8f8f2;">req.cpu_time,</span> 
	<span style="color:#f8f8f2;">req.total_elapsed_time</span> 
<span style="color:#66d9ef;">FROM</span> <span style="color:#f8f8f2;">sys.dm_exec_requests</span> <span style="color:#f8f8f2;">req</span> 
	<span style="color:#66d9ef;">CROSS</span> <span style="color:#f8f8f2;">APPLY</span> <span style="color:#f8f8f2;">sys.dm_exec_sql_text(sql_handle)</span> <span style="color:#66d9ef;">AS</span> <span style="color:#f8f8f2;">sqltext</span>
</pre>
That's it, have a nice day :)</body></html>
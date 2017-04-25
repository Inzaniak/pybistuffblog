<html><body><p>As a SQL/Python coder, one of the library i use the most is <em><a href="https://github.com/mkleehammer/pyodbc/wiki">pyodbc</a>.
</em><i>p</i>yodbc is an open source Python module that makes accessing ODBC databases simple. It implements the <a href="https://www.python.org/dev/peps/pep-0249">DB API 2.0</a> specification but is packed with even more Pythonic convenience.

Let's start coding then!
</p><pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#75715e;"># Let's import the library</span>
<span style="color:#f92672;">import</span> <span style="color:#f8f8f2;">pyodbc</span>

<span style="color:#75715e;"># Here we set the connection variables</span>
<span style="color:#f8f8f2;">server</span> <span style="color:#f92672;">=</span> <span style="color:#e6db74;">'your_server_name'</span>
<span style="color:#f8f8f2;">database</span> <span style="color:#f92672;">=</span> <span style="color:#e6db74;">'your_db_name'</span>
<span style="color:#75715e;"># Username and password if you use a SQL account. Otherwise it will use</span>
<span style="color:#75715e;"># Windows Authentication</span>
<span style="color:#f8f8f2;">username</span> <span style="color:#f92672;">=</span> <span style="color:#e6db74;">'your_username'</span>
<span style="color:#f8f8f2;">password</span> <span style="color:#f92672;">=</span> <span style="color:#e6db74;">'your_password'</span>
<span style="color:#75715e;"># The driver you are going to use.</span>
<span style="color:#f8f8f2;">driver</span><span style="color:#f92672;">=</span> <span style="color:#e6db74;">'{ODBC Driver 13 for SQL Server}'</span>

<span style="color:#75715e;"># Let's Create a connection and a cursor</span>
<span style="color:#f8f8f2;">conn</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">pyodbc</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">connect(</span><span style="color:#e6db74;">'DRIVER='</span><span style="color:#f92672;">+</span><span style="color:#f8f8f2;">driver</span>
                      <span style="color:#f92672;">+</span><span style="color:#e6db74;">';PORT=1433;SERVER='</span><span style="color:#f92672;">+</span><span style="color:#f8f8f2;">server</span>
                      <span style="color:#f92672;">+</span><span style="color:#e6db74;">';DATABASE='</span><span style="color:#f92672;">+</span><span style="color:#f8f8f2;">database</span>
                      <span style="color:#f92672;">+</span><span style="color:#e6db74;">';UID='</span><span style="color:#f92672;">+</span><span style="color:#f8f8f2;">username</span><span style="color:#f92672;">+</span><span style="color:#e6db74;">';PWD='</span><span style="color:#f92672;">+</span> <span style="color:#f8f8f2;">password)</span>
<span style="color:#f8f8f2;">cursor</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">conn</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">cursor()</span>
</pre>
The first step is to import the library. If you need to install it: pip install pyodbc.

After importing the library we need to set up the connection variables.
You'll need you server name, database name and username and password. If you don't have a User because you are using Windows Authentication, just remove the variables from the connection string.
The driver variable is the driver version you are using to connect to SQL. If you can't connect because of a driver error, just Google download odbc driver 13 :) .

To connect to SQL we need to pass the variables to the pyodbc.connect() function.
Then we need to create a cursor by using the conn.cursor()
<h2>Select</h2>
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#75715e;"># SELECT</span>
<span style="color:#f8f8f2;">cursor</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">execute(</span><span style="color:#e6db74;">"SELECT FROM dbo.your_table"</span><span style="color:#f8f8f2;">)</span>
<span style="color:#f8f8f2;">rows</span> <span style="color:#f92672;">=</span> <span style="color:#f8f8f2;">cursor</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">fetchall()</span>
<span style="color:#66d9ef;">for</span> <span style="color:#f8f8f2;">row</span> <span style="color:#f92672;">in</span> <span style="color:#f8f8f2;">rows:</span>
    <span style="color:#f8f8f2;">print(row[</span><span style="color:#ae81ff;">0</span><span style="color:#f8f8f2;">],row[</span><span style="color:#ae81ff;">1</span><span style="color:#f8f8f2;">])</span>
</pre>
To communicate with SQL, we use cursor.execute(). You just need to pass a query and use fetchone() or fetchall() to return the result.
With fetchall() you can loop over the rows by using a for loop.
<h2>Insert/Update/Delete etc...</h2>
<pre style="background:#272822;overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;margin:0;line-height:125%;"><span style="color:#75715e;"># INSERT</span>
<span style="color:#f8f8f2;">cursor</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">execute(</span><span style="color:#e6db74;">"INSERT into dbo.your_table VALUES ('test')"</span><span style="color:#f8f8f2;">)</span>
<span style="color:#f8f8f2;">cursor</span><span style="color:#f92672;">.</span><span style="color:#f8f8f2;">commit()</span>
</pre>
To run an insert,update or delete you just need to execute the statement and the commit it to the server.

That's all for today!</body></html>
<html><body><p>More than once I found myself with the annoying problem of not being able to connect to a wifi network.

I'm sure it's happened to you.

Often just a simple reboot to fix the problem, but system reboots are slow and tedious. Through these commands you will be able to reset DNS, IP and Proxies.

Just run Command Prompt and paste the script by right-clicking.
</p><div style="background:#272822;border-width:.1em .1em .1em .8em;border:solid gray;overflow:auto;padding:.2em .6em;width:auto;">
<p style="line-height:125%;margin:0;"><span style="color:#f8f8f2;">ipconfig</span> <span style="color:#f8f8f2;">/flushdns</span></p>
<p style="line-height:125%;margin:0;"><span style="color:#f8f8f2;">ipconfig</span> <span style="color:#f8f8f2;">/release</span></p>
<p style="line-height:125%;margin:0;"><span style="color:#f8f8f2;">ipconfig</span> <span style="color:#f8f8f2;">/renew</span></p>
<p style="line-height:125%;margin:0;"><span style="color:#f8f8f2;">set</span> <span style="color:#f8f8f2;">http_proxy</span><span style="color:#f92672;">=</span></p>
<p style="line-height:125%;margin:0;"><span style="color:#f8f8f2;">set</span> <span style="color:#f8f8f2;">https_proxy</span><span style="color:#f92672;">=</span></p>

</div></body></html>
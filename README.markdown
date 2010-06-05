> Good morning, fuckspores. Yet another horrible morning in this endless cold damp ash-covered hell we call "life." Smile.
>
> * [@warrenellis](http://twitter.com/warrenellis) on [tweet](http://twitter.com/warrenellis/status/14156393417)

Fuckspores is a Facebook replacement that is built on open standards. There already are tools and standards for distributing
status information called feeds. Fuckspores is just a tool that aggregates your friend's feeds into Facebook like interface.

At least for now fuckspores are not shared. You create fuckspores for your friends or import them. You manage them and can do
whatever you want with them. Which means that people described in fuckspores do have no control over them. 

## Fuckspore File Format ##

fuckspore := "FUCKSPORE" CRLF metadata urllist
metadata := name "=" value CRLF metadata | CRLF 
urllist := url CRLF urllist | url

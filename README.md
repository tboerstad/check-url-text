# check-url-text
Crawl a web page and send a mobile notification (Using Yo-app) if a criterion is met.
An example use case is if you want to poll Amazon, and be notified if price changes. 

The script crawls the URLs given in `config.py`.
It then searches through all `<divs>` on the page, and tries to find a
`<div>` with a given `class` name. If it does, the script will send a notification 
if the contents of the `<div>`s found does not match the given `string`.

The `<div>` `class` and `string` are given as a list of tuples, `DIVCLASS_STRING`, in `config.py`.


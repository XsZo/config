This is for **Clash**, a network core in go.

Well, I thought deep and decided to rely on subconverter for clash configurations, because many users are used to the 'paste and go' experience many clients provide, and don't bother the trouble directly editing the yaml files. Also, subconverter provides universal experience rewriting some parts of the config, which saves time both for you and me. The only problem is that you need a subconverter backend, there's some public choice though without uptime and privacy grantee, and setting up one yourself is pretty troublesome. But I made up my mind to move to this.

To use, you need url of a subconverter endpoint, which looks like `https://example.com/sub` . Then let's pass some values to define the result template, which looks like `?target=clash&config=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FXsZo%2Fconfig%40network%2Fclash%2Fclash.ini`, '?' marks the start of properties and '&' seperates each. And include your subscription url, first google a url encoder, and paste your links, seperate them with '|', then do url encode and copy the result, pass it to the endpoint like `&url=https%3A%2F%2Fexample.com%2Fsample.txt`. All done, the final url will look like `https://example.com/sub?target=clash&config=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FXsZo%2Fconfig%40network%2Fclash%2Fclash.ini&url=https%3A%2F%2Fexample.com%2Fsample.txt`, just use it like your sub link.

`clash.ini` is the configurations passed to subconverter to make target profile. It's located at `https://cdn.jsdelivr.net/gh/XsZo/config@network/clash/clash.ini`, and you may use `config=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FXsZo%2Fconfig%40network%2Fclash%2Fclash.ini` in the url to refer to it.

If you want to use global mode, just point Default group to preferred destination and use your GUI client's built in feature to Global mode, and point the newly added Global group to Default. Default is not used in rule mode.

None of the trust worthy public DNS service is avaliable in PRC, so no need to set fallback.

`?target=clash&config=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FXsZo%2Fconfig%40network%2Fclash%2Fconvert.ini&url=`

`?target=clash&config=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FXsZo%2Fconfig%40network%2Fclash%2Fsimple.ini&url=`

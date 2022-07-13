# Network Traffic Processing Rules

This branch mainly host network filtering rules, request rewrite rules, and more.

## Filters

`filter/` is generated from `src/filter/` using `gen.py`.

These lists intend to cover popular domains around the world, and to reduce string look up load, those less popular ones were removed, so when you need to ensure access to local sites, we recommend using geoip as an addition. (Please note that geoip consumes much more resource than domain rules, and has to wait for dns lookup, so we recommend using one at most.)

I know that `game.txt` lacks many popular games, `region.txt` lacks many popular sites, and many other rulesets have issues. I will be happy if you can submit it on [github](https://github.com/XsZo/config/discussions) or create a pr.

### usage

The first part of url is `https://cdn.jsdelivr.net/gh/XsZo/config@net-rule/filter/`.

Then append the rule style info refering to table below:

| \*  | content          |
| :-: | :--------------- |
|  q  | quantumult style |
|  s  | surge style      |
|  c  | clash style      |

Then append the rule dest info refering to table below:

|  \*.   | content                                                |
| :----: | :----------------------------------------------------- |
| direct | intranet, no-proxy, speedtest domains                  |
| block  | domains used by some unwanted services                 |
| global | domains used by services without regional restrictions |
| system | domains used by services of operating system           |
|  game  | domains used by some games and services using udp      |
| region | domains used by region sensitive services              |
|  r-cn  | domains used by PRC related services                   |
|  r-jp  | domains used by Japanese local services                |
|  r-tw  | domains used by Taiwanese local services               |
|  r-us  | domains used by American local services                |

Then rule type info refering to table below:

| .\*.txt(yml) | content                    |
| :----------: | :------------------------- |
|    (null)    | domain, domain-suffix      |
|      ip      | ip-cidr, v4 or v6          |
|      ms      | domain-keyword, port, etc. |

So the actual url shall look like  
`https://cdn.jsdelivr.net/gh/XsZo/config@net-rule/filter/s/direct.txt`  
`https://cdn.jsdelivr.net/gh/XsZo/config@net-rule/filter/s/direct.ip.txt`

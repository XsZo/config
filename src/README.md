## Filters

```yaml
domain:
  - example.com
  - _example.com
ip:
  - 0.0.0.0/8
ip6:
  - "::1/128"
port:
  - 80
```

generates:

```txt
DOMAIN-SUFFIX,example.com
DOMAIN,example.com
IP-CIDR,0.0.0.0/8
IP6-CIDR,::1/128
DST-PORT,80
```

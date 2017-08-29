# Readme for Unix commands and Unix administration 

- How to tell if a URL is being re-directed:
```
curl -w "%{url_effective}\n" -I -L -s -S $URL -o /dev/null
```

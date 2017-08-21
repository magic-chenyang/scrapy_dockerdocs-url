# scrapy_dockerdocs-url
### 爬虫scrapy
1. 先爬取docs-docker-cn.com的所有url
2. 将url传入redis中
3. scrapy提取redis中的url,按照url爬取数据.
4. 将爬取数据存去elasticsearch中.

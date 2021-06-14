# python_code-for-Finding-the-Restricted-Parts-of-a-Web-Site
here we have imported two modules. With the help of module functions, we build a simple function that first checks whether you want to go after a subdomain.
After that, it reads the data, and we'll get some print output. 



#Example(Finding-the-Restricted-Parts-of-a-Web-Site)


change the last line of the get robots function, and instead of a simple site, let’s crawl a comparatively heavy site like https://www.reddit.com. 
You may get different results. Change the last line of code to this:
print(GetRobots("https://www.reddit.com")) 
Now, look at the output. It has changed drastically. /usr/bin/python3.4 /home/hagudu/PycharmProjects/ FirstPythonProject/Nmap/robots.py # 80legs
User-agent: 008 
Disallow: /
# 80legs' new crawler User-agent: voltron
Disallow: /
User-Agent: bender 
Disallow: /my_shiny_metal_ass
User-Agent: Gort 
Disallow: /earth
User-agent: MJ12bot
Disallow: /
User-agent: PiplBot 
Disallow: /
User-Agent: * 
Disallow: /*.json
Disallow: /*.json-compact 
Disallow: /*.json-html 
Disallow: /*.xml 
Disallow: /*.rss 
Disallow: /*.i 
Disallow: /*.embed
Disallow: /*/comments/*?*sort= 
Disallow: /r/*/comments/*/*/c* 
Disallow: /comments/*/*/c* 
Disallow: /r/*/submit 
Disallow: /message/compose* 
Disallow: /api 
Disallow: /post
Disallow: /submit
Disallow: /goto 
Disallow: /*after= 
Disallow: /*before= 
Disallow: /domain/*t= 
Disallow: /login
Disallow: /reddits/search 
Disallow: /search 
Disallow: /r/*/search 
Disallow: /r/*/user/ 
Disallow: /gold? 
Allow: /partner_api/ 
Allow: /
Allow: /sitemaps/*.xml
Sitemap: https://www.reddit.com/sitemaps/subreddit-sitemaps.xml 
Sitemap: https://www.reddit.com/sitemaps/comment-page-sitemaps. xml
Process finished with exit code 0


#Example(Finding IP address using URL)
ip = socket.gethostbyname("google.com")
142.250.193.14
Process finished with exit code 0

from urllib import parse, request
import re
search = 'gatitos'
query_string = parse.urlencode({'search_query': search})
html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
search_results = re.findall('\\/watch\\?v=(.{11})', html_content.read().decode())
print(search_results[0])
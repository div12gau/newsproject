# importing api 
from django.http import HttpResponse
from django.shortcuts import render 
from newsapi import NewsApiClient 

# Create your views here. 
def index(request): 
	#return HttpResponse("dfsahhjfkdsa")
	newsapi = NewsApiClient(api_key ='0efb2e56129647378bd3d31cc9f5b487') 
	top = newsapi.get_top_headlines(sources ='nbc-news') 
	l = top['articles'] 
	desc =[] 
	news =[] 
	img =[] 
	for i in range(len(l)): 
		f = l[i] 
		news.append(f['title']) 
		desc.append(f['description']) 
		img.append(f['urlToImage']) 
	mylist = zip(news, desc, img)
	#return render(request,'newsapp/base.html') 
	return render(request,'newsapp/index.html',context ={"mylist":mylist}) 

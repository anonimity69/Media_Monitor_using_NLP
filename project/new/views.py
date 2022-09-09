from django.shortcuts import redirect, render
from django.http import HttpResponse
from googlesearch import search
import pickle

def home(request):
    return render(request, 'index.html')

def home2(request):
    return render(request, 'method.html')

def home3(request):
    return render(request, 'about.html')


def product(request):
    if request.method == 'POST':
        product = request.POST.get('product')
    try:
        query = product+"Reviews"
        url = []
        for j in search(query, tld="co.in", num=10, stop=10, pause=2):
            url.append(j)
        site = url[0]
    except:
        return render(request, 'index.html')
    model = pickle.load(open("new/model3.pkl", "rb"))
    if(model > 0.50):
            comment = "Very Positive Reviews:\n  \
                       Highly Trusted"
    elif(model > 0.25):
            comment = "Moderately Positive Reviews:\n  \
                       Mostly Trusted"
    elif(model > 0):
            comment = "Not Much Positive Reviews:\n  \
                       Moderately Trusted but with few Bad Insights"
    elif(model == 0):
            comment =  "Neutral reviews:\n  \
                        Not so much Trusted"
    else:
            comment = "very bad:\n   \
                       Not Trusted. Maximum People hated it."
    return render(request, 'index.html', {'site': site, 'model': comment})
    

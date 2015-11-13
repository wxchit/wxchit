# -*- coding: cp936 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from bookdb.models import *
from itertools import chain
from django.template import RequestContext



#找作者写的书
def Search_form(request):
    return render(request, 'search_form.html')
    
def Search(request):
    name = request.GET["name"]
    people = Author.objects.filter(Name=name)

    ID = []
    tag = 0
    book = []
    if(len(people) != 0):     #判断有没有此人
        tag = 1
        for i in range(0, len(people)):
            ID.append(people[i].AuthorID)

        book = Book.objects.filter(AuthorID = ID[0])
        for i in range(1, len(ID)):
            book = book|Book.objects.filter(AuthorID = ID[i])
                
    return render(request, 'Search.html', {'book': book, 'tag': tag})



#找书的信息
def book_views(request):
    isbn = request.GET["isbn"]
    bk = Book.objects.get(ISBN=isbn)
    author = Author.objects.get(AuthorID=bk.AuthorID)
    return render(request, 'views.html', {'bk': bk, 'author': author})



#删除操作
def Delete(request):
    isbn = request.GET["isbn"]
    ID = Book.objects.get(ISBN=isbn).AuthorID
    author_name = Author.objects.get(AuthorID=ID).Name
    Book.objects.filter(ISBN=isbn).delete()
    
    return render(request, 'delete.html', {'author_name': author_name})



#新增一本图书
def add_form(request):
    return render(request, 'add_form.html')



def Add(request):
    authorid = request.POST["authorid"]
    if request.method == 'POST':
        post = request.POST
        new_book = Book(
            ISBN = post["isbn"],
            Title = post["title"],
            AuthorID = authorid,
            Publisher = post["publisher"],
            PublishDate = post["publishdate"],
            Price = post["price"])
        new_book.save()
     
    #return render_to_response("add_result1.html",context_instance=RequestContext(request))

    
    #Book.objects.create(ISBN=request.POST["isbn"],Title=request.POST["title"],AuthorID=request.POST["authorid"],Publisher=request.POST["publisher"],PublishDate=request.POST["publishdate"],Price=POST["price"])
    
   
    #c = RequestContext(request, {'authorid': request.POST["authorid"]})    
    #return render_to_response('add_result1.html', c) 
    
    #global authorid
    #c = RequestContext(request, {'authorid': authorid})
    bk=Author.objects.filter(AuthorID=post["authorid"])
    if(len(bk) != 0):
        return render_to_response("add_result1.html",context_instance=RequestContext(request))
    else:
        return render_to_response("tip.html",context_instance=RequestContext(request, {'authorid': authorid}))
        
        
        
        
    
    


def update(request):
    isbn = request.GET["isbn"]
    bk = Book.objects.get(ISBN=isbn)
    #c = RequestContext(request, {'bk': bk})

    if request.method == 'POST':
        bk.Publisher = request.POST["publisher"]
        bk.PublishDate = request.POST["publishdate"]
        bk.Price = request.POST["price"]
        bk.AuthorID = request.POST["authorid"]
        '''
        authorid = request.POST["authorid"]
        if(len(authorid.objects.filter(AuthorID=authorid)) != 0):
            bk.AuthorID = authorid
        '''    
        
        bk.save()

        
    return render_to_response("update.html",context_instance=RequestContext(request, {'bk': bk}))



def add_author(request):
    authorid = request.GET["authorid"]
    if request.method == 'POST':
        post = request.POST
        #new_author =(
            #AuthorID = authorid
           # Name = post["name"]
          #  Age = post["age"]
         #   Country = post["country"])
        #new_author.save()
        Author.objects.create(AuthorID=authorid, Name=post["name"], Age=post["age"], Country=post["country"])

    return render_to_response("add_result2.html",context_instance=RequestContext(request, ))


    

# Create your views here.

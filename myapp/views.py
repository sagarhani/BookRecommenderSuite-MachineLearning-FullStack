from django.shortcuts import render,HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from myapp.models import book, reviews
from random import randint
import os
from django.conf import settings

def home(request):
      return render_to_response('home.html')

def log_in(request):
      return render(request,'log_in.html')

def log_out(request):
	logout(request)
	return HttpResponseRedirect('/home')

def sample(request):
	  all_books = book.objects.all();
	  return render(request, 'sample.html', {'all_books':all_books},content_type=RequestContext(request))

@csrf_exempt
def my_view(request):
	if request.method=='POST':
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
		else:
			return render(request,'fail.html',{},content_type=RequestContext(request))
	username=request.user.username
	books1 = reviews.objects.filter(name=username)
	allb = book.objects.all()
	randb = []
	reviewed_books = [] 
	rev_book=reviews.objects.filter(name=username)
	leng=len(rev_book)
	for i in range(0,leng):
		reviewed_books.append(rev_book[i].bookid)
	print("Reviewed books")
	print(reviewed_books)
	rev_gen=[]
	for i in range(0,leng):
		x=book.objects.get(id=reviewed_books[i])
		rev_gen.append(x.genre_name)
	
	count = 0
	for i in range(0,132):
		j = randint(1,132)
		if j not in reviewed_books:
			randb.append(j)
			count = count + 1
			if count == 5:
				break
				
	ttb=book.objects.order_by('-rating')[:132]
	ttbs=[]
	for i in range(0,10):
		x=book.objects.get(name=ttb[i].name)
		'''print(x.id)'''
		ttbs.append(x.id)
	print(ttbs)

	cbct=0
	cbbl=[]
	for i in range(0,132):
		if ttb[i].id not in reviewed_books:
			for j in set(rev_gen):
				if ttb[i].genre_name % j==0:
					cbbl.append(ttb[i].id)
					cbct+=1
			if cbct==10:
				break
	cbbl=set(cbbl)
	cbbl=list(cbbl)
	print(cbbl)

	return render(request,'welcome.html',{'username':username, 'all_books':books1, 'rev':reviewed_books, 'allb':allb, 'rbs':randb, 'ttbs':ttbs, 'cbbl':cbbl},content_type=RequestContext(request))
		

def signup(request):
	  return render(request,'signup.html')

def signingup(request):
	  username = request.POST.get("username")
	  firstname = request.POST.get("fname")
	  lastname = request.POST.get("lname")
	  mail = request.POST.get("mail")
	  pwd = request.POST.get("pwd")
	  user = User.objects.create_user(username,mail,pwd)
	  user.first_name = firstname
	  user.last_name = lastname
	  user.save()
	  user1 = authenticate(username=username, password=pwd)
	  if user1 is not None:
		  return render(request,'success.html',{},content_type=RequestContext(request))
	  else:
		  return render(request,'fail.html',{},content_type=RequestContext(request))

def binarysearch(wordList, user_review):
    start = 0
    end = len(wordList) - 1
    while start <= end:
    	middle = int((start + end)/2)
    	midpoint = wordList[middle]
    	if midpoint > user_review:
    		end = middle - 1
    	elif midpoint < user_review:
    		start = middle + 1
    	else:
    		return midpoint
    return -1
    
@csrf_exempt
def reloading(request):
	if request.method=="POST":
		user_l=request.user
		review=request.POST.get("review")
		bid=request.POST.get("abcd")
		reviews.objects.create(name=user_l.username,review=review,bookid=bid,rating=0)
		negative_array = []
		file1 = open(os.path.join(settings.PROJECT_ROOT, 'negative.txt'))
		'''with open('./negative.txt','r') as f:'''
		for line in file1:
		    for word in line.split():
		        negative_array.append(word)
		'''for x in negative_array:
			print(x)
		'''
		negative_stararray = []
		file11 = open(os.path.join(settings.PROJECT_ROOT, 'starnegative.txt'))
		'''with open('./negative.txt','r') as f:'''
		for line in file11:
		    for word in line.split():
		        negative_stararray.append(word)
		positive_array = []

		file2 = open(os.path.join(settings.PROJECT_ROOT, 'positive.txt'))
		for line in file2:
		    for word in line.split():
		        positive_array.append(word)
		'''for x in positive_array:
			print(x)
		'''
		'''punctuation = [',','.','!','?','\'','"',':',';']'''
		positive_stararray = []
		file22 = open(os.path.join(settings.PROJECT_ROOT, 'starpositive.txt'))
		'''with open('./negative.txt','r') as f:'''
		for line in file22:
		    for word in line.split():
		        positive_stararray.append(word)
		review_nostop = []
		stop = set(stopwords.words('english'))
		"""review = input('Enter a review. ')"""
		review_low = review.lower()
		review_low = ''.join([c for c in review_low if c not in (',','.','!','?','\'','"',':',';',')','(')])
		print(review_low)
		for word in review_low.split():
			if word not in stop:
				review_nostop.append(word)
		print(review_nostop)

		length_review = len(review_low.split())
		print(length_review)
		pos_count = 0
		neg_count = 0
		for word in review_nostop:
			posstar = binarysearch(positive_stararray,word)
			if posstar != -1:
				pos_count+=2
				length_review+=1
			else:
				pos = binarysearch(positive_array,word)
				if pos != -1:
					pos_count+=1
			negstar = binarysearch(negative_stararray,word)
			if negstar != -1:
				neg_count+=2
				length_review+=1
			else:
				neg = binarysearch(negative_array,word)
				if neg !=-1:
					neg_count+=1

		prob_positive = pos_count/length_review
		prob_negative = neg_count/length_review
		print(prob_positive)
		print(prob_negative)
		if prob_positive > prob_negative:
			npv=prob_positive
		else:
			npv=-1*prob_negative
		obj1=book.objects.get(id=bid)
		'''print(obj1.name)'''
		val=obj1.rating
		val=val+(npv*10)
		'''obj1.rating=val
		obj1.save()'''
		book.objects.filter(id=bid).update(rating=val)
		return HttpResponseRedirect('/log_in/my_view')
	#return redirect('/log_in/my_view')
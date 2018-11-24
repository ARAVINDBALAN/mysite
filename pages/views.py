from django.shortcuts import render
from django.http import HttpResponse
from .models import menu,student,payment
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,authenticate
from django.views.generic import ListView,DetailView

# def home(request):
#   return render(request,"home.html",{}) 
def about(request):
  return render(request,"about.html",{})
def login(request):
  return render(request,"login.html",{})
def order(request):
  	return render(request,"order.html",{})
def adminp(request):
  return render(request,"adminp.html",{})
def vo(request):
  return render(request,"vo.html",{}) 



def placeorder(request):
	m_list = menu.objects.all()
	if request.method == "POST":
		form = ordernow(request.POST)
		if form.is_valid():
			f = form.save(commit=False)
			avail = form.cleaned_data['i_id'].qty
			req = form.cleaned_data['quantity_order']
			if (req>avail):
				messages.success(request,'enter valid no of item less than max limit')
			else:
				m = menu.objects.get(id=form.cleaned_data['i_id'].id)
				m.qty = m.qty - req
				pri = m.price
				f.amount = pri*req
				m.save()
			print(avail,req)
			f.owner = request.user
			f.save()		
	else :
		form = ordernow()
	return render(request,'order.html',{'form':form,'m_list':m_list})					



# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user1 = form.save()
#             user1.refresh_from_db()  # load the profile instance created by the signal
#             user1.student.name = form.cleaned_data.get('name')
#             user1.student.email = form.cleaned_data.get('email')
#             user1.student.ph_no = form.cleaned_data.get('ph_no')
#             user1.save()
#             raw_password = form.cleaned_data.get('password1')
#             user1 = authenticate(username=user1.username, password=raw_password)
#             login(request, user1)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})


class MenuList(ListView):
	context_object_name = 'menu_list'
	model = menu
	template_name = 'home.html'

class MList(ListView):
	context_object_name = 'm_list'
	model = menu
	template_name = 'order.html'

class SList(ListView):
	context_object_name = 's_list'
	model = student
	template_name = 'student.html'

class PList(DetailView):
	context_object_name = 'p_list'
	model = student
	template_name = 'profile.html'

def profile(request):
	s = student.objects.filter(stud=request.user)
	print(s)
	return render(request,'profile.html',{'student':s})
# def pages(request):
# 	all_menus=menu.objects.all()
# 	"""for f in spots:
# 		html += "<p>item_id:" + f.item_id + "<br> item_name:" + str(f.item_name) +"<br> quantity:" + f.quantity + "<br> rate:" + f.rate+ "<br></p>"
# 	return HttpResponse(html)"""
   
# 	context={
# 	'item_id':all_menus.item_id,
# 	'item_name':all_menus.item_name,
# 	'quantity':all_menus.qty,
# 	'price':all_menus.price,
# 	}
# 	return render(request,"home.html",context=context)

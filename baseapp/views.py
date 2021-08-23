from django.shortcuts import render

def show_index(request):
	active = 1
	context = {
		'active' : active,
 	}
	return render(request, 'baseapp/index.html', context)

def show_products(request):
	active = 2
	context = {
		'active' : active,
 	}
	return render(request, 'baseapp/products.html', context)

def show_about(request):
	active = 3
	context = {
		'active' : active,
 	}
	return render(request, 'baseapp/about.html', context)

def show_contacts(request):
	active = 4
	context = {
		'active' : active,
 	}
	return render(request, 'baseapp/contacts.html', context)

def show_production(request):
	active = 5
	context = {
		'active' : active,
 	}
	return render(request, 'baseapp/production.html', context)
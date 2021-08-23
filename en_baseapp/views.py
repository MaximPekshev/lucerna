from django.shortcuts import render

def en_show_index(request):
	active = 1
	context = {
		'active' : active,
 	}
	return render(request, 'en_baseapp/en_index.html', context)

def en_show_products(request):
	active = 2
	context = {
		'active' : active,
 	}
	return render(request, 'en_baseapp/en_products.html', context)

def en_show_about(request):
	active = 3
	context = {
		'active' : active,
 	}
	return render(request, 'en_baseapp/en_about.html', context)

def en_show_contacts(request):
	active = 4
	context = {
		'active' : active,
 	}
	return render(request, 'en_baseapp/en_contacts.html', context)

def en_show_production(request):
	active = 5
	context = {
		'active' : active,
 	}
	return render(request, 'en_baseapp/en_production.html', context)	
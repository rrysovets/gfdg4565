from django.shortcuts import render, redirect
from .models import FormData

def submit_data_view(request):

    if request.method == 'POST':
        items = request.POST.getlist('items[]')
        items = [item for item in items if item.strip()]
        if items:
            FormData.objects.create(data=items)
            return redirect('list_data')
    return render(request, 'submit_data.html')

def list_data_view(request):
    form_data_list = FormData.objects.all().order_by('-created_at')
    return render(request, 'list_data.html', {'form_data_list': form_data_list})

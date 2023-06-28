# views.py
from django.shortcuts import render
from .forms import MyForm

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        oform = MyForm()
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            # Do something with the input_text
            return render(request, 'index.html', {'input_text': input_text , 'form' : oform,} )
    else:
        form = MyForm()
    return render(request, 'index.html', {'form': form})

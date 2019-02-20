from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Memo
from .forms import MemoForm


# Create your views here.

def show(request):
    memo_id = request.GET.get('id')
    memo = Memo.objects.get(pk=memo_id)
    return HttpResponse("%s:%s" % (memo.title,memo.content))

def create(request):
    if request.method == 'GET':
        form = MemoForm()
        return render(request, 'create.html', {'form': form})
    elif request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.save()
            return redirect('/memo?id=%s' % memo.pk)

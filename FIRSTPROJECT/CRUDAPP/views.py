from django.shortcuts import get_object_or_404, redirect, render
from .forms import bookform
from .models import books

#CREATE THE BOOK_LIST VIEW
def book_list(request):
    book1= books.objects.all() #make one object book1 and add all entry in that
    return render(request,"book/book_list.html",{'object_list':book1}) # tell browswer where to render the page where object
    #list is storing the book1 object.

def book_view(request,pk):
    book2=get_object_or_404(books,pk=pk)
    return render(request,"book/book_detail.html",{'object':book2})

def book_update(request,pk):
    book3=get_object_or_404(books,pk=pk)
    form=bookform(request.POST or None,instance=book3)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request,'book/book_form.html',{'form':form})

def book_delete(request,pk):
    book4=get_object_or_404(books,pk=pk)
    if request.method=='POST':
        book4.delete()
        return redirect('book_list')
    return render(request,'book/book_delete.html',{'object':book4})

def book_create(request):
    form=bookform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request,'book/book_form.html',{'form':form})

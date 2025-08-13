# Create your views here.
from django.shortcuts import render, redirect
from .models import Ebook
from django.db.models import Q
from .forms import EbookForm
from rest_framework import generics
from .serializers import EbookSerializer


def home(request):
    books = Ebook.objects.all().order_by('-uploaded_at')
    return render(request, 'home.html', {'books': books})

def search(request):
    query = request.GET.get('q', '')
    results = Ebook.objects.filter(
        Q(title__icontains=query) |
        Q(author__icontains=query) |
        Q(genre__icontains=query) |
        Q(topic__icontains=query) |
        Q(publisher__icontains=query)
    ) if query else []
    return render(request, 'search.html', {'results': results, 'query': query})

def book_detail(request, pk):
    book = Ebook.objects.get(pk=pk)
    return render(request, 'detail.html', {'book': book})

def upload_book(request):
    if request.method == 'POST':
        form = EbookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EbookForm()
    return render(request, 'upload.html', {'form': form})


class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

class EbookDetailAPIView(generics.RetrieveAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer



#For databse on render
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Ebook
from .serializers import EbookSerializer

@method_decorator(csrf_exempt, name="dispatch")   # ✅ avoid CSRF block for public upload
class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all().order_by("-uploaded_at")
    serializer_class = EbookSerializer
    parser_classes = [MultiPartParser, FormParser]  # ✅ accept files
    permission_classes = [AllowAny]

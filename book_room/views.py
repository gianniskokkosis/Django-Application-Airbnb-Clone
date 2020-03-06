from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Room, Review, Purchase


class RoomListView(ListView):
    model = Room
    template_name = 'book_room/homepage.html'

    def get_queryset(self):
        queryset = Room.objects.all()
        location = self.request.GET.get('search')

        if  location != '' and location is not None:
            queryset = queryset.filter(location__icontains=location)
        return queryset
    
    context_object_name = 'queryset'

    paginate_by = 3


class RoomDetailView(DetailView):
    model = Room
    template_name = 'book_room/detail.html'


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['review_content']
    template_name = 'book_room/new_review.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.room = Room.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)


class PurchaseCreateView(LoginRequiredMixin, CreateView):
    model = Purchase
    fields= ['name', 'surname', 'address', 'country', 'city',
            'card_name', 'card_number', 'card_exp_date', 'card_cvv']

    template_name = 'book_room/purchase.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.room = Room.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)


class ReviewListView(ListView):
    model = Review
    template_name = 'book_room/all_reviews.html'
    
    def get_queryset(self):
        queryset = Review.objects.filter(room__id__icontains = self.kwargs['pk'])
        return queryset

    def get_context_data(self, *args, **kwargs):
        queryset = super(ReviewListView, self).get_context_data(*args, **kwargs)
        queryset['review_obj'] = Room.objects.get(pk=self.kwargs['pk'])
        return queryset

    context_object_name = 'queryset'

class ReviewUserList(LoginRequiredMixin, ListView):
    model = Review
    template_name = 'book_room/user_reviews.html'

    def get_queryset(self):
        queryset = Review.objects.filter(user__username__icontains = self.request.user)
        return queryset
    
    context_object_name = 'queryset'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'book_room/detail_review.html'

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['review_content']
    template_name = 'book_room/new_review.html'

    def form_valid(self, form):
        review_obj = Review.objects.get(pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.room = Room.objects.get(pk=review_obj.room.id)
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'book_room/delete_review.html'
    success_url = '/user_reviews/'

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False

class UserPurchasesListView(ListView):
    model = Purchase
    template_name='book_room/user_purchases.html'

    def get_queryset(self):
        queryset = Purchase.objects.filter(user__username__icontains = self.request.user)
        return queryset
    
    context_object_name = 'queryset'
        



def about(request):
    return render(request, 'book_room/about.html')

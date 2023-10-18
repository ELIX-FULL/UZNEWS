from django.views.generic import ListView, DetailView
from products.models import ProductModel, CategoryModel

class IndexPageView(ListView):
    template_name = 'index.html'
    queryset = ProductModel.objects.all()
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q')
        category = self.request.GET.get('category')
        sort = self.request.GET.get('sort')

        if q:
            qs = qs.filter(title__icontains=q)

        if category:
            category_ids = category.split(',')
            qs = qs.filter(category__in=category_ids)

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = CategoryModel.objects.all()

        return context


class IndexDetailView(DetailView):
    template_name = 'index-details.html'
    model = ProductModel
    context_object_name = 'products'



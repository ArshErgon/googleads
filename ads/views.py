from django.shortcuts import render, get_object_or_404 

from .models import SEO, RecipeModel

seo_data = SEO.objects.all()
for seo_loop in seo_data:
    pass

def desktop_home_page(request):
    # print(dir(RecipeModel.objects))
    print(RecipeModel.objects.filter(slug_title='making/slug/filed/workinm'))

    return render(request, 'desktop/home/index.html', {'seo':seo_loop, 'all_recipes':RecipeModel.objects.all(),})

def desktop_single_page_recipes(request, slug_title):
    single_recipe = get_object_or_404(RecipeModel, slug_title=slug_title)
    recom_recipes = RecipeModel.objects.order_by("?")[:3]
    return render(request, 'desktop/single/single_page.html', {'seo_data':seo_loop, 'single_rec_desplay':single_recipe, "recom_recipes":recom_recipes})
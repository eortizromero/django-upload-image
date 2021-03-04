from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.views.generic.list import ListView
from home.models import Images
from home.forms import ImageForm

class ImageFormAttrs(ImageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control form-control-lg br-input',
                'required': 'required'
            })

def image_delete(request, id):
    Images.objects.get(id=id).delete()
    return redirect('/')

def image_detail(request, id):
    data = Images.objects.get(id=id)
    return render(request, 'home/image_detail.html', {'data': data})

def image_list(request):
    ## Restructurar codigo para cargar datos con validaciones
    if request.method == 'POST':
        form = ImageFormAttrs(request.POST, request.FILES)

        img_obj = [] 
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return redirect('/')
        return render(request, 'home/image_list.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageFormAttrs()
        img_obj = Images.objects.all()
        return render(request, 'home/image_list.html', {'form': form, 'img_obj': img_obj})


'''class ImageList(ListView):
    template_name = 'home/image_list.html'
    model = Images
    context_object_name = 'images'

    def get_context_data(self, **kwargs):
        res = super(ImageList, self).get_context_data(**kwargs)
        print(res)
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, )
        res.update({
            'form':  
        })
        return res
'''
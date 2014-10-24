import json
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views.generic import TemplateView
from django.http import QueryDict
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string


from quick_list import models, forms


def index(request):
    '''
    '''
    context = dict()
    quick_lists = models.QuickList.objects.all().select_related('item')
    
    context['quick_lists'] = quick_lists

    context['form'] = forms.QuickListForm()

    return render_to_response(
        'quick_list/quick_lists.html',
        context,
        context_instance=RequestContext(request)
    )



def quick_list(request, list_id=None):
    print "IN quick list"

    context = dict()
    if request.method == "POST":
        form = forms.QuickListForm(request.POST)
        if form.is_valid():
            print "Valid Form"
            gl, created = models.QuickList.objects.get_or_create(
                title=form.cleaned_data.get("title"))
            context['id'] = gl.id
            context['title'] = gl.title
            context['created_date'] = str(gl.created_date)
        else:
            print "invalid"
            context['errors'] = form.errors
            print form.errors

    elif request.method == "DELETE":
        print "Trying to delete"

    return HttpResponse(json.dumps(context), content_type="application/json")


def quick_list_items(request, list_id=None):
    """
    """
    print "IN items"
    context = dict()
    status = 200
    
    if request.method == "GET":
        print "Getting Items"
        context['quick_list'] = models.QuickList.objects.get(id=list_id)
        context['quick_list_items'] = models.QuickListItem.objects.filter(quick_list=list_id).order_by("-created_date")
        print context['quick_list']
        context['form'] = forms.QuickListItemForm()
        return render_to_response(
            'quick_list/quick_list_items.html',
            context,
            context_instance=RequestContext(request)
        )
        
    elif request.method == "POST":
        print request.POST
        form = forms.QuickListItemForm(request.POST)
        if form.is_valid():
            ql = models.QuickList.objects.get(id=list_id)

            i, ic = ql.quicklistitem_set.get_or_create(
                name=form.cleaned_data['name']
            )

            context['name'] = i.name
            context['category'] = i.category
            context['active'] = i.active
            context['id'] = i.id
            context['list_id'] = ql.id
            print context

        else:
            print "Not valid"
            status = 404
            print form.errors

        # item = models.GroceryItem.objects.get_or_create()

    elif request.method == "PUT":
        print "I am trying to update with a PUT"
        put = QueryDict(request.body)
        print put
        
        try:
            item = models.QuickListItem.objects.get(id=put.get("item_id"))
        except ObjectDoesNotExist:
            print "Dont' exists"
            item = None

        form = forms.QuickListItemForm(put, instance=item)
        if form.is_valid():
            print "PUT IS VALID"
            form.save()
            context['name'] = item.name
            # context['category'] = item.category
            context['active'] = item.active
            context['id'] = item.id
        else:
            status=404
            print form.errors

    elif request.method == "DELETE":
        print "Trying to delete"
        print request.body
        delete = QueryDict(request.body)
        gl = models.QuickList.objects.get(id=delete['quick_list']).delete()
        context['delete'] = "successful"
        # return redirect('/')


    # context['grocery_list'] = gl
    # context['form'] = forms.GroceryItemForm()

    return HttpResponse(json.dumps(context), status=status, content_type="application/json")


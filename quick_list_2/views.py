import json
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import QueryDict

from quick_list import forms, models


# def index(request):
#     '''
#     '''
#     print "QUICK INDEX"
#     context = dict()
#     context['quick_list'] = models.QuickList.objects.all()
#     # context['grocery_list'] = shopping_list
#     context['form'] = forms.QuickListForm()
#     # context['gform'] = forms.GroceryListForm()

#     return render_to_response(
#         'quick_list/index.html',
#         context,
#         context_instance=RequestContext(request)
#     )

def quick_list(request, list_id=None):
    context = dict()
    print "in quick list 2"
    if request.method == "POST":
        form = forms.QuickListForm(request.POST)
        if form.is_valid():
            print "I am a valid post"
            ql, created = models.QuickList.objects.get_or_create(
                title=form.cleaned_data.get("title"))
            context['id'] = ql.id
            context['title'] = ql.title
            context['created_date'] = str(ql.created_date)
        else:
            print form.errors
        return redirect('quick_list')

    context['quick_list'] = models.QuickList.objects.all()
    # context['grocery_list'] = shopping_list
    context['form'] = forms.QuickListForm()
    return render_to_response(
        'quick_list_2/quick_lists.html',
        context,
        context_instance=RequestContext(request)
    )
    # return HttpResponse(json.dumps(context), content_type="application/json")
def quick_list_items(request, list_id=None):
    print "IN quick items"
    context = dict()
    if request.method == "GET":
        print "getting"


    if request.method == "POST":
        print "item post"
        form = forms.QuickListItemForm(request.POST)
        if form.is_valid():
            print "item post is valid"
            ql = models.QuickList.objects.get(id=list_id)
            i, ic = ql.quicklistitem_set.get_or_create(
                name=form.cleaned_data['name']
            )
        else:
            print form.errors

    elif request.method == "DELETE":
        print "Trying to delete"
        print request.body
        delete = QueryDict(request.body)
        print delete

    context['form'] = forms.QuickListItemForm()
    context['items'] = models.QuickListItem.objects.filter(quick_list=list_id).order_by("-created_date")
    context['quick_list'] = models.QuickList.objects.get(id=list_id)

    return render_to_response(
        'quick_list_2/quick_list_2_items.html',
        context,
        context_instance=RequestContext(request)
    ) 
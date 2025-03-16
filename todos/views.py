from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

from .forms import CreateTodoForm
from .models import TodoItem

@require_http_methods(["GET"])
def index(request):
    
    form = CreateTodoForm()
    todos = TodoItem.objects.all()
    context = {"form": form, "todo_items": todos}
    return render(request=request, template_name="todos/index.html", context=context)

@require_http_methods(["POST"])
def action_add_new_todo(request):
    form = CreateTodoForm(request.POST)
    instance = form.save()
    return render(request, "todos/partial_todo_item.html", {"item": instance, "form": CreateTodoForm()})

@require_http_methods(["PUT"])
def action_toggle_todo(request, item_id):
    item = TodoItem.objects.get(id=item_id)
    item.completed = not item.completed
    item.save()
    return HttpResponse('') 

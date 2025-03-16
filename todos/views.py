from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import CreateTodoForm

@require_http_methods(["GET"])
def index(request):
    
    form = CreateTodoForm()
    context = {"form": form}
    return render(request=request, template_name="todos/index.html", context=context)

@require_http_methods(["POST"])
def action_add_new_todo(request):
    form = CreateTodoForm(request.POST)
    instance = form.save()
    return render(request, "todos/partial_todo_item.html", {"item": instance, "form": CreateTodoForm()})

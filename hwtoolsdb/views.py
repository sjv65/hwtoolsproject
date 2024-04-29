from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tool
from .forms import ToolForm


from django.shortcuts import render
from .models import Tool

def tools_list(request):
    tools = Tool.objects.all()
    return render(request, 'hwtoolsdb/tools_list.html', {'tools': tools})


def add_or_edit_tool(request, id=None):
    if id:
        tool = Tool.objects.get(id=id)
    else:
        tool = None

    if request.method == 'POST':
        form = ToolForm(request.POST, instance=tool)
        if form.is_valid():
            form.save()
            return redirect('tools-list')
    else:
        form = ToolForm(instance=tool)

    return render(request, 'add_or_edit_tool.html', {'form': form})


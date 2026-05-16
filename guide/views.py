from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import GuideSection
from .forms import GuideSectionForm


def guide_page(request):
    sections = GuideSection.objects.all().order_by('emergency_type')
    return render(request, 'guide/guide.html', {'sections': sections})


@login_required
def guide_edit(request, pk):
    if request.user.role != 'authority':
        return redirect('guide_page')
    section = get_object_or_404(GuideSection, pk=pk)
    if request.method == 'POST':
        form = GuideSectionForm(request.POST, instance=section)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.last_updated_by = request.user
            obj.save()
            return redirect('guide_page')
    else:
        form = GuideSectionForm(instance=section)
    return render(request, 'guide/edit.html', {'form': form})


@login_required
def guide_create(request):
    if request.user.role != 'authority':
        return redirect('guide_page')
    if request.method == 'POST':
        form = GuideSectionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.last_updated_by = request.user
            obj.save()
            return redirect('guide_page')
    else:
        form = GuideSectionForm()
    return render(request, 'guide/edit.html', {'form': form})


from django.shortcuts import render

# Create your views here.

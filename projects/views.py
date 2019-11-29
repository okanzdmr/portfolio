from django.http import Http404
from django.shortcuts import render
from projects.models import Project, Technology
from django.shortcuts import get_object_or_404
from django.db.models import Count


def project_index(request):
    projects = Project.objects.all()
    technology=Technology.objects.prefetch_related('tech').all()
    k=Technology.objects.annotate(sth=Count("tech")).order_by("-sth")
    t=Technology.objects.all()


    context = {"projects": projects,"technology":technology,"t":t,"k":k}
    return render(request, "project_index.html", context)



def project_detail(request, slug):


        project = get_object_or_404(Project,slug=slug)
        context = {"project": project}

        return render(request, "project_detail.html", context)




def project_category(request, category):
    projects = Project.objects.filter(technology__title=category).order_by(
        "-published_date"
    )
    context = {"category": category, "projects": projects}
    return render(request, "project_category.html", context)

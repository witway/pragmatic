from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import RedirectView

from projectapp.models import Project
from subscribeapp.models import Subscription


class SubscriptionView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk':self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        # project_pk를 가진 Project를 찾는다, 만약 없다면 404 에러를 띄움
        user = self.request.user
        subscription = Subscription.objects.filter(user=user, project=project)

        if subscription.exists():
            subscription.delete()
            # 구독정보가 있으면 지우고
        else:
            Subscription(user=user, project=project).save()
            # 구독정보가 없다면 새로 만듦

        return super(SubscriptionView, self).get(request, *args, **kwargs)
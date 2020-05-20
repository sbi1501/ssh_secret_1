from django.shortcuts import render
from .models import Team, Secret
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TeamSerializer


def index(request):
    """View function for home page of site."""
    num_teams = Team.objects.all().count()
    num_secrets = Secret.objects.all().count()

    # todo может пригодиться фильтрация в дальнейшем, например, для вывода только своих групп и секретов
    # Available copies of books
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    return render(
        request,
        'index.html',
        context={
            'num_teams': num_teams,
            'num_secrets': num_secrets,
        },
    )


class TeamListView(generic.ListView):
    """Generic class-based view for a list of teams."""
    model = Team
    paginate_by = 10


class TeamListViewAPI(APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response({'teams': serializer.data})


class TeamDetailView(generic.DetailView):
    """Generic class-based detail view for a team."""
    model = Team


class SecretsByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing secrets to current user.
    """
    model = Secret
    template_name = 'storage/secret_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Secret.objects.filter(owner=self.request.user)


class SecretDetailView(generic.DetailView):
    """Generic class-based detail view for a secret."""
    model = Secret


class TeamsByUserListView(PermissionRequiredMixin, generic.ListView):
    """Generic class-based view listing all groups. Only visible to users with can_mark_returned permission."""
    model = Team
    permission_required = 'storage.can_manage_group'
    template_name = 'storage/my_team_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Team.objects.filter()  # select by executive

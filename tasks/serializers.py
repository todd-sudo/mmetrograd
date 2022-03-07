from rest_framework.serializers import ModelSerializer

from .models import Task
from mmetrograd.users.models import User


class TaskListSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"
        # fields = [
        #     "inn",
        #     "id",
        # ]


class TaskDetailSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"


class TenantListTaskSerializer(ModelSerializer):
    tasks = TaskListSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"
        # exclude = ["tenant"]


class TenantDetailTaskSerializer(ModelSerializer):
    tasks = TaskDetailSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"
        # exclude = ["tenant"]
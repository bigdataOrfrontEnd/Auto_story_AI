from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ModelUsageLog
from .serializers import ModelUsageLogSerializer


class ModelProviderViewSet(viewsets.ModelViewSet):
    
    """
    模型使用日志视图集
    提供模型使用日志的增删改查接口
    """
    queryset = ModelUsageLog.objects.all()
    serializer_class = ModelUsageLogSerializer

    def get_queryset(self):
        """
        根据请求参数过滤查询集
        支持按模型提供商ID和项目ID过滤
        """
        queryset = super().get_queryset()
        provider_id = self.request.query_params.get('provider_id')
        project_id = self.request.query_params.get('project_id')
        if provider_id:
            queryset = queryset.filter(model_provider_id=provider_id)
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        return queryset
class ModelUsageLogViewSet(viewsets.ModelViewSet):
    """
    模型使用日志视图集
    提供模型使用日志的增删改查接口
    """
    queryset = ModelUsageLog.objects.all()
    serializer_class = ModelUsageLogSerializer

    def get_queryset(self):
        """
        根据请求参数过滤查询集
        支持按模型提供商ID和项目ID过滤
        """
        queryset = super().get_queryset()
        provider_id = self.request.query_params.get('provider_id')
        project_id = self.request.query_params.get('project_id')
        if provider_id:
            queryset = queryset.filter(model_provider_id=provider_id)
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        return queryset
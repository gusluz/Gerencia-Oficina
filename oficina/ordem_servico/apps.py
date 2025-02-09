from django.apps import AppConfig


class OrdemServicoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ordem_servico'
    verbose_name = 'Cadastro de Ordem de Serviço'

    def ready(self):
        import ordem_servico.estoque
import random
from django_unicorn.components import UnicornView,QuerySetType

from render.forms import TaskForm
from render.models import Task

class TaskDynamicV2View(UnicornView):
    v = ['fazer','terminar','começar','concluir','mostar']
    a = ['o computador novo','o livro comprado recente','a cama','a arrumação do quarto']
    form_class = TaskForm
    tasks: QuerySetType[Task] = Task.objects.none()
    task: str = ""
    #task_up: str = "" #é ALTAMENTE recomendavel separar o campo de task do adicionar para o atulizar
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.atualizar_tasks() #atualzia assim que o componente é incluido no template

    def atualizar_tasks(self):
        self.tasks = Task.objects.all().reverse()

    def salvar_task(self):#metodo para salvar, necessario chamar no html
        if self.is_valid():#se o metodo de input atual (self) for valido
            Task.objects.create(titulo=self.task)#criação e salvamento da nova task
            self.atualizar_tasks()
            self.task = "" #limpar o input

    def deletar_todas_as_tasks(self):
        Task.objects.all().delete()
        self.tasks = Task.objects.none()

    def deletar_task(self,task_id):
        Task.objects.get(id=task_id).delete()
        self.tasks = self.tasks.exclude(id=task_id)
        self.atualizar_tasks()

    def adicionar_3_tasks_aleatorias(self):
        for i in range(3):
            new_task_random_titulo = "{} {}".format(random.choice(self.v),random.choice(self.a))
            Task.objects.create(titulo=new_task_random_titulo).save()
        self.atualizar_tasks()

    def atualizar_task(self,task_id):
        if len(self.task) < 2:
            self.task = ""
            pass #necessario para dar erro
        else:
            task_update = Task.objects.get(id=task_id)
            task_update.titulo = self.task
            task_update.save()
            self.task = "" #chamando dentro da funcao nao funciona
            self.atualizar_tasks()

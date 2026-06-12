from rest_framework import viewsets
from .models import Game, Screenshot
from .serializer import GameSerializer, ScreenshotSerializer
from rest_framework.exceptions import PermissionDenied

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def perform_create(self, serializer):
        # Na hora de salvar um jogo novo, carimba o usuário logado como o dono (added_by)
        serializer.save(added_by=self.request.user)

class ScreenshotViewSet(viewsets.ModelViewSet):
    serializer_class = ScreenshotSerializer

    def get_queryset(self):
        queryset = Screenshot.objects.all()
        
        # Permite que o app peça as fotos apenas do jogo atual
        game_id = self.request.query_params.get('game', None)
        if game_id is not None:
            queryset = queryset.filter(game_id=game_id)
            
        # A CORREÇÃO: Garante que a lista volte ordenada da foto mais antiga para a mais nova
        return queryset.order_by('upload_date')
    

    def perform_create(self, serializer):
        jogo = serializer.validated_data['game']

        print(f"--- DEBUG: Dono do Jogo: {jogo.added_by} | Usuário Logado: {self.request.user} ---")
        
        # Verifica se o ID do usuário que mandou a requisição é igual ao ID do criador do jogo
        if jogo.added_by != self.request.user:
            raise PermissionDenied("Acesso negado: Você só pode adicionar fotos aos jogos que você mesmo cadastrou.")
        
        serializer.save()

    # 2. O SEGURANÇA DA EXCLUSÃO:
    def perform_destroy(self, instance):
        # O 'instance' é a foto que está tentando ser apagada. Olhamos para o dono do jogo dela.
        if instance.game.added_by != self.request.user:
            raise PermissionDenied("Acesso negado: Você só pode apagar fotos dos jogos que você mesmo cadastrou.")
        
        instance.delete()

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import GameForm
from .models import Game

@login_required(login_url='/contas/login/')
def list_games_view(request):
    query = request.GET.get('query', '')
    if query:
        games = Game.objects.filter(title__icontains=query)
    else:
        games = Game.objects.all()
    return render(request, 'game/list_games.html', {'games': games, 'query': query})

@login_required(login_url='/contas/login/')
def add_game_view(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.added_by = request.user
            game.save()
            form.save_m2m()  # Necessário para salvar relacionamentos ManyToMany (genres/consoles)
            return redirect('game:list_games_view')
    else:
        form = GameForm()
    return render(request, 'game/add_game.html', {'form': form, 'action': 'Adicionar'})

@login_required(login_url='/contas/login/')
def edit_game_view(request, id_game):
    game = get_object_or_404(Game, id=id_game)
    # Restrição de edição para dono do cadastro ou equipe técnica
    if game.added_by != request.user and not request.user.is_staff:
        return render(request, '403.html', {'message': 'Você não tem permissão para editar este jogo.'}, status=403)
    
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game:list_games_view')
    else:
        form = GameForm(instance=game)
    return render(request, 'game/add_game.html', {'form': form, 'action': 'Editar'})

@login_required(login_url='/contas/login/')
def delete_game_view(request, id_game):
    game = get_object_or_404(Game, id=id_game)
    if game.added_by != request.user and not request.user.is_staff:
        return render(request, '403.html', {'message': 'Você não tem permissão para excluir este jogo.'}, status=403)
    game.delete()
    return redirect('game:list_games_view')
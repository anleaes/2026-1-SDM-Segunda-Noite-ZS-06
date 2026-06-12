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

from apps.review.models import Review
from apps.review.forms import ReviewForm
from .forms import ScreenshotForm
from .models import Screenshot

@login_required(login_url='/contas/login/')
def view_game_view(request, id_game):
    game = get_object_or_404(Game, id=id_game)
    screenshots = game.screenshots.all().order_by('upload_date')
    reviews = game.reviews.all().order_by('-review_date')
    
    review_form = ReviewForm()
    screenshot_form = ScreenshotForm()

    if request.method == 'POST':
        if 'submit_review' in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                # Substituição: apaga avaliação anterior do mesmo usuário para este jogo
                Review.objects.filter(user=request.user, game=game).delete()
                
                review = review_form.save(commit=False)
                review.user = request.user
                review.game = game
                review.save()
                return redirect('game:view_game_view', id_game=game.id)
        
        elif 'submit_screenshot' in request.POST:
            if game.added_by != request.user and not request.user.is_staff:
                return render(request, '403.html', {'message': 'Somente quem adicionou o jogo pode anexar capturas de tela.'}, status=403)
            
            screenshot_form = ScreenshotForm(request.POST, request.FILES)
            if screenshot_form.is_valid():
                screenshot = screenshot_form.save(commit=False)
                screenshot.game = game
                screenshot.save()
                return redirect('game:view_game_view', id_game=game.id)

    context = {
        'game': game,
        'screenshots': screenshots,
        'reviews': reviews,
        'review_form': review_form,
        'screenshot_form': screenshot_form,
    }
    return render(request, 'game/view_game.html', context)

@login_required(login_url='/contas/login/')
def delete_screenshot_view(request, id_screenshot):
    screenshot = get_object_or_404(Screenshot, id=id_screenshot)
    game_id = screenshot.game.id
    if screenshot.game.added_by != request.user and not request.user.is_staff:
        return render(request, '403.html', {'message': 'Acesso negado.'}, status=403)
    screenshot.delete()
    return redirect('game:view_game_view', id_game=game_id)

from apps.review.models import Review
from apps.review.forms import ReviewForm
from .forms import ScreenshotForm
from .models import Screenshot

@login_required(login_url='/contas/login/')
def view_game_view(request, id_game):
    game = get_object_or_404(Game, id=id_game)
    screenshots = game.screenshots.all().order_by('upload_date')
    reviews = game.reviews.all().order_by('-review_date')
    
    review_form = ReviewForm()
    screenshot_form = ScreenshotForm()

    if request.method == 'POST':
        if 'submit_review' in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                # Substituição: apaga avaliação anterior do mesmo usuário para este jogo
                Review.objects.filter(user=request.user, game=game).delete()
                
                review = review_form.save(commit=False)
                review.user = request.user
                review.game = game
                review.save()
                return redirect('game:view_game_view', id_game=game.id)
        
        elif 'submit_screenshot' in request.POST:
            if game.added_by != request.user and not request.user.is_staff:
                return render(request, '403.html', {'message': 'Somente quem adicionou o jogo pode anexar capturas de tela.'}, status=403)
            
            screenshot_form = ScreenshotForm(request.POST, request.FILES)
            if screenshot_form.is_valid():
                screenshot = screenshot_form.save(commit=False)
                screenshot.game = game
                screenshot.save()
                return redirect('game:view_game_view', id_game=game.id)

    context = {
        'game': game,
        'screenshots': screenshots,
        'reviews': reviews,
        'review_form': review_form,
        'screenshot_form': screenshot_form,
    }
    return render(request, 'game/view_game.html', context)

@login_required(login_url='/contas/login/')
def delete_screenshot_view(request, id_screenshot):
    screenshot = get_object_or_404(Screenshot, id=id_screenshot)
    game_id = screenshot.game.id
    if screenshot.game.added_by != request.user and not request.user.is_staff:
        return render(request, '403.html', {'message': 'Acesso negado.'}, status=403)
    screenshot.delete()
    return redirect('game:view_game_view', id_game=game_id)
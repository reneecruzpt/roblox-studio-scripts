import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Definições de cores
RED = (255, 0, 0)
GREEN = (0, 255, 51)
BLUE = (0, 0, 255)
ORANGE = (255, 123, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 0, 100)
LIGHT_BLUE = (80, 80, 255)

# Dimensões da tela
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

class Area:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def set_color(self, color):
        self.color = color

    def fill(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def set_outline(self, surface, outline_color):
        pygame.draw.rect(surface, outline_color, self.rect, 2)

    def collidepoint(self, point):
        return self.rect.collidepoint(point)

# Classe Label derivada da classe Area
class Label(Area):
    def __init__(self, x, y, width, height, color, text='', text_color=BLACK):
        super().__init__(x, y, width, height, color)
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.SysFont(None, 36)

    def set_text(self, text, text_color=BLACK):
        self.text = text
        self.text_color = text_color

    def draw(self, surface):
        self.fill(surface)
        self.set_outline(surface, BLACK)
        if self.text:
            text_surf = self.font.render(self.text, True, self.text_color)
            text_rect = text_surf.get_rect(center=self.rect.center)
            surface.blit(text_surf, text_rect)

# Configurações da tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fast Clicker Game")
clock = pygame.time.Clock()

# Função principal do jogo
def main():
    # Criação dos objetos Label
    cards = []
    start_x = 70
    start_y = 170
    card_width = 70
    card_height = 100
    gap = 30

    for i in range(4):
        card = Label(start_x + i * (card_width + gap), start_y, card_width, card_height, YELLOW)
        cards.append(card)

    # Variáveis do jogo
    click_display_time = 1000  # Tempo em milissegundos que o texto "CLICK!" será exibido
    score = 0
    start_time = pygame.time.get_ticks()
    game_over = False
    click_card_index = -1
    last_click_time = pygame.time.get_ticks()
    show_click_time = 0

    # Loop principal do jogo
    while True:
        screen.fill(WHITE)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouse_pos = event.pos
                for index, card in enumerate(cards):
                    if card.collidepoint(mouse_pos):
                        if index == click_card_index:
                            score += 1
                            card.set_color(GREEN)
                        else:
                            card.set_color(RED)
                        last_click_time = pygame.time.get_ticks()

        # Exibição do texto "CLICK!" aleatoriamente
        current_time = pygame.time.get_ticks()
        if current_time - last_click_time > click_display_time and not game_over:
            if click_card_index != -1 and current_time - show_click_time > click_display_time:
                cards[click_card_index].set_text('')
                cards[click_card_index].set_color(YELLOW)
            click_card_index = random.randint(0, 3)
            cards[click_card_index].set_text('CLICK!')
            show_click_time = pygame.time.get_ticks()

        # Atualização do status dos cartões
        for card in cards:
            card.draw(screen)

        # Verificação de vitória ou derrota
        elapsed_time = (current_time - start_time) / 1000  # Tempo em segundos
        if not game_over:
            if score >= 5 and elapsed_time <= 10:
                game_over = True
                win_label = Label(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 200, 100, LIGHT_GREEN, 'You Win!', BLACK)
                win_label.draw(screen)
            elif elapsed_time > 10:
                game_over = True
                lose_label = Label(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 200, 100, LIGHT_RED, 'You Lose!', BLACK)
                lose_label.draw(screen)

        # Exibição do tempo e da pontuação
        font = pygame.font.SysFont(None, 36)
        if not game_over:
            time_surf = font.render(f'Time: {int(elapsed_time)}', True, BLACK)
        else:
            time_surf = font.render(f'Time: {int(elapsed_time):.2f}', True, BLACK)
        score_surf = font.render(f'Score: {score}', True, BLACK)
        screen.blit(time_surf, (10, 10))
        screen.blit(score_surf, (10, 50))

        pygame.display.flip()
        clock.tick(40)

if __name__ == '__main__':
    main()

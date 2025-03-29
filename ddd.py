import pygame1

pygame.init()
size = WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode(size)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[1] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                pygame.draw.rect(screen, 'white',
                                 (self.left + self.cell_size * col,
                                  self.top + self.cell_size * row,
                                  self.cell_size, self.cell_size), width=self.board[row][col])

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        (self.on_click(cell))

    def get_cell(self, mouse_pos):
        x = (mouse_pos[0] - self.left) // self.cell_size
        y = (mouse_pos[1] - self.top) // self.cell_size
        return x, y

    def on_click(self, cell):
        x, y = cell
        if x not in range(0, self.width) or y not in range(0, self.height):
            return print(None)
        self.board[y][x] = int(not bool(self.board[y][x]))
        return print(x, y)


board = Board(10, 5)
board.render(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    clock = pygame.time.Clock()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

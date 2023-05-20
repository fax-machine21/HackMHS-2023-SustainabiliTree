import pygame, random, time


def get_font(size):
  return pygame.font.Font("Orbitron-Regular.ttf", size)


class BUttons2:

  def __init__(self, text, width, height, pos, elevation, screen, clock1):
    self.Clicks = 0
    self.cpsPower = 1
    self.elevation = elevation
    self.dynamicElevation = elevation
    self.originalY_pos = pos[1]
    self.screen = screen
    font = pygame.font.Font('Orbitron-Regular.ttf', 24)
    self.font = font
    self.clock1 = clock1

    self.topRectangle = pygame.Rect(pos, (width, height))
    self.topColor = "#1db336"
    self.bottomRect = pygame.Rect(pos, (width, height))
    self.bottomColor = "#248a35"
    self.textSurf = font.render(text, True, "#ffffff")
    self.textRect = self.textSurf.get_rect(center=self.topRectangle.center)

  def draw(self):
    self.topRectangle.y = self.originalY_pos - self.dynamicElevation
    self.textRect.center = self.topRectangle.center

    self.bottomRect.midtop = self.topRectangle.midtop
    self.bottomRect.height = self.topRectangle.height + self.dynamicElevation

    pygame.draw.rect(self.screen,
                     self.bottomColor,
                     self.bottomRect,
                     border_radius=12)
    pygame.draw.rect(self.screen,
                     self.topColor,
                     self.topRectangle,
                     border_radius=12)
    self.screen.blit(self.textSurf, self.textRect)

    # slider = Slider(300, 300, 200, 10, -5, 105, 50)

  def check_click(self):
    mouse_pos = pygame.mouse.get_pos()
    if self.topRectangle.collidepoint(mouse_pos):
      self.topColor = "#137824"
      if pygame.mouse.get_pressed()[0]:
        if pygame.MOUSEBUTTONDOWN:
          self.dynamicElevation = 0
          return True
      else:
        if self.dynamicElevation == 0:
          self.dynamicElevation = self.elevation
          return False

    else:
      self.dynamicElevation = self.elevation
      self.topColor = "#1db336"


class BUttons:

  def __init__(self, text, width, height, pos, elevation, screen, clock1):
    self.Clicks = 0
    self.cpsPower = 1
    self.elevation = elevation
    self.dynamicElevation = elevation
    self.originalY_pos = pos[1]
    self.screen = screen
    font = pygame.font.Font('Orbitron-Regular.ttf', 24)
    self.font = font
    self.clock1 = clock1

    self.topRectangle = pygame.Rect(pos, (width, height))
    self.topColor = "#1db336"
    self.bottomRect = pygame.Rect(pos, (width, height))
    self.bottomColor = "#248a35"
    self.textSurf = font.render(text, True, "#ffffff")
    self.textRect = self.textSurf.get_rect(center=self.topRectangle.center)

  def draw(self):
    self.topRectangle.y = self.originalY_pos - self.dynamicElevation
    self.textRect.center = self.topRectangle.center

    self.bottomRect.midtop = self.topRectangle.midtop
    self.bottomRect.height = self.topRectangle.height + self.dynamicElevation

    pygame.draw.rect(self.screen,
                     self.bottomColor,
                     self.bottomRect,
                     border_radius=12)
    pygame.draw.rect(self.screen,
                     self.topColor,
                     self.topRectangle,
                     border_radius=12)
    self.screen.blit(self.textSurf, self.textRect)

  def addScore(self):
    pass
    # self.clicks += self.clicksPerClicks
    # print(self.clicks)

    # slider = Slider(300, 300, 200, 10, -5, 105, 50)

  def check_click(self):
    mouse_pos = pygame.mouse.get_pos()
    if self.topRectangle.collidepoint(mouse_pos):
      self.topColor = "#137824"
      if pygame.mouse.get_pressed()[0]:
        if pygame.MOUSEBUTTONDOWN:
          self.dynamicElevation = 0
          return True
      else:
        if (self.dynamicElevation == 0):
          self.dynamicElevation = self.elevation
          self.Clicks += self.cpsPower
          return False

    else:
      self.dynamicElevation = self.elevation
      self.topColor = "#1db336"


class Slider:

  def __init__(self, x, y, width, height, min_value, max_value, value):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.min_value = min_value
    self.max_value = max_value
    self.value = value
    self.dragging = False

    self.bar_rect = pygame.Rect(x, y, width, height)
    self.knob_width = 20
    self.knob_height = 30
    self.knob_rect = pygame.Rect(
      x + (value - min_value) / float(max_value - min_value) * width -
      self.knob_width / 2, y - self.knob_height / 2, self.knob_width,
      self.knob_height)

  def update(self, events):
    # ALlows slider to be changed
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if self.knob_rect.collidepoint(event.pos):
          self.dragging = True
      elif event.type == pygame.MOUSEBUTTONUP:
        self.dragging = False
      elif event.type == pygame.MOUSEMOTION:
        if self.dragging:
          self.knob_rect.centerx = event.pos[0]
          if self.knob_rect.left < self.bar_rect.left:
            self.knob_rect.left = self.bar_rect.left
          elif self.knob_rect.right > self.bar_rect.right:
            self.knob_rect.right = self.bar_rect.right
          self.value = int(
            round((self.knob_rect.centerx - self.bar_rect.left) /
                  float(self.bar_rect.width) *
                  (self.max_value - self.min_value) + self.min_value))

  def draw(self, surface):
    #Draws Slider
    pygame.draw.rect(surface, (200, 200, 200), self.bar_rect)

    pygame.draw.rect(surface, (0, 255, 0), self.knob_rect)

    font = pygame.font.Font('Orbitron-Regular.ttf', 24)
    slider_text = font.render(str(self.value), True, (255, 255, 255))
    slider_text_rect = slider_text.get_rect()
    slider_text_rect.centerx = self.knob_rect.centerx
    slider_text_rect.bottom = self.knob_rect.top - 5
    surface.blit(slider_text, slider_text_rect)

  def get_value(self):
    #returns value of the slider
    return self.value

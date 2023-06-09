import math, random, time
# from loop import *
from tools import *
import pygame

pygame.init()

# Creating the screen

screen_width = 1280
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SustainabiliTree")
clock = pygame.time.Clock()

# logic
cpsPower = 0
greenCoin = 0
gcps = 1
upgrades = {
  'Sapling': 15,
  'Plant': 50,
  'Bush': 100,
  'Tree': 1000,
  'Forest': 10000
}  # name:price
upgradesAmount = {
  'Sapling': 0,
  'Plant': 0,
  'Bush': 0,
  'Tree': 0,
  'Forest': 0
}  # name:amount
gc_p_s = {
  'Sapling': 1,
  'Plant': 15,
  'Bush': 50,
  'Tree': 100,
  'Forest': 500
}  # name:cps
# reforestationDrones-Max Loss-40%, Max Gain 50%,
# solarPanels-Max Loss-20%,Max Gain-20%,
# electricVehicles = 0 Max Loss-30%, Max Gain 30%,
# renewableFuel = 0  Max Loss-25%   max Gain 25%,
# carbonCapture = 0   Max Loss 40%, Max gain 80%,

investments = {
  'Solar Panels': 5000,
  'Reforestation Drones': 5000,
  'Electric Vehicles': 5000,
  'Renewable Fuels': 5000,
  'Carbon Capture': 5000
}
risk_reward = {
  'Solar Panels': [-0.2, 1.2],
  'Reforestation Drones': [-0.5, 1.5],
  'Electric Vehicles': [-0.3, 1.3],
  'Renewable Fuels': [-0.2, 1.3],
  'Carbon Capture': [-0.4, 1.8]
}


def buyInvestment(index):
  global greenCoin, gcps, upgrades, gc_p_s
  global investments, risk_reward
  if greenCoin >= 5000:  #5k
    greenCoin -= 5000  #5k
    start_button.Clicks -= 5000  #5k
    updateTitleText()
    riskreward = random.choice([0, 1])
    result = 5000 * risk_reward[index][riskreward]
    time.sleep(1)
    greenCoin += result
    start_button.Clicks += result
    updateTitleText()
    if result > 5000:
      print('Your investment paid off and you gained ' + str(result) +
            ' coins!')
    elif result < 5000:
      print('Your investment failed and you lost ' + str(5000 - result) +
            ' coins!')
    else:
      print('Your investment did absolutely nothing...')
  else:
    print("You don't have enough money to make this investment! (You have " +
          str(greenCoin) + " coins)")


# buyInvestment('Reforestation Drones')


def buyUpgrade(index):
  global greenCoin, gcps, upgrades, gc_p_s, upgradesAmount, TITLE_TEXT

  price = upgrades[index]

  if greenCoin >= price:
    newPrice = math.floor(price**1.07)
    upgrades[index] = newPrice
    gcps += gc_p_s[index]
    greenCoin -= price
    start_button.Clicks -= price
    print('Successful purchase!')
    updateTitleText()
    upgradesAmount[index] += 1
    start_button.cpsPower = gcps

  else:
    print("You don't have enough money to complete this purchase. (You have " +
          str(greenCoin) + " coins)")


# buyUpgrade('Sapling')

# pygame
start_button_width = 275
start_button_height = 50
start_button_x = (screen_width - start_button_width) / 2
start_button_y = ((screen_height - start_button_height) / 2) + 250
start_button_pos = (start_button_x, start_button_y)
start_button_elevation = 10
start_button = BUttons("Click!", start_button_width, start_button_height,
                       start_button_pos, start_button_elevation, screen, clock)

upgrade_button_width = 275
upgrade_button_height = 75
upgrade_button_x = ((screen_width - upgrade_button_width) / 2) + 470
upgrade_button_y = ((screen_height - upgrade_button_height) / 2) - 300
upgrade_button_pos = (upgrade_button_x, upgrade_button_y)
upgrade_button_elevation = 10
upgrade_button = BUttons("upgrade", upgrade_button_width,
                         upgrade_button_height, upgrade_button_pos,
                         upgrade_button_elevation, screen, clock)

upgrade1_button_width = 275
upgrade1_button_height = 100
upgrade1_button_x = (screen_width - upgrade1_button_width) / 2 + 485
upgrade1_button_y = ((screen_height - upgrade1_button_height) / 2) - 185
upgrade1_button_pos = (upgrade_button_x, upgrade1_button_y)
upgrade1_button_elevation = 10
upgrade1_button = BUttons("upgrade1", upgrade1_button_width,
                          upgrade1_button_height, upgrade1_button_pos,
                          upgrade1_button_elevation, screen, clock)

upgrade2_button_width = 275
upgrade2_button_height = 100
upgrade2_button_x = (screen_width - upgrade2_button_width) / 2 + 470
upgrade2_button_y = ((screen_height - upgrade2_button_height) / 2) - 70
upgrade2_button_pos = (upgrade2_button_x, upgrade2_button_y)
upgrade2_button_elevation = 10
upgrade2_button = BUttons("upgrade2", upgrade2_button_width,
                          upgrade2_button_height, upgrade2_button_pos,
                          upgrade2_button_elevation, screen, clock)

upgrade3_button_width = 275
upgrade3_button_height = 75
upgrade3_button_x = (screen_width - upgrade3_button_width) / 2 + 500
upgrade3_button_y = ((screen_height - upgrade3_button_height) / 2) + 35
upgrade3_button_pos = (upgrade2_button_x, upgrade3_button_y)
upgrade3_button_elevation = 10
upgrade3_button = BUttons("upgrade3", upgrade3_button_width,
                          upgrade3_button_height, upgrade3_button_pos,
                          upgrade3_button_elevation, screen, clock)

upgrade4_button_width = 275
upgrade4_button_height = 75
upgrade4_button_x = (screen_width - upgrade4_button_width) / 2 + 485
upgrade4_button_y = ((screen_height - upgrade4_button_height) / 2) + 150
upgrade4_button_pos = (upgrade4_button_x, upgrade4_button_y)
upgrade4_button_elevation = 10
upgrade4_button = BUttons("upgrade3", upgrade4_button_width,
                          upgrade4_button_height, upgrade4_button_pos,
                          upgrade4_button_elevation, screen, clock)

investment_button_width = 245
investment_button_height = 110
investment_button_x = ((screen_width - investment_button_width) / 2) - 490
investment_button_y = ((screen_height - investment_button_height) / 2) - 295
investment_button_pos = (investment_button_x, investment_button_y)
investment_button_elevation = 10
investment_button = BUttons("investment", investment_button_width,
                            investment_button_height, investment_button_pos,
                            investment_button_elevation, screen, clock)

investment1_button_width = 245
investment1_button_height = 95
investment1_button_x = (screen_width - investment1_button_width) / 2 + 500
investment1_button_y = ((screen_height - investment1_button_height) / 2) - 170
investment1_button_pos = (investment_button_x, investment1_button_y)
investment1_button_elevation = 10
investment1_button = BUttons("investment1", investment1_button_width,
                             investment1_button_height, investment1_button_pos,
                             investment1_button_elevation, screen, clock)

investment2_button_width = 250
investment2_button_height = 95
investment2_button_x = (screen_width - investment2_button_width) / 2 - 495
investment2_button_y = ((screen_height - investment2_button_height) / 2) - 50
investment2_button_pos = (investment2_button_x, investment2_button_y)
investment2_button_elevation = 10
investment2_button = BUttons("upgrade2", investment2_button_width,
                             investment2_button_height, investment2_button_pos,
                             investment2_button_elevation, screen, clock)

investment3_button_width = 250
investment3_button_height = 100
investment3_button_x = (screen_width - investment3_button_width) / 2 - 500
investment3_button_y = ((screen_height - investment3_button_height) / 2) + 65
investment3_button_pos = (investment2_button_x, investment3_button_y)
investment3_button_elevation = 10
investment3_button = BUttons("investment3", investment3_button_width,
                             investment3_button_height, investment3_button_pos,
                             investment3_button_elevation, screen, clock)

investment4_button_width = 250
investment4_button_height = 100
investment4_button_x = (screen_width - investment4_button_width) / 2 - 490
investment4_button_y = ((screen_height - investment4_button_height) / 2) + 185
investment4_button_pos = (investment4_button_x, investment4_button_y)
investment4_button_elevation = 10
investment4_button = BUttons("investment4", investment4_button_width,
                             investment4_button_height, investment4_button_pos,
                             investment4_button_elevation, screen, clock)

bg = pygame.image.load('bg.png')
bg = pygame.transform.scale(bg, (screen_width, screen_height))
bg1 = pygame.image.load('bg1.png')
bg1 = pygame.transform.scale(bg1, (screen_width, screen_height))
bg2 = pygame.image.load('bg2.png')
bg2 = pygame.transform.scale(bg2, (screen_width, screen_height))
bg3 = pygame.image.load('bg3.png')
bg3 = pygame.transform.scale(bg3, (screen_width, screen_height))
bg4 = pygame.image.load('bg4.png')
bg4 = pygame.transform.scale(bg4, (screen_width, screen_height))
bg5 = pygame.image.load('bg5.png')
bg5 = pygame.transform.scale(bg5, (screen_width, screen_height))

logo_coords = (15, 623)
running = True
upgradeCounter = 0
upgrade1Counter = 0
upgrade2Counter = 0
upgrade3Counter = 0
upgrade4Counter = 0

CRED_TEXT = get_font(25).render(str("Made by: JH, RS, DK, RC"), True,
                                "#00ff00")
CRED_RECT = CRED_TEXT.get_rect(center=((screen_width // 2), 50))
CRED_RECT.center = (screen_width // 2, (screen_height // 2) + 335)

while running:
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      running = False

  screen.fill("#000000")

  clicks = start_button.Clicks
  greenCoin = clicks

  upgrade_button.draw()
  upgrade1_button.draw()
  upgrade2_button.draw()
  upgrade3_button.draw()
  upgrade4_button.draw()

  investment_button.draw()
  investment1_button.draw()
  investment2_button.draw()
  investment3_button.draw()
  investment4_button.draw()

  if upgradesAmount['Forest'] > 0:
    screen.blit(bg5, (0, 0))
    logo_coords = (28, 618)
  elif upgradesAmount['Tree'] > 0:
    screen.blit(bg4, (0, 0))
    logo_coords = (25, 623)
  elif upgradesAmount['Bush'] > 0:
    screen.blit(bg3, (0, 0))
    logo_coords = (25, 618)
  elif upgradesAmount['Plant'] > 0:
    screen.blit(bg2, (0, 0))
    logo_coords = (25, 618)
  elif upgradesAmount['Sapling'] > 0:
    screen.blit(bg1, (0, 0))
    logo_coords = (25, 618)
  else:
    screen.blit(bg, (0, 0))
    logo_coords = (15, 623)

  logoicon = pygame.image.load('logo.png')
  logoicon = pygame.transform.scale(logoicon, (250, 105))
  screen.blit(logoicon, logo_coords)

  def updateTitleText():
    global greenCoin, clicks, TITLE_TEXT
    clicks = greenCoin
    TITLE_TEXT = get_font(70).render(str(int(greenCoin)), True, "#ffffff")
    TITLE_RECT = TITLE_TEXT.get_rect(center=((screen_width // 2), 50))
    TITLE_RECT.center = (screen_width // 2, (screen_height // 2) - 275)
    screen.blit(TITLE_TEXT, TITLE_RECT)

  start_button.draw()
  updateTitleText()

  screen.blit(CRED_TEXT, CRED_RECT)

  GCPS_TEXT = get_font(35).render(
    str(gcps) + ' coins per click', True, '#ffffff')
  GCPS_RECT = GCPS_TEXT.get_rect(center=((screen_width // 2), 50))
  GCPS_RECT.center = (screen_width // 2, (screen_height // 2) - 325)
  screen.blit(GCPS_TEXT, GCPS_RECT)

  # price texts
  upgradeOne_TEXT = get_font(15).render(str(upgrades['Sapling']), True,
                                        '#000000')
  upgradeOne_RECT = upgradeOne_TEXT.get_rect(center=((screen_width // 2), 50))
  upgradeOne_RECT.center = (screen_width - 160, 94)
  screen.blit(upgradeOne_TEXT, upgradeOne_RECT)

  upgradeTwo_TEXT = get_font(15).render(str(upgrades['Plant']), True,
                                        '#000000')
  upgradeTwo_RECT = upgradeTwo_TEXT.get_rect(center=((screen_width // 2), 50))
  upgradeTwo_RECT.center = (screen_width - 160, 208)
  screen.blit(upgradeTwo_TEXT, upgradeTwo_RECT)

  upgradeThree_TEXT = get_font(15).render(str(upgrades['Bush']), True,
                                          '#000000')
  upgradeThree_RECT = upgradeThree_TEXT.get_rect(center=((screen_width // 2),
                                                         50))
  upgradeThree_RECT.center = (screen_width - 165, 316)
  screen.blit(upgradeThree_TEXT, upgradeThree_RECT)

  upgradeFour_TEXT = get_font(15).render(str(upgrades['Tree']), True,
                                         '#000000')
  upgradeFour_RECT = upgradeFour_TEXT.get_rect(center=((screen_width // 2),
                                                       50))
  upgradeFour_RECT.center = (screen_width - 160, 425)
  screen.blit(upgradeFour_TEXT, upgradeFour_RECT)

  upgradeFive_TEXT = get_font(15).render(str(upgrades['Forest']), True,
                                         '#000000')
  upgradeFive_RECT = upgradeFive_TEXT.get_rect(center=((screen_width // 2),
                                                       50))
  upgradeFive_RECT.center = (screen_width - 160, 535)
  screen.blit(upgradeFive_TEXT, upgradeFive_RECT)

  if start_button.check_click():
    continue

  if upgrade_button.check_click():
    buyUpgrade('Sapling')
    upgradeCounter += 1

  if upgrade1_button.check_click():
    buyUpgrade('Plant')
    upgrade1Counter += 1

  if upgrade2_button.check_click():
    buyUpgrade('Bush')
    upgrade2Counter += 1

  if upgrade3_button.check_click():
    buyUpgrade('Tree')
    upgrade3Counter += 1

  if upgrade4_button.check_click():
    buyUpgrade('Forest')
    upgrade4Counter += 1

  if investment_button.check_click():
    buyInvestment('Solar Panels')
    updateTitleText()
  if investment1_button.check_click():
    buyInvestment('Reforestation Drones')
    updateTitleText()
  if investment2_button.check_click():
    buyInvestment('Electric Vehicles')
    updateTitleText()
  if investment3_button.check_click():
    buyInvestment('Renewable Fuels')
    updateTitleText()
  if investment4_button.check_click():
    buyInvestment('Carbon Capture')
    updateTitleText()
  else:
    updateTitleText()

  pygame.display.update()

  clock.tick(60)

pygame.quit()

import pygame
import vgamepad as vg
import time

# 初始化
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("没有检测到手柄")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print("检测到手柄:", joystick.get_name())

# 虚拟手柄
gamepad = vg.VX360Gamepad()

toggle = False
last_share_state = False

last_press_time = 0
press_interval = 1.0  # 每1秒按一次

def press_a():
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
    time.sleep(0.05)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()

print("按 Share 开关自动剧情")

while True:
    pygame.event.pump()

    # Share = 9
    share_pressed = joystick.get_button(4)

    # 边沿检测
    if share_pressed and not last_share_state:
        toggle = not toggle
        print("\r自动点击: {}".format("开启" if toggle else "关闭"), end="", flush=True)
        time.sleep(0.2)  # 防抖

    last_share_state = share_pressed

    # 独立计时逻辑
    if toggle:
        now = time.time()
        if now - last_press_time >= press_interval:
            press_a()
            last_press_time = now

    time.sleep(0.005)
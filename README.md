# GenshinImpactDualSenseAutoSkip
Genshin Impact Dual Sense controller auto skip Python script


## 功能
- 创建 Xbox 360 虚拟手柄
- 按 Share 键开启/关闭自动模式
- 自动模式下每 1 秒 模拟按下一次 A 键
- 不影响实体手柄的其它按键操作


## 依赖
安装所需库：
`pip install pygame vgamepad`
另外需要安装 ViGEmBus 驱动（vgamepad 依赖），否则无法创建虚拟 Xbox 手柄。

默认点击间隔为 1 秒，可修改代码中的：
`press_interval = 1.0`
例如：
`press_interval = 0.5`
表示每 0.5 秒按一次 A 键。


[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
[![LICENSE](https://badges.frapsoft.com/os/mit/mit.svg)](https://opensource.org/licenses/mit-license.php)

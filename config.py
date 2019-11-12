import os
import logging.handlers

MP_BASE_URL = "http://ttmp.research.itcast.cn/"
# 找到当前文件的绝对路径
# os.path.abspath(__file__)
# 获取根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print("BASE_DIR" + BASE_DIR)


# 日志配置初始化

def init_log_config():
    # 创建日志器(组件入口)
    logger = logging.getLogger()
    # 定义文件级别
    logger.setLevel(logging.INFO)

    # 创建处理器（可以把日志存放在不同位置）

    # 控制台处理器
    sh = logging.StreamHandler()

    #  最普通的文件处理器()：会把日志一直输入到同一个文件里，不会自动的去拆分
    #  ：缺点，长时间积累的日志文件过大，不方便定位
    #  logging.FileHandler

    # 日志绝对路径
    log_file = BASE_DIR + "/log/hmtt.log"
    # 文件处理器：根据文件拆分的处理器
    # when:可以根据设置参数天/小时/分/秒/去区分，interval可以设置是几天/几小时/几分钟/几秒
    # backupCount:设置备份，0代表不会过期，页可以根据需要设置几天后清除
    fh = logging.handlers.TimedRotatingFileHandler(log_file, when="midnight", interval=1, backupCount=7,
                                                   encoding="utf-8")

    # 创建格式器
    fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)
    # 把格式化器添加到处理器中
    # 两个处理器使用同一种格式化器，也可以一个处理器使用一个格式化器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 把处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)


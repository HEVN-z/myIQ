import mmjs as mm
from threading import Thread
def thread_test():
    # print(mm.get_base_amount())
    # print(mm.get_order_amount())
    # print(mm.get_total_amount())
    # print(mm.get_today_profit())
    # print(mm.get_profit_target())
    # print(mm.get_martingale_level())
    # print(mm.get_martingale_max_level())
    # print(mm.get_martingale_min_level())
    # print(mm.get_martingale_multiplier())
    # print(mm.get_anti_martingale_multiplier())
    # print(mm.get_target_goal())
    # print(mm.get_target_loss())
    mm.set_base_amount(100)
    mm.set_order_amount(100)
    mm.set_total_amount(100)
    mm.set_today_profit(100)
    mm.set_profit_target(100)
    mm.set_martingale_level(100)
    mm.set_martingale_max_level(100)
    mm.set_martingale_min_level(100)
    mm.set_martingale_multiplier(100)
    mm.set_anti_martingale_multiplier(100)
    mm.set_target_goal(100)
    mm.set_target_loss(100)

Thread(target=thread_test).start()
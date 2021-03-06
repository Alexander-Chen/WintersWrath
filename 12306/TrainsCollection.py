from prettytable import PrettyTable
from colorama import init, Fore

class TrainsCollection:
    header = '车次 车站 时间 历时 一等 二等 软卧 硬卧 硬座 无座 控制信息 购票'.split()

    def __init__(self, available_trains, options):
        """查询到的火车班次集合

        :param available_trains: 一个列表, 包含可获得的火车班次, 每个火车班次是一个字典
        :param options: 查询的选项, 如高铁, 动车, etc...
        """
        self.available_trains = available_trains
        self.options = options

    def _get_duration(self, raw_train):
        duration = raw_train.get('queryLeftNewDTO').get('lishi').replace(':', '小时') + '分'
        if duration.startswith('00'):
            return duration[4:]
        if duration.startswith('0'):
            return duration[1:]
        return duration

    @property
    def trains(self):
        for raw_train in self.available_trains:
            train_no = raw_train['queryLeftNewDTO']['station_train_code']
            initial = train_no[0].lower()
            contorl_flag = raw_train['queryLeftNewDTO']['controlled_train_message']
            buy_flag = raw_train['queryLeftNewDTO']['canWebBuy']

            if "正常" in contorl_flag:
                contorl_flag = Fore.GREEN + '正常' + Fore.RESET
            else:
                contorl_flag = Fore.RED + '受控' + Fore.RESET

            if "Y" in buy_flag:
                buy_flag = Fore.GREEN + '可购票' + Fore.RESET
            else:
                buy_flag = Fore.RED + '不可购票' + Fore.RESET

            if not self.options or initial in self.options:
                train = [
                    train_no,        
                    '\n'.join([Fore.RED + raw_train['queryLeftNewDTO']['from_station_name'] + Fore.RESET, Fore.BLUE + raw_train['queryLeftNewDTO']['to_station_name'] + Fore.RESET]),
                    '\n'.join([Fore.RED + raw_train['queryLeftNewDTO']['start_time'] + Fore.RESET,Fore.BLUE + raw_train['queryLeftNewDTO']['arrive_time'] + Fore.RESET]),
                    self._get_duration(raw_train),
                    raw_train['queryLeftNewDTO']['zy_num'],
                    raw_train['queryLeftNewDTO']['ze_num'],
                    raw_train['queryLeftNewDTO']['rw_num'],
                    raw_train['queryLeftNewDTO']['yw_num'],
                    raw_train['queryLeftNewDTO']['yz_num'],
                    raw_train['queryLeftNewDTO']['wz_num'],
                    contorl_flag,
                    buy_flag
                ]
                yield train

    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)

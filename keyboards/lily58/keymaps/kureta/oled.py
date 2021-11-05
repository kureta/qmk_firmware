from time import sleep

import GPUtil as GPUtil
import hid
import psutil as psutil

VENDOR_ID = 0x04d8
PRODUCT_ID = 0xeb2d
USAGE_PAGE = 0xff60
USAGE = 0x61

CLEAR = 4
WRITE = 3


def bar(x: float) -> str:
    x = int(x / 10.)
    return ''.join(x * ['='])


def memory() -> str:
    return f'MEM: {bar(psutil.virtual_memory()[2])}'


def cpu() -> str:
    return f'CPU: {bar(psutil.cpu_percent(interval=1))}'


def disk() -> str:
    return f'DISK:{bar(psutil.disk_usage("/home").percent)}'


def gpu() -> str:
    return f'GPU: {bar(GPUtil.getGPUs()[0].load * 100)}'


def gpu_mem() -> str:
    return f'GMEM:{bar(GPUtil.getGPUs()[0].memoryUtil * 100)}'


def predicate(d: dict) -> bool:
    vid = d['vendor_id'] == VENDOR_ID
    pid = d['product_id'] == PRODUCT_ID
    up = d['usage_page'] == USAGE_PAGE
    u = d['usage'] == USAGE

    return vid and pid and up and u


def message_to_byte(message: str) -> bytes:
    message = bytes(message, 'ascii')
    size = bytes([len(message)])
    size = size + (4 - len(size)) * bytes([0])

    return size + message


def prepare_payload(command: int, message: str = '') -> bytes:
    command = bytes([0, command])
    message = message_to_byte(message)
    payload = command + message
    padding = (64 - (len(payload) % 64)) * bytes([0])
    payload += padding

    return payload


class Dummy:
    def __init__(self):
        path = [d['path'] for d in hid.enumerate() if predicate(d)][0]
        self.device = hid.Device(path=path)
        self.stat_funcs = [cpu, memory]

        self.clear()

    def __send_command(self, command: int, message: str = ''):
        payload = prepare_payload(command, message)
        self.device.write(payload)

    def send_message(self, message: str):
        self.__send_command(WRITE, message)

    def clear(self):
        self.__send_command(CLEAR)

    def stats(self):
        lines = '\n'.join([fn() for fn in self.stat_funcs])
        self.send_message(lines)

    def run(self, refresh_rate=1.0):
        period = 1. / refresh_rate
        while True:
            self.stats()
            sleep(period)


def main():
    dummy = Dummy()
    dummy.run()


if __name__ == '__main__':
    main()

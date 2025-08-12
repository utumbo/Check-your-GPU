import GPUtil

gpus = GPUtil.getGPUs()
def gpu_info():
    for gpu in gpus:
        print(f'ID: {gpu.id}, Name: {gpu.name}')
        print(f'GPU Load: {gpu.load}') # загрузка gpu в процентах
        print(f'GPU memoty Total: {gpu.memoryTotal}, GPU Temp: {gpu.temperature}')
        print(f'GPU memory: {gpu.memoryUsed}, GPU free: {gpu.memoryFree}')

if __name__ == "__main__":
    print(gpu_info())


# Загрузка GPU — проценте использования вычислительных ресурсов GPU
# Использование памяти GPU — объёме памяти, занятой процессами.
# Частота GPU — тактовой частоте графического процессора.
# Температура GPU — температуре графического чипа.
# Идентификация GPU — модели и производителя GPU.
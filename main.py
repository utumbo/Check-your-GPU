import GPUtil

def gpu_info():

    gpus = GPUtil.getGPUs()
    result = []

    for gpu in gpus:
        gpu_data = (
            f'ID: {gpu.id}, Name: {gpu.name}'
            f'GPU Load: {gpu.load}' # загрузка gpu в процентах
            f'GPU memoty Total: {gpu.memoryTotal}, GPU Temp: {gpu.temperature}'
            f'GPU memory: {gpu.memoryUsed}, GPU free: {gpu.memoryFree}'
        )
        result.append(gpu_data)
    return result
        

if __name__ == "__main__":
    # Получаем данные
    gpu_data = gpu_info()
    
    # Выводим информацию
    print(gpu_data)

    input("Press Enter to exit...")


# Загрузка GPU — проценте использования вычислительных ресурсов GPU
# Использование памяти GPU — объёме памяти, занятой процессами.
# Частота GPU — тактовой частоте графического процессора.
# Температура GPU — температуре графического чипа.
# Идентификация GPU — модели и производителя GPU.
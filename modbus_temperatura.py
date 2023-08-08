from pymodbus.client import ModbusTcpClient
import time
from random import randint


def bitString(boolList):
    return "".join(["1" if x else "0" for x in boolList])


client = ModbusTcpClient(
    host="192.168.0.216", port=14502, unit_id=1, retry_on_empty=True
)
client.connect()

time.sleep(1)

result_coils = client.read_coils(0, 16)
result_discrete_inputs = client.read_discrete_inputs(0, 16)
result_holding_registers = client.read_holding_registers(0, 3)
result_input_registers = client.read_input_registers(0, 3)

print("Coils:", bitString(result_coils.bits))
print("Discrete_inputs:", bitString(result_discrete_inputs.bits))
print("Holding_registers:", result_holding_registers.registers)
print("Input_registers", result_input_registers.registers)
print()

time.sleep(1)

TARGET_TEMPERATURE = result_input_registers.registers[0]
TEMPERATURE = TARGET_TEMPERATURE + randint(-50, 50)
print("Target temperature:", TARGET_TEMPERATURE)
print("Random temperature:", TEMPERATURE)
print()

client.write_register(0, TEMPERATURE)
client.close()

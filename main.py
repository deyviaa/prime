import matplotlib.pyplot as plt
import numpy as np

# constants
k = 1.380649e-23  # Boltzmann constant in J/K
q = 1.602176634e-19  # Elementary charge in C
n = 1.0  # Ideality factor
i_L = 0.5  # Light generated current (A)
i_0 = 1e-10  # Dark saturation current (A)
N = 100
voltage = np.linspace(0, 0.577, N)  # Voltage range from 0 V to 577 mV


def calculate_current(temperature, irradiance_factor):
    current_array = []

    # using diode law to calculate current values while varying voltage
    for i in voltage:
        current_val = (irradiance_factor * i_L) - (
            i_0 * (np.exp((q * i) / (n * k * temperature)) - 1)
        )
        current_array = np.append(current_array, current_val)

    return current_array


def main():
    print("Hello from prime!")

    # gathering parameters from user input
    t = input("Enter Temperature (in Kelvin) : ")
    t = float(t)
    print(t, "K")

    i_f = input("Enter Irradiance (Multiplication Factor): ")
    i_f = float(i_f)
    print("x", i_f, "W/m^2")

    current = calculate_current(t, i_f)
    plt.title("I-V Curve")
    plt.plot(voltage, current)
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (A)")
    plt.show()


if __name__ == "__main__":
    main()

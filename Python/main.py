import math

# RK2 & RK4 to solve OMID model problem

# start point
delta_0 = 0
omega_0 = 0

# power system parameters
Omega_b = 314.16

t_0 = 0.5

e = v = P_M = 1

x_eq = 0.5

P_E = e * v / x_eq

H = 8

# step size
delta_t = 0.25

# results RK
delta_list_RK4 = []
omega_list_RK4 = []

delta_list_RK2 = []
omega_list_RK2 = []

# RK4
for i in range(0, 500):

    # simulate disturbance
    if ( i >= 200 ):
        x_eq = 0.6
        P_E = e * v / x_eq

    K_1 = omega_0 * Omega_b * delta_t

    I_1 = ((P_M - P_E * math.sin(delta_0)) / (2 * H)) * delta_t

    K_2 = (omega_0 + I_1 / 2) * Omega_b * delta_t

    I_2 = ((P_M - P_E * math.sin(delta_0 + K_1 / 2)) / (2 * H)) * delta_t

    K_3 = (omega_0 + I_2 / 2) * Omega_b * delta_t

    I_3 = ((P_M - P_E * math.sin(delta_0 + K_2 / 2)) / (2 * H)) * delta_t

    K_4 = (omega_0 + I_3) * Omega_b * delta_t

    I_4 = ((P_M - P_E * math.sin(delta_0 + K_3)) / (2 * H)) * delta_t

    delta_1 = delta_0 + (K_1 + 2 * K_2 + 2 * K_3 + K_4) / 6

    omega_1 = omega_0 + (I_1 + 2 * I_2 + 2 * I_3 + I_4) / 6

    delta_0 = delta_1
    omega_0 = omega_1

    delta_list_RK4.append(delta_1)
    omega_list_RK4.append(omega_1)

# reset
# start point
delta_0 = 0
omega_0 = 0

# power system parameters
Omega_b = 314.16

t_0 = 0.5

e = v = P_M = 1

x_eq = 0.5

P_E = e * v / x_eq

H = 8

# step size
delta_t = 0.25

# RK2
for i in range(0, 500):

    # simulate disturbance
    if ( i >= 240 ):
        x_eq = 0.6
        P_E = e * v / x_eq

    K_1 = omega_0 * Omega_b * delta_t

    I_1 = ((P_M - P_E * math.sin(delta_0)) / (2 * H)) * delta_t

    K_2 = (omega_0 + I_1) * Omega_b * delta_t

    I_2 = ((P_M - P_E * math.sin(delta_0 + K_2)) / (2 * H)) * delta_t

    delta_1 = delta_0 + (K_1 + K_2) / 2

    omega_1 = omega_0 + (I_1 + I_2) / 2

    delta_0 = delta_1
    omega_0 = omega_1

    delta_list_RK2.append(delta_1)
    omega_list_RK2.append(omega_1)


import matplotlib.pyplot as plt
x = [_ for _ in range(0, 500)]

fig = plt.figure(figsize = (12, 6))

ax1 = fig.add_subplot(221)
plt.plot(x, delta_list_RK4)
ax1.set_xlabel('time')
ax1.set_ylabel('delta')
ax1.set_title('RK4')

ax2 = fig.add_subplot(222)
plt.plot(x, omega_list_RK4)
ax2.set_xlabel('time')
ax2.set_ylabel('omega')
ax2.set_title('RK4')

ax3 = fig.add_subplot(223)
plt.plot(x, delta_list_RK2)
ax3.set_xlabel('time')
ax3.set_ylabel('delta')
ax3.set_title('RK2')

ax4 = fig.add_subplot(224)
plt.plot(x, omega_list_RK2)
ax4.set_xlabel('time')
ax4.set_ylabel('omega')
ax4.set_title('RK2')

plt.show()

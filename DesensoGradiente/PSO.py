import sys
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

class PSO:
    def __init__(self, particles, velocities, fitness_function,
                 w=0.8, c_1=1, c_2=1, max_iter=100, auto_coef=True):
        self.particles = particles
        self.velocities = velocities
        self.fitness_function = fitness_function
        self.N = len(self.particles)
        self.w = w
        self.c_1 = c_1
        self.c_2 = c_2
        self.auto_coef = auto_coef
        self.max_iter = max_iter
        self.p_bests = self.particles
        self.p_bests_values = [self.fitness_function(i) for i in self.particles]
        self.g_best = self.p_bests[0]
        self.g_best_value = self.p_bests_values[0]
        self.update_bests()
        self.iter = 0
        self.is_running = True
        self.update_coef()
    def __str__(self):
        return f'[{self.iter}/{self.max_iter}] $w$:{self.w:.3f} - $c_1$:{self.c_1:.3f} - $c_2$:{self.c_2:.3f}'
    def next(self):
        if self.iter > 0:
            self.move_particles()
            self.update_bests()
            self.update_coef()
        self.iter += 1
        self.is_running = self.is_running and self.iter < self.max_iter
        return self.is_running
    def update_coef(self):
        if self.auto_coef:
            t = self.iter
            n = self.max_iter
            self.w = (0.4/n**2) * (t - n) ** 2 + 0.4
            self.c_1 = -3 * t / n + 3.5
            self.c_2 =  3 * t / n + 0.5
    def move_particles(self):
        # add inertia
        new_velocities = self.w * self.velocities
        # add cognitive component
        r_1 = np.random.random(self.N)
        r_1 = np.tile(r_1[:, None], (1, 10))
        new_velocities += self.c_1 * r_1 * (self.p_bests - self.particles)
        # add social component
        r_2 = np.random.random(self.N)
        r_2 = np.tile(r_2[:, None], (1, 10))
        g_best = np.tile(self.g_best[None], (self.N, 1))
        new_velocities += self.c_2 * r_2 * (g_best  - self.particles)
        self.is_running = np.sum(self.velocities - new_velocities) != 0
        # update positions and velocities
        self.velocities = new_velocities
        self.particles = self.particles + new_velocities
    def update_bests(self):
        fits = [self.fitness_function(i) for i in self.particles]
        for i in range(len(self.particles)):
            # update best personnal value (cognitive)
            if fits[i] < self.p_bests_values[i]:
                self.p_bests_values[i] = fits[i]
                self.p_bests[i] = self.particles[i]
                # update best global value (social)
                if fits[i] < self.g_best_value:
                    self.g_best_value = fits[i]
                    self.g_best = self.particles[i]


def griewank_func(x, n = 10):
    fr = 4000
    s = 0
    p = 1
    for j in range(n):
        s = s+x[j]**2
    for j in range(n):
        p = p*math.cos(x[j]/math.sqrt(j+1))
    return s/fr-p+1

def rosen_func(x, n=10):
    sum = 0
    for j in range(n-1):
        sum = sum+100*(x[j]**2-x[j+1])**2+(x[j]-1)**2
    return sum

def opt_funct(x,n = 10):
    return griewank_func(x,n)

num_particles = 10
num_features = 10

iterations_to_converge = 0
ITERATIONS = 100
t2 = []
for k in range(ITERATIONS):
    particles = np.random.uniform(-600, 600, (num_particles, num_features))
    velocities = (np.random.random((num_particles, num_features)) - 0.5) / 10
    pso = PSO(particles, velocities, opt_funct)
    i = 0
    while pso.next():
        i += 1
    # Registra el número de iteraciones para converger
    iterations_to_converge += i
    tmp = [pso.g_best_value] + [i for i in pso.g_best]
    t2.append(tmp)

# Calcula el promedio de iteraciones requeridas para converger
average_iterations = iterations_to_converge / ITERATIONS
print(f"Número promedio de iteraciones para converger: {average_iterations:.2f}")


last_pso = t2[-1]

best_fitness_value = last_pso[0]

best_fitness_values = [pso[0] for pso in t2]

iterations = list(range(1, len(best_fitness_values) + 1))

fig = plt.figure()

ax1 = fig.add_subplot(121)
ax1.plot(iterations, best_fitness_values)
ax1.set_xlabel('Iteración')
ax1.set_ylabel('Mejor Valor de Aptitud')
ax1.set_title('Convergencia de PSO (2D)')
ax1.grid(True)

ax2 = fig.add_subplot(122, projection='3d')
X = [pso[1] for pso in t2] 
Y = [pso[2] for pso in t2] 
Z = best_fitness_values 
ax2.scatter(X, Y, Z, c='r', marker='o')
ax2.set_xlabel('Variable X')
ax2.set_ylabel('Variable Y')
ax2.set_zlabel('Mejor Valor de Aptitud')
ax2.set_title('Convergencia de PSO (3D)')

plt.tight_layout()
plt.show()
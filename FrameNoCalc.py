import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
n_particles = 50  # Number of particles
N_frames = 10000  # Number of frames
D = 1.0  # Diffusion coefficient (µm^2/s)
dt = 0.2  # Time step (s)
dim = 2  # Dimensions (2D)

# Derived parameters
std_dev = np.sqrt(2 * D * dt)  # Standard deviation of displacements

# Initialize particle positions (n_particles x N_frames x dim)
positions = np.zeros((n_particles, N_frames, dim))

# Simulate Brownian motion
for t in range(1, N_frames):
    displacements = np.random.normal(0, std_dev, (n_particles, dim))
    positions[:, t] = positions[:, t - 1] + displacements

# Function to calculate MSD
def calculate_msd(positions, max_lag):
    n_particles, N_frames, dim = positions.shape
    msd = np.zeros(max_lag)
    for tau in range(1, max_lag + 1):
        displacements = positions[:, tau:] - positions[:, :-tau]
        squared_displacements = np.sum(displacements**2, axis=2)
        msd[tau - 1] = np.mean(squared_displacements)
    return msd

# Compute MSD for different lag times
max_lag = int(N_frames / 2)  # Use up to half the frames for lag times
msd = calculate_msd(positions, max_lag)
lag_times = np.arange(1, max_lag + 1) * dt

# Theoretical MSD
msd_theoretical = 4 * D * lag_times

# Plot results
plt.figure(figsize=(8, 6))
plt.plot(lag_times, msd, label="Simulated MSD")
plt.plot(lag_times, msd_theoretical, label="Theoretical MSD", linestyle="--")
plt.xlabel("Lag time (s)")
plt.ylabel("Mean Squared Displacement (µm²)")
plt.title(f"MSD for {n_particles} Particles over {N_frames} Frames")
plt.legend()
plt.grid()
plt.show()
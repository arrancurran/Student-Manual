# Avogadro's Number from Diff. Coeff.

Avogadro’s number ($N_A$) can be calculated from the translational diffusion coefficient ($D_T$) using the **Stokes-Einstein equation** in combination with the **Ideal Gas Law**.

# Stokes-Einstein equation

### $D_T = \frac{k_B T}{6 \pi \eta r}$

Where:

• $D_T$ = diffusion coefficient ($m^2/s$),

• $k_B$ = Boltzmann constant ($J/K$),

• $T$ = temperature ($K$),

• $\eta$ = dynamic viscosity of the medium ($Pa·s$),

• $r$ = radius of the particle ($m$).


# Ideal Gas Law

$PV = nRT$

• $P$ = Pressure,

• $V$ = Volume,

• $n$ = Number of moles,

• $R$ = Ideal gas constant,

## Microscopic Ideal Gas Law

On a molecular scale, the ideal gas law is,

$PV = Nk_BT$.

• $N$ = Number of particles,

Relating $n$ and $N$

The number of particles $N$ is related to the number of moles $n$ by Avogadro’s number,

$N = nN_A$.

Substituting into $PV = Nk_BT$, we get,

$PV = nN_Ak_BT$.

Comparing this with the macroscopic ideal gas law $PV = nRT$,

$R = N_Ak_B$.

$\therefore k_B = \frac{R}{N_A}$

Substitute into Stokes-Einstein and solve for $N_A$
  
## $N_A = \frac{R T}{6 \pi \eta r D_T}$

**Example**

Imagine a spherical particle in water at $T = 298 K$ 

• $D = 5.0 \times 10^{-13}$  $m^2/s$,

• $\eta$ = 0.001 $Pa·s$,

• $r = 1.0 \times 10^{-6}$  $m$.
  
The ideal gas constant $R = 8.314$ $J/\text{mol}·K$.

$N_A$ = $\frac{(8.314)(298)}{6 \pi (0.001)(10^{-6})(5.0 \times 10^{-13})}$
  
First, calculate the denominator:

$6 \pi (0.001)(10^{-6})(5.0 \times 10^{-13}) = 9.4248 \times 10^{-18}$  

Now calculate:

$N_A$ = $\frac{2480.572}{9.4248 \times 10^{-18}} \approx 6.6 \times 10^{23} \, \text{mol}^{-1}$.
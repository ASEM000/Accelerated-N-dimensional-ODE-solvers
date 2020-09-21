# Accelerated N-dimensional Runge-Kutta solvers
Accelerated N dimensional Runge Kutta solvers with implementations in numpy , numba and matlab

#### Implementation of N dimensional Euler,RK2,RK3,RK4 and Dormand–Prince Runge kutta in python+numba
On average , the accelerated implementation is **10x** faster than matlab and **20x~40x** faster than numpy implementation

### Comparison plots
![Image](https://i.imgur.com/tA9QHwN.png)

### How to use ?
1. similar to matlab , you need to create a function that accepts t,y and output y vectors of the same shape as the ode degree
2. check the sample implementation included in the jupyter notebook


### Future work 
Cuda implementation

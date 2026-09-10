# fractfal_gen

*f.c* code is packaged as a lib into *f.so* with

```bash
gcc -shared -fPIC -o f.so f.c -lm
```

*f.so* is then loaded into python file *c_module.py* with ctypes

*c_module.py* is imported into the *fractal.py* for plotting

*fractal.py* plots grid using matplotlib based on the values computed using the *c_module.py* **iterate_point(X, Y, CX, CY, N)** function

### **iterate_point(X, Y, CX, CY, N)** function
- *X* points x coordinate (real part)
- *Y* points y coordinate (imaginary part)\\
$C = C_X + i \cdot C_Y$
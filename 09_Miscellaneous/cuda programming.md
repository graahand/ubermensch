#rnd #learning 
GPUs memory bandwidth is faster/better as compared to CPU because of the use of wider memory buses in GPU (256-bit, 384-bit, 512-bit) interface whereas CPUs memory uses narrow memory buses (64-bit). GPUs memory bandwidth ranges from GB/s to TB/s. 

double precision means 64 bit (1 bit for sign 11 bits for exponent and 53 bits for mantissa), single precision means 32 bit (1 bit for sign, 8 bit for exponent, 23 bits for mantissa)

IEEE 754 is the de facto standard for floating-point arithmetic in modern computing, supporting a variety of precisions and covering edge cases for robust numerical computation.

OpenGL (open graphics language) is a graphics API used for rendering 2d and 3d graphics. it is designed for hardware accelerated rendering system. 
Direct3D is microsoft's _proprietary_ api for rendering 2d and 3d graphiccs for microsoft platforms (windows, xbox). 

2007, programs written on CUDA didn't have to use graphics part of the GPU instead CUDA can directly talk to the special general-purpose part of chip made for parallel processing. 

GPUs are made up of SMs (streaming microprocessors), each SMs contains SPs (streaming processors) which are basic execution units for arithmetic operations (+ and *), teraflops of floating point operations are performed by SMs and SPs. *

GPU also have their global memory with very high bandwidth as compared to CPU's RAM. 



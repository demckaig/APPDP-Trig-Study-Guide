#!/usr/bin/env python
# coding: utf-8

# # Algebra Review
# In this chapter we will highlight some of the key algebra tools/tricks that are utilize throughout physics.

# ## Order of Operations
# Consider the following mathematical expression,
# 
# ```{math}
# :label: viral-math-problem
# 6\div2(1+2)
# ```
# 
# Problems like this one often go viral has people disgree on what the answer should be. Is it 1, is it 9, or is it some other number? It *feels* ambiguous on what the answer should be because depending on how you do your operations you will get different results.
# 
# To prevent these types of confusion mathematics has adopted the **order of operations**. The sequence of rules dictating how to evaluate expressions lke the one above. You can remember the steps with the *PEMDAS* acronym.
# 
# ```{admonition} PEMDAS
# - *P*(arentheses)
# - *E*(xponents)
# - *M*(ultiplication) 
# - *D*(ivision)
# - *A*(ddition)
# - *S*(ubtraction) 
# 
# The order of operations using PEMDAS for any expression will be 
# 1. Simplify anything inside a *parentheses*.
# 2. Simplify anything involving *exponents* (this includes squareroots or any other radical).
# 3. Evaluate all *multiplications* and *divisions*.
# 4. Evaluate all *additions* and *subtractions*
# 
# Note that steps three and four are evaluated from left to right. 
# ```
# 
# Using PEMDAS we can calculate the equation {eq}`viral-math-problem` correctly.
# 
# $$6\div2\underbrace{(1+2)}$$
# $$\underbrace{6\div2}(3)$$
# $$3(3)$$
# $$9$$

# ## Quadratic Formula
# Many problems in physics result in solving a quadratic polynomial. As an example how much will a spring compress if a weight is dropped on it.
# 
# ```{figure} ./media/spring-drop-mass.svg
# ---
# align: center
# name: spring-compress
# ---
# Where you define the $y$-axis to be zero will change what potential energies you have initially and finally.
# However, your choice of coordinate system will not change the final answer.
# ```
# 
# Assume the block was released from rest at a height $h$ above the spring. Let $y$ represent the height of the spring and set it equal to zero when the spring is relaxed. Conservation of energy tells us that
# 
# ```{math}
# :label: eq-energy-conservation
# mgh=\tfrac{1}{2}ky^2+mgy
# ```
# 
# This is a quadratic equation in $y$ and it has no nice simplifications to help us solve for $y$.
# This is where we can use the *quadratic formula* to tackle any problem.
# 
# ```{admonition} Quadratic Formula
# $$ax^2+bx+c=0$$
# 
# $$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$ (eq-quad-formula)
# ```

# ## Exercises
# 1. Solve for how much the spring in figure {numref}`spring-compress` will compress, given the following values.
#    m=.40 kg, g=9.8 m/s$^2$m h=.60 m, k=340 N/m.
#    ```{dropdown} Solution
#    $$mgh=\tfrac{1}{2}ky^2+mgy$$
#    $$\tfrac{1}{2}ky^2+mgy-mgh=0$$
#    $$y=\frac{-mg\pm\sqrt{(mg)^2-4*(\tfrac{1}{2}k)(-mgh)}}{2(\tfrac{1}{2}k)}$$
#    $$y=[+0.11\,\text{m},-0.13\,\text{m}]$$
#    
#    The solution to this particular problem will be the -0.13 meters. 
#    ```
#    

# README.md
Implementing Matrix Transformations, Determinants, and Jacobian Matrix computations from scratch using NumPy and SymPy.
# 🧮 Advanced Linear Algebra & Calculus Solvers

Welcome to my mathematical computing repository! As a Mathematics student, this project bridges the gap between pure mathematical theory and computational execution using Python.

## 📌 Project Overview
This tool focuses on visualising and calculating foundational concepts in **Linear Algebra** and **Multivariable Calculus**, specifically focusing on Matrix Transformations, Determinants, and their geometric relationship to integration.

## 📐 Mathematical Framework

### 1. Determinants and Linear Transformations
In Linear Algebra, a matrix $A$ acts as a linear transformation that maps space. The **Determinant**, denoted as $\det(A)$, represents the factor by which areas or volumes scale during this transformation:

$$ \det(A) = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc $$

If $\det(A) = 0$, the transformation collapses the space into a lower dimension, meaning the matrix is singular and non-invertible.

### 2. The Jacobian and Multiple Integration
In Multivariable Calculus, when changing variables in multiple integrals (e.g., substituting Cartesian coordinates to Polar or Spherical), the **Jacobian determinant** acts as the scaling factor for the differential area or volume element:

$$ \iint_{R} f(x,y) \, dx \, dy = \iint_{G} f(g(u,v), h(u,v)) \cdot \left| \frac{\partial(x,y)}{\partial(u,v)} \right| \, du \, dv $$

Where the Jacobian matrix is defined as:
$$ J = \frac{\partial(x,y)}{\partial(u,v)} = \begin{bmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{bmatrix} $$

---

## 💻 Code Implementation & Features
This repository contains Python scripts leveraging **NumPy** and **SymPy** to:
* **Compute Determinants & Eigenvalues:** Dynamically calculates values for any $n \times n$ matrix.
* **Symbolic Differentiation:** Computes exact Jacobian matrices for multivariable functions.
* **Geometric Verification:** Verifies if a transformation preserves orientation (positive determinant) or reverses it (negative determinant).

## 🚀 How to Run
1. Clone the repository.
2. Install dependencies: `pip install numpy sympy`
3. Run the main solver: `python main.py`

---
✨ *Built with passion by Ahlam Al-Mutairi — Actively exploring the intersection of Pure Mathematics and Computer Science.*

import numpy as np
import sympy as sp

def analyze_matrix():
    print("\n--- 1. Linear Algebra Operations (NumPy) ---")
    # تعريف مصفوفة 2x2 كمثال (يمكن تغيير الأرقام)
    A = np.array([[4, 2],
                  [1, 3]])
    print(f"Matrix A:\n{A}")
    
    # حساب المحدد (Determinant)
    det_A = np.linalg.det(A)
    print(f"Determinant of A: {det_A:.2f}")
    
    # حساب القيم الذاتية والمتجهات الذاتية (Eigenvalues & Eigenvectors)
    eigenvalues, eigenvectors = np.linalg.eig(A)
    print(f"Eigenvalues: {eigenvalues}")

def calculate_jacobian():
    print("\n--- 2. Multivariable Calculus: Jacobian (SymPy) ---")
    # تعريف المتغيرات الرمزية
    r, theta = sp.symbols('r theta')
    
    # التحويل من الإحداثيات الكارتيزية إلى القطبية كدوال
    # x = r * cos(theta), y = r * sin(theta)
    x = r * sp.cos(theta)
    y = r * sp.sin(theta)
    
    # حساب مصفوفة الجاكوبي لـ [x, y] بالنسبة لـ [r, theta]
    functions = sp.Matrix([x, y])
    variables = sp.Matrix([r, theta])
    jacobian_matrix = functions.jacobian(variables)
    
    print("Jacobian Matrix (Polar Coordinates transformation):")
    sp.pprint(jacobian_matrix)
    
    # حساب محدد الجاكوبي (الذي نستخدمه في التكامل الثنائي)
    jacobian_det = jacobian_matrix.det()
    print(f"Jacobian Determinant: {sp.simplify(jacobian_det)}")

if __name__ == "__main__":
    print("Executing Mathematical Framework Solver...")
    analyze_matrix()
    calculate_jacobian()

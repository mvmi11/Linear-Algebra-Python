import numpy as np
import matplotlib.pyplot as plt

# 1. Define the mathematical function (Cost Function)
# f(x) = x^2 + 4x + 4  (A simple parabola)
def function_f(x):
    return x**2 + 4*x + 4

# 2. Define the exact derivative (Calculus: f'(x) = 2x + 4)
def derivative_f(x):
    return 2*x + 4

def gradient_descent(starting_x, learning_rate, iterations):
    x_history = [starting_x]
    y_history = [function_f(starting_x)]
    
    x = starting_x
    for i in range(iterations):
        # Apply Calculus: move in the opposite direction of the gradient
        gradient = derivative_f(x)
        x = x - (learning_rate * gradient)
        
        x_history.append(x)
        y_history.append(function_f(x))
        
    return x_history, y_history

if __name__ == "__main__":
    print("🚀 Initializing Mathematical Optimization Solver...")
    
    # Hyperparameters
    start_point = 4.0      # Starting at x = 4
    learning_step = 0.1    # Step size
    total_steps = 20       # Iterations
    
    # Run the algorithm
    x_steps, y_steps = gradient_descent(start_point, learning_step, total_steps)
    
    print(f"✅ Optimization Complete!")
    print(f"🎯 Global Minimum found near x = {x_steps[-1]:.4f}, f(x) = {y_steps[-1]:.4f}")
    
    # Visualizing the Calculus concept
    x_vals = np.linspace(-6, 2, 100)
    plt.plot(x_vals, function_f(x_vals), label='f(x) = x² + 4x + 4', color='blue')
    plt.scatter(x_steps, y_steps, color='red', label='Gradient Descent Steps')
    plt.plot(x_steps, y_steps, color='red', linestyle='dashed', alpha=0.5)
    plt.title('Calculus in AI: Optimization Via Gradient Descent')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    
    # Save the mathematical plot to push to GitHub
    plt.savefig('optimization_plot.png')
    print("📊 Plot saved successfully as 'optimization_plot.png'!")

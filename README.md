# Lagrange Interpolation Visualization

This project visualizes the process of constructing a Lagrange Interpolating Polynomial given a set of data points. The visualization includes an animation that shows how the polynomial is built step-by-step, and it prints the final simplified polynomial equation.

## Author

Jimmy Sitompul

## Project Structure

- `lagrange.py`: Contains the functions for computing the Lagrange Interpolating Polynomial.
- `main.py`: Handles user input, animates the graph, and prints the simplified polynomial.

## Prerequisites

Make sure you have Python installed on your system. You will also need to install the following Python libraries:

- `numpy`
- `matplotlib`
- `sympy`
  

You can install these libraries using `pip`:

```sh
pip install numpy matplotlib sympy
```

1. Clone the Repository: Clone this repository to your local machine.

```sh
git clone https://github.com/yourusername/lagrange-interpolation.git
cd lagrange-interpolation
```

2. Run the Main Script: Execute the main.py script to start the animation and see the resulting polynomial.

```sh
python main.py
```

3. Input Data Points: You will be prompted to enter the number of data points and their corresponding x and y values.

## Example

When you run the main.py script, you will be prompted to enter the number of data points and their coordinates. The script will then animate the Lagrange Interpolating Polynomial construction and print the final polynomial equation.

## Sample Input
```bash
Enter the number of data points: 4
Enter x[1]: -2
Enter y[1]: 0
Enter x[2]: 1
Enter y[2]: 2
Enter x[3]: 5
Enter y[3]: 4
Enter x[4]: 7
Enter y[4]: 3
```

## Visualization

![lagrange](https://github.com/jsitompul/lagrange-interpolation-visualization/assets/151981311/0c14559e-25bf-4600-a570-3c48683c64d7)

## Output

After the animation, the simplified polynomial will be printed. For example:

```bash
Final Lagrange Interpolating Polynomial:
P(x)= -0.0158730158730159*x**3 + 0.0396825396825398*x**2 + 0.753968253968254*x + 1.22222222222222
```

## Explanation of Files

lagrange.py

- `lagrange_basis(x_vals, i, x)`: Computes the Lagrange basis polynomial ![image](https://github.com/jsitompul/lagrange-interpolation-visualization/assets/151981311/f853b353-608b-46bb-8bb5-d025d4ec9d80)
- `lagrange_interpolation(x_vals, y_vals, x)`: Computes the full Lagrange polynomial incrementally.
- `build_polynomial_string(terms)`: Builds and simplifies the polynomial equation string using SymPy.

main.py

- `input_data()`: Handles user input for data points.
- `update(frame)`: Updates the plot for each animation frame.
- `FuncAnimation`: Sets up the animation using Matplotlib.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
1. The project uses `NumPy` for numerical operations.
2. `matplotlib` is used for plotting and animation.
3. `sympy` is used for symbolic mathematics and simplifying the polynomial.
   

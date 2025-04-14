# Root Finding For Quadratic Equation using Hill Climbing Algorithm
## 🚀 Functions Overview
The functions implemented in this repo is basically root finding for equations using two approaches 
 ### Bisection Method 
 The Bisection Method is a reliable and straightforward root-finding technique that works on continuous functions where the function changes sign over an interval 
[
𝑎
,
𝑏
]
[a,b], meaning 
𝑓
(
𝑎
)
⋅
𝑓
(
𝑏
)
<
0
f(a)⋅f(b)<0.
It works by repeatedly halving the interval and selecting the subinterval where the sign change occurs, which ensures the root lies within. The process continues until the interval becomes sufficiently small or a desired tolerance is met.

✅ Key Features:

Guaranteed convergence if the initial interval satisfies the sign condition.

Slower but very reliable.

Requires the function to be continuous.
 ### Hill Climbing algorithm method

 The Hill Climbing Algorithm is a heuristic optimization algorithm typically used for maximizing or minimizing a function.
In this context, it's adapted for root finding by minimizing the absolute value 
∣
𝑓
(
𝑥
)
∣
∣f(x)∣. Starting from an initial guess, the algorithm iteratively moves in the direction (left or right) that reduces 
∣
𝑓
(
𝑥
)
∣
∣f(x)∣, using a defined step size. It stops when the function value is close enough to zero, within a specified tolerance.

✅ Key Features:

Does not require sign change like bisection.

Flexible and intuitive, but may get stuck in local minima for complex functions.

Works well when provided a good initial guess.
 
## 🛠 Installation & Usage
### 1 **Clone the Repository**
```sh
git clone https://github.com/johnnas12/Root-Finding-Using-HCA.git
cd Root-Finding-Using-HCA
```

### 2️ **Create a Virtual Environment** (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️ **Install Dependencies**
```sh
pip install -r requirements.txt
```
### 4 ** Run Files **
```
python root_finding_using_bisection.py  # for the bisection method
```
```
python root_finding_using_hca.py # for the Hill climbing algorithm method
```

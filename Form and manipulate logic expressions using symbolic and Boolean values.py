from sympy import symbols, Not, And, Or, Implies, Eq
from sympy.logic.boolalg import truth_table

# Define symbolic variables
p, q, r = symbols('p q r')

# Create logical expressions
expr_and = And(p, q, r)              # Logical AND
expr_or = Or(p, q, r)                # Logical OR
expr_not = Not(p)                    # Logical NOT
expr_implies = Implies(p, q)         # Logical implication (p implies q)
expr_iff = Eq(p, q)                  # Logical equivalence (p if and only if q)

# Evaluate logical expressions
result_and = expr_and.subs({p: True, q: False, r: True})
result_or = expr_or.subs({p: True, q: False, r: True})
result_not = expr_not.subs({p: True})

print("AND Result:", result_and)
print("OR Result:", result_or)
print("NOT Result:", result_not)

# Simplify logical expressions
simplified_and = expr_and.simplify()
simplified_or = expr_or.simplify()
simplified_not = expr_not.simplify()

print("Simplified AND Expression:", simplified_and)
print("Simplified OR Expression:", simplified_or)
print("Simplified NOT Expression:", simplified_not)

# Generate truth tables
tt_and = truth_table(expr_and, [p, q, r])
tt_or = truth_table(expr_or, [p, q, r])
tt_not = truth_table(expr_not, [p])

print("AND Truth Table:")
print(tt_and)

print("OR Truth Table:")
print(tt_or)

print("NOT Truth Table:")
print(tt_not)

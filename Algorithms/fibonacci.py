# def fib(num):
#     """basic fibonacci sequence implementation, printing out each number as it runs."""
#     a=1
#     b=0
#     counter = 0
#     for n in range(num):
#         b=a
#         a = a+b
#         counter +=1
#         print(counter, ":", a)
#     return a        


 
# fib(5)

# def rec_fib(num):
#     if num <= 0:
#         return 0
#     return rec_fib(num - 1) + rec_fib(num - 2)

# result = rec_fib(5)
# print(result)

"""
fibonacci visualized
"""
import graphviz

dot = graphviz.Digraph(format="png")
dot.attr(dpi="120")

call_id = 0

def fib_trace(n, parent=None):
    global call_id
    call_id += 1
    node_id = f"{n}_{call_id}"  # unique ID per call
    
    # base cases
    if n == 0:
        value = 0
    elif n == 1:
        value = 1
    else:
        value = None

    label = f"rec_fib({n})" if value is None else f"rec_fib({n})={value}"
    dot.node(node_id, label)

    if parent:
        dot.edge(parent, node_id)

    if value is None:
        left_val = fib_trace(n-1, node_id)
        right_val = fib_trace(n-2, node_id)
        value = left_val + right_val
        dot.node(node_id, f"rec_fib({n})={value}")

    return value

fib_trace(5)
dot.render("./fib5_tree_unique", format="png", cleanup=True)

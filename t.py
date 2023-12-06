import multiprocessing

def find_low(value):
    # Your calculation logic here
    print(f"Processing value: {value}")

def generate_values(n):
    # Your generator logic here
    for i in range(n):
        yield i

ns = [10, 20, 30]  # Replace this with your list of values

with multiprocessing.Pool() as pool:
    for rn in ns:
        chunk = list(generate_values(rn))
        print(chunk)
        
        # Use the map function to apply the find_low function to each element in the chunk list
        pool.map(find_low, chunk)
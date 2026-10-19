import random
import timeit

def insertion_sort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1
		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key
	return arr



def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	mid = len(arr) // 2
	left_half = merge_sort(arr[:mid])
	right_half = merge_sort(arr[mid:])
	return merge(left_half, right_half)

def merge(left, right):
	sorted_result = []
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			sorted_result.append(left[i])
			i += 1
		else:
			sorted_result.append(right[j])
			j += 1
	sorted_result.extend(left[i:])
	sorted_result.extend(right[j:])
	return sorted_result



def run_comparison():
	
	sizes = [100, 500, 2000, 8000]
	print("-" * 100)
	print(f"| {'Розмір масиву (n)':<18} | {'Insertion Sort (с)':<25} | {'Merge Sort (с)':<25} | {'Timsort (sorted) (с)':<22} |")
	print("-" * 100)
	
	for size in sizes:
		data = [random.randint(0, 100000) for _ in range(size)]
		t_insertion = timeit.timeit(lambda: insertion_sort(data.copy()), number=3)
		t_merge = timeit.timeit(lambda: merge_sort(data.copy()), number=3)
		t_timsort = timeit.timeit(lambda: sorted(data.copy()), number=3)    
		print(f"| {size:<18} | {t_insertion:<25} | {t_merge:<25} | {t_timsort:<22} |")  
	print("-" * 100) 


if __name__ == "__main__":
	run_comparison()
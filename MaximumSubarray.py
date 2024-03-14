import random
import time


def MaxSubarray(array):
    n = len(array)
    max_sum = -100000000000
    # Kadane's algorithm

    for i in range(0,n):
        curr_sum = 0
        for j in range(i, n):
            
            curr_sum = curr_sum + array[j]
            if (curr_sum > max_sum):
                
                max_sum = curr_sum
                print(max_sum) 
    print(f"the list was {len(array)}")
    print(f"the max sum was {max_sum}")
    return max_sum

def main():
    lista = [-6006, 5752, 2847, -3028, -5295, -2074, 7121, 8234, -6757, -1091, 9804, 6377, -6797, -3240, -7476, -1271, -9287, 5410, -3700, -1340, 4789, -6098, 4433, -5586, -5688, 3065, 4383, 6075, 4942, 9986, -4923, 6048, 5051, -8509, 3592, -9445, 8850, -5355, 4607, -7127, -1308, -5791, 4186, 5886, 206, -6195, -2967, -7808, 8445, 728, 4390, -7390, -9123, 2433, 2934, -5161, 1071, 7996, -8041, 7423, -2674, 3393, -530, 3307, 9533, 3570, 155, -2062, -5540, -9499, -6183, -4625, -3130, 7910, -8222, 4017, 5236, -780, 9448, 8850, 7705, -5284, 9358, 9584, -7281, -5617, -7381, 9942, -8221, 1922, -8645, 6940, -3902, 3406, -7299, -7776, -4124, 6036,-9212,-3563]
    MaxSubarray(lista)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Tiempo de ejecucion: {(end-start)} seconds")
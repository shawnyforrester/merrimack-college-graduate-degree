package fibonacci



func Fibonacci(n int)([]int){
	var output []int
	var nextNum int
	if n == 1{
		output = append(output, 0)
	} else if n == 2{
		output = append(output, 0, 1)
	} else {
		output = append(output, 1, 1, 1)
		for i := 3; i < n; i++{
			nextNum = output[i-1] + output[i-2] + output [i-3]
			output = append(output, nextNum)
		} 
	}
	return output
}

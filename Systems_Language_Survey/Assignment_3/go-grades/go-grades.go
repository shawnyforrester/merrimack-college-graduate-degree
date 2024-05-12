//Create a go function that takes a number and assigns grade to "A" if the number is greater than 90, "B" if the number is greater than 80, "C" if the number is greater than 70, "D" if the number is greater than 60 and "F" otherwise. The function should return the grade as a string. 
//package gogrades


package gogrades

func Grade(score int) string {
	var grade = ""	
	switch {
	case score >= 90:
		grade=  "A"
	case score >= 80:
		grade =  "B"
	case score >= 70:
		grade =  "C"
	default:
		grade = "F"
	}
	if((score % 10 >= 7) && (grade != "A" || grade != "F")) {
		grade = grade + "+"
	}
	if ((score % 10 <=3) && (grade != "F")){
		grade = grade + "-"
	}
	return grade
}


package main

import "fmt"

func partition(s string) [][]string {
	if len(s) == 0 {
		return [][]string{}
	}
	var result [][]string

	for i:=0; i<len(s); i++ {
		partA := s[:i+1]
		if !isPalindrome(partA) {
			continue
		}
		partBList := partition(s[i+1:])

		var tmpList [][]string
		if len(partBList) == 0 {
			tmpList = append(tmpList, []string{partA})
		}
		for _, partB := range partBList {
			var l []string
			l = append(l, partA)
			l = append(l, partB...)
			tmpList = append(tmpList, l)
		}
		result = append(result, tmpList...)
	}

	println("================")
	fmt.Println(result)
	return result
}

func isPalindrome(str string) bool {

	i, j := 0, len(str)-1

	for j > i {
		if str[i] != str[j] {
			return false
		}
		j--
		i++
	}

	return true
}

func main() {
	// x := partition("abcd")
	x := partition("abbcbbd")

	println("-----------------")
	fmt.Println(x)
}

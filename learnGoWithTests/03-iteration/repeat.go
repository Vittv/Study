package iteration

import "strings"

func Repeat(character string, quantity int) string {
	repeatCount := quantity
	var repeated strings.Builder
	for i := 0; i < repeatCount; i++ {
		repeated.WriteString(character)
	}
	return repeated.String()
}


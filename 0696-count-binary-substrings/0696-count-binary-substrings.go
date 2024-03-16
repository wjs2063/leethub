func min(a int, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}

func countBinarySubstrings(s string) int {
	ans := make([]int, 0)
	// 처음값 1 추가
	ans = append(ans, 1)
	for i := 1; i < len(s); i++ {
		if s[i-1] == s[i] {
			ans[len(ans)-1]++
		} else {
			ans = append(ans, 1)
		}
	}
	res := 0
	for i := 1; i < len(ans); i++ {
		res += min(ans[i-1], ans[i])
	}
	return res

}
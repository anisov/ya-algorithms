package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func getMaxGoldWeight(goldBars []uint16, weight uint16) uint16 {
	dp := make([][]uint16, len(goldBars))
	for i := 0; i < len(dp); i++ {
		dp[i] = make([]uint16, weight+1)
	}
	for i := 0; i < len(goldBars); i++ {
		for j := uint16(1); j <= weight; j++ {
			var maxWeight uint16
			goldWeight := goldBars[i]
			if j == goldWeight {
				maxWeight = goldWeight
			} else if j > goldWeight {
				var prevWeight uint16
				if i >= 1 {
					prevWeight = dp[i-1][j-goldWeight]
				}
				maxWeight = goldWeight + prevWeight
			}
			var prevWeight uint16
			if i >= 1 {
				prevWeight = dp[i-1][j]
			}
			dp[i][j] = uint16(math.Max(float64(prevWeight), float64(maxWeight)))
		}
	}
	return dp[len(goldBars)-1][weight]
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	data := strings.Split(scanner.Text(), " ")
	goldBarsCount, _ := strconv.Atoi(data[0])
	weight, _ := strconv.Atoi(data[1])
	scanner.Scan()
	goldBars := make([]uint16, goldBarsCount)
	for i, v := range strings.Split(scanner.Text(), " ") {
		value, _ := strconv.Atoi(v)
		goldBars[i] = uint16(value)
	}
	fmt.Println(getMaxGoldWeight(goldBars, uint16(weight)))
}

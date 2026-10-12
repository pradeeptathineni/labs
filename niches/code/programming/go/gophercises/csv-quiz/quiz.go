// csv-quiz/quiz.go - Read a small CSV quiz

package main

// Use the standard CSV reader and text cleanup
import (
	"encoding/csv"
	"fmt"
	"io"
	"strings"
)

// Keep each prompt with its expected answer
type question struct {
	text   string
	answer string
}

// Read two-field rows and reject incomplete questions
func readQuiz(input io.Reader) ([]question, error) {

	// Let the CSV reader handle quoted commas and column counts
	reader := csv.NewReader(input)
	reader.FieldsPerRecord = 2
	rows, err := reader.ReadAll()
	if err != nil {
		return nil, fmt.Errorf("read quiz: %w", err)
	}
	if len(rows) == 0 {
		return nil, fmt.Errorf("quiz is empty")
	}

	// Keep prompt text and clean up the expected answers
	questions := make([]question, 0, len(rows))
	for index, row := range rows {
		if strings.TrimSpace(row[0]) == "" || strings.TrimSpace(row[1]) == "" {
			return nil, fmt.Errorf("row %d needs a question and answer", index+1)
		}
		questions = append(questions, question{row[0], strings.TrimSpace(row[1])})
	}
	return questions, nil
}

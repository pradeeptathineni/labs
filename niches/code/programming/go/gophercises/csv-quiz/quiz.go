// csv-quiz/quiz.go - Run the untimed half of a CSV quiz
// Usage: go run . [-csv path]

package main

// Use the standard CSV reader and text cleanup
import (
	"bufio"
	"encoding/csv"
	"errors"
	"flag"
	"fmt"
	"io"
	"os"
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

// Ask one question per answer line and stop cleanly at end of input
func askQuiz(questions []question, input io.Reader, output io.Writer) (int, error) {

	// Keep input and output replaceable in tests
	answers := bufio.NewScanner(input)
	correct := 0
	for index, item := range questions {
		if _, err := fmt.Fprintf(output, "Question %d: %s\n", index+1, item.text); err != nil {
			return correct, fmt.Errorf("write question: %w", err)
		}

		// Distinguish a clean end of input from a read failure
		if !answers.Scan() {
			if err := answers.Err(); err != nil {
				return correct, fmt.Errorf("read answer: %w", err)
			}
			break
		}

		// Count a right answer and immediately move to the next question
		if strings.TrimSpace(answers.Text()) == item.answer {
			correct++
		}
	}
	return correct, nil
}

// Parse the CSV option, run the quiz, and return a command status
func run(args []string, input io.Reader, output, errorOutput io.Writer) int {

	// Use Go's flag parser and keep its messages out of quiz output
	flags := flag.NewFlagSet("quiz", flag.ContinueOnError)
	flags.SetOutput(errorOutput)
	filename := flags.String("csv", "problems.csv", "quiz CSV path")
	if err := flags.Parse(args); err != nil {
		if errors.Is(err, flag.ErrHelp) {
			return 0
		}
		return 2
	}
	if flags.NArg() != 0 {
		fmt.Fprintln(errorOutput, "usage: quiz [-csv path]")
		return 2
	}

	// Keep the CSV file owned by this command, including error paths
	file, err := os.Open(*filename)
	if err != nil {
		fmt.Fprintln(errorOutput, "quiz:", err)
		return 1
	}
	defer file.Close()
	questions, err := readQuiz(file)
	if err != nil {
		fmt.Fprintln(errorOutput, "quiz:", err)
		return 1
	}

	// Run the untimed part and report the score against all questions
	correct, err := askQuiz(questions, input, output)
	if err != nil {
		fmt.Fprintln(errorOutput, "quiz:", err)
		return 1
	}
	if _, err := fmt.Fprintf(output, "Correct: %d/%d\n", correct, len(questions)); err != nil {
		fmt.Fprintln(errorOutput, "quiz:", err)
		return 1
	}
	return 0
}

// Use the real command streams when called from the terminal
func main() {
	os.Exit(run(os.Args[1:], os.Stdin, os.Stdout, os.Stderr))
}

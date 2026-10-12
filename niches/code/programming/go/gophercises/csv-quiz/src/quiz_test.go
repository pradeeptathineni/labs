// src/quiz_test.go - Check the quiz's input and scoring

package main

// Build small inputs using the standard test tools
import (
	"bytes"
	"errors"
	"io"
	"os"
	"path/filepath"
	"strings"
	"testing"
)

// Check useful CSV inputs and the mistakes that should fail
func TestReadQuiz(t *testing.T) {

	// Include quoted commas, extra columns, and missing content
	cases := []struct {
		name  string
		input string
		want  []question
		bad   bool
	}{
		{
			name:  "quoted comma",
			input: "\"Count words, carefully\", 2 \n",
			want:  []question{{"Count words, carefully", "2"}},
		},
		{
			name:  "two rows",
			input: "First,one\nSecond,two\n",
			want:  []question{{"First", "one"}, {"Second", "two"}},
		},
		{"empty", "\n", nil, true},
		{"short row", "Question\n", nil, true},
		{"long row", "Question,yes,extra\n", nil, true},
		{"bad quote", "\"Question,yes\n", nil, true},
		{"empty question", ",yes\n", nil, true},
		{"empty answer", "Question, \n", nil, true},
	}

	// Read each input and compare either its rows or its failure
	for _, example := range cases {
		t.Run(example.name, func(t *testing.T) {
			got, err := readQuiz(strings.NewReader(example.input))
			if example.bad {
				if err == nil {
					t.Fatal("expected invalid quiz to fail")
				}
				return
			}
			if err != nil {
				t.Fatal(err)
			}
			if len(got) != len(example.want) {
				t.Fatalf("got %d rows, want %d", len(got), len(example.want))
			}

			// Compare prompt and answer text without losing whitespace meaning
			for index, expected := range example.want {
				if got[index] != expected {
					t.Fatalf("row %d: got %+v, want %+v", index, got[index], expected)
				}
			}
		})
	}
}

// Check scoring, whitespace cleanup, wrong answers, and early EOF
func TestAskQuiz(t *testing.T) {

	// Use two questions and keep the expected prompts explicit
	questions := []question{{"First", "one"}, {"Second", "two"}}
	prompts := "Question 1: First\nQuestion 2: Second\n"
	cases := []struct {
		name   string
		input  string
		score  int
		output string
	}{
		{"right", "one\ntwo\n", 2, prompts},
		{"wrong", "no\ntwo\n", 1, prompts},
		{"spaces", " one \n two \n", 2, prompts},
		{"end of input", "", 0, "Question 1: First\n"},
	}

	// Compare the actual prompts and score for each answer sequence
	for _, example := range cases {
		t.Run(example.name, func(t *testing.T) {
			var output bytes.Buffer
			got, err := askQuiz(questions, strings.NewReader(example.input), &output)
			if err != nil {
				t.Fatal(err)
			}
			if got != example.score || output.String() != example.output {
				t.Fatalf("got score %d and output %q", got, output.String())
			}
		})
	}
}

// Supply a real read failure through the same interface as stdin
type failedInput struct{}

// Read reports a failure rather than ordinary end of input
func (failedInput) Read(_ []byte) (int, error) {
	return 0, io.ErrUnexpectedEOF
}

// Supply a real write failure through the same interface as stdout
type failedOutput struct{}

// Write reports a closed output stream
func (failedOutput) Write(_ []byte) (int, error) {
	return 0, io.ErrClosedPipe
}

// Preserve read and write errors rather than reporting a clean score
func TestStreamErrors(t *testing.T) {
	questions := []question{{"First", "one"}}

	// A broken input stream differs from ordinary end of input
	_, err := askQuiz(questions, failedInput{}, io.Discard)
	if !errors.Is(err, io.ErrUnexpectedEOF) {
		t.Fatalf("got %v, want a read error", err)
	}

	// A broken output stream should stop before asking more questions
	_, err = askQuiz(questions, strings.NewReader("one\n"), failedOutput{})
	if !errors.Is(err, io.ErrClosedPipe) {
		t.Fatalf("got %v, want a write error", err)
	}
}

// Check a custom CSV path and command-level failure statuses
func TestCommand(t *testing.T) {

	// Keep command inputs in a temporary directory
	filename := filepath.Join(t.TempDir(), "quiz.csv")
	if err := os.WriteFile(filename, []byte("First,one\nSecond,two\n"), 0600); err != nil {
		t.Fatal(err)
	}
	cases := []struct {
		name string
		args []string
		code int
	}{
		{"custom CSV", []string{"-csv", filename}, 0},
		{"missing CSV", []string{"-csv", filename + ".missing"}, 1},
		{"timer not built", []string{"-limit", "1"}, 2},
		{"extra argument", []string{"extra"}, 2},
		{"help", []string{"-h"}, 0},
	}

	// Check output and status through the same command entry point
	for _, example := range cases {
		t.Run(example.name, func(t *testing.T) {
			var output, errorOutput bytes.Buffer
			code := run(example.args, strings.NewReader("one\nwrong\n"), &output, &errorOutput)
			if code != example.code {
				t.Fatalf("got code %d, want %d: %s", code, example.code, errorOutput.String())
			}
			if example.name == "custom CSV" {
				if !strings.HasSuffix(output.String(), "Correct: 1/2\n") || errorOutput.Len() != 0 {
					t.Fatalf("unexpected output %q or error %q", output.String(), errorOutput.String())
				}
			} else if example.name != "help" && (output.Len() != 0 || errorOutput.Len() == 0) {
				t.Fatal("failure should write only to the error stream")
			}
		})
	}
}

// csv-quiz/quiz_test.go - Check the quiz's input and scoring

package main

// Build small inputs using the standard test tools
import (
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

% gpa_calculator.pl

% Facts for grade points
grade_point('A', 4.0).
grade_point('A-', 3.67).
grade_point('B+', 3.33).
grade_point('B', 3.0).
grade_point('B-', 2.67).
grade_point('C+', 2.33).
grade_point('C', 2.0).
grade_point('C-', 1.67).
grade_point('D+', 1.33).
grade_point('D', 1.0).
grade_point('F', 0.0).

% Default GPA
:- dynamic default_gpa/1.
default_gpa(2.0).

% Rule to update the default GPA
update_default_gpa(NewGPA) :-
    retractall(default_gpa(_)),
    assert(default_gpa(NewGPA)).

% Rule to calculate total grade points and total credits
calculate_totals([], 0, 0).
calculate_totals([[GradePoints, Credits] | T], TotalGradePoints, TotalCredits) :-
    calculate_totals(T, SubTotalGradePoints, SubTotalCredits),
    TotalGradePoints is SubTotalGradePoints + GradePoints * Credits,
    TotalCredits is SubTotalCredits + Credits.

% Rule to calculate GPA and round to 3 decimal places
calculate_gpa(TotalGradePoints, TotalCredits, GPA) :-
    TotalCredits > 0,
    GPA is TotalGradePoints / TotalCredits,
    round_to_three_decimal_places(GPA, RoundedGPA),
    GPA = RoundedGPA.

% Helper rule to round to 3 decimal places
round_to_three_decimal_places(Number, RoundedNumber) :-
    RoundedNumber is round(Number * 1000) / 1000.
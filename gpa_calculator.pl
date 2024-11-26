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

% Rule to calculate total grade points and total credits
calculate_totals([], 0, 0).
calculate_totals([[GradePoints, Credits] | T], TotalGradePoints, TotalCredits) :-
    calculate_totals(T, SubTotalGradePoints, SubTotalCredits),
    TotalGradePoints is SubTotalGradePoints + GradePoints * Credits,
    TotalCredits is SubTotalCredits + Credits.

% Rule to calculate GPA
calculate_gpa(TotalGradePoints, TotalCredits, GPA) :-
    TotalCredits > 0,
    GPA is TotalGradePoints / TotalCredits.
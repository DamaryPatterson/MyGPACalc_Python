% Define dynamic predicates to store total credits and total grade points
:- dynamic total_credits/1.
:- dynamic total_grade_points/1.

% Calculate GPA for a single semester
calculate_gpa(GPA) :-
    total_credits(TotalCredits),
    total_grade_points(TotalGradePoints),
    TotalCredits > 0, % Ensure there are credits to avoid division by zero
    GPA is TotalGradePoints / TotalCredits.

% Calculate cumulative GPA for multiple semesters
calculate_cumulative_gpa(Semester1Credits, Semester1Points, Semester2Credits, Semester2Points, CumulativeGPA) :-
    TotalCredits is Semester1Credits + Semester2Credits,
    TotalGradePoints is Semester1Points + Semester2Points,
    TotalCredits > 0, % Ensure there are credits to avoid division by zero
    CumulativeGPA is TotalGradePoints / TotalCredits.

% Example data for Semester 1
semester1_data([
    module(s, 3, 3.67),
    module(t, 3, 2.00),
    module(v, 4, 3.33),
    module(w, 4, 2.33),
    module(x, 3, 1.30),
    module(y, 2, 3.00),
    module(z, 1, 4.00)
]).

% Example data for Semester 2
semester2_data([
    module(l, 1, 4.30),
    module(p, 4, 3.67),
    module(x, 3, 3.00), % Redone module
    module(q, 4, 3.33),
    module(r, 2, 4.00)
]).

% Calculate total credits and grade points for a given semester
calculate_totals([], 0, 0).
calculate_totals([module(_, Credits, GradePoints) | Rest], TotalCredits, TotalGradePoints) :-
    calculate_totals(Rest, RestCredits, RestGradePoints),
    TotalCredits is RestCredits + Credits,
    TotalGradePoints is RestGradePoints + (Credits * GradePoints).

% Main predicate to calculate and print GPA and cumulative GPA
main :-
    % Calculate Semester 1 GPA
    semester1_data(Semester1Modules),
    calculate_totals(Semester1Modules, Semester1Credits, Semester1Points),
    retractall(total_credits(_)),
    retractall(total_grade_points(_)),
    assertz(total_credits(Semester1Credits)),
    assertz(total_grade_points(Semester1Points)),
    calculate_gpa(Semester1GPA),
    format('GPA for Semester 1: ~2f~n', [Semester1GPA]),

    % Calculate Semester 2 GPA
    semester2_data(Semester2Modules),
    calculate_totals(Semester2Modules, Semester2Credits, Semester2Points),
    retractall(total_credits(_)),
    retractall(total_grade_points(_)),
    assertz(total_credits(Semester2Credits)),
    assertz(total_grade_points(Semester2Points)),
    calculate_gpa(Semester2GPA),
    format('GPA for Semester 2: ~2f~n', [Semester2GPA]),

    % Calculate Cumulative GPA
    calculate_cumulative_gpa(Semester1Credits, Semester1Points, Semester2Credits, Semester2Points, CumulativeGPA),
    format('Cumulative GPA: ~2f~n', [CumulativeGPA]).

% Run the main predicate
:- main.
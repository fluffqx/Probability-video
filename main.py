"""
main.py — Master scene registry for 2MBS10 Manim video series.

Usage:
    # List all scene names in order
    python main.py --list

    # Print manim render commands for all scenes
    python main.py --commands

    # Render a specific scene
    python -m manim -qh week1_probability_spaces.py W1a_p1

    # Render all scenes (slow — use generate_audio.py first)
    python main.py --render-all

Scene naming convention:
    Theory:  W{week}{a/b}_p{N}   e.g. W1a_p1, W6b_p3
    Recap:   FormulaRecapWeek{N} e.g. FormulaRecapWeek1
    Special: NotInCompendium, FinalExamPrep
"""

import sys
import subprocess

# ---------------------------------------------------------------------------
# ORDERED SCENE REGISTRY
# (module_file, scene_class_name, description)
# ---------------------------------------------------------------------------
SCENES = [
    # ── Week 1a: Events and Probabilities ───────────────────────────────────
    ("week1_probability_spaces",   "W1a_p1",  "Motivation: what is probability?"),
    ("week1_probability_spaces",   "W1a_p2",  "Sample space definition"),
    ("week1_probability_spaces",   "W1a_p3",  "Events, sigma-algebras"),
    ("week1_probability_spaces",   "W1a_p4",  "Probability measure — axioms P1-P3"),
    ("week1_probability_spaces",   "W1a_p5",  "Consequences of the axioms"),
    ("week1_probability_spaces",   "W1a_p6",  "Conditional probability"),
    ("week1_probability_spaces",   "W1a_p7",  "Total probability and Bayes"),
    ("week1_probability_spaces",   "W1a_p8",  "Example: HIV test (a)"),
    ("week1_probability_spaces",   "W1a_p9",  "Example: HIV test (b) threshold"),
    ("week1_probability_spaces",   "W1a_p10", "Example: Two-box problem"),
    # ── Week 1b: Independence, Combinatorics ────────────────────────────────
    ("week1_probability_spaces",   "W1b_p1",  "Independence definition"),
    ("week1_probability_spaces",   "W1b_p2",  "Independence under complement — proof"),
    ("week1_probability_spaces",   "W1b_p3",  "Exam: subset and independence"),
    ("week1_probability_spaces",   "W1b_p4",  "Counting — permutations and combinations"),
    ("week1_probability_spaces",   "W1b_p5",  "Example: full house on five dice"),
    ("week1_probability_spaces",   "W1b_p6",  "Example: birthday problem"),
    ("week1_probability_spaces",   "W1b_p7",  "Example: football scores"),
    ("week1_probability_spaces",   "W1b_p8",  "Common mistakes and exam strategy"),
    # ── Week 2a: Discrete Random Variables ──────────────────────────────────
    ("week2_discrete_random_variables", "W2a_p1", "Random variable definition"),
    ("week2_discrete_random_variables", "W2a_p2", "PMF and CDF"),
    ("week2_discrete_random_variables", "W2a_p3", "Expectation and LOTUS"),
    ("week2_discrete_random_variables", "W2a_p4", "Variance"),
    ("week2_discrete_random_variables", "W2a_p5", "Bernoulli and Binomial"),
    ("week2_discrete_random_variables", "W2a_p6", "Geometric and Poisson"),
    ("week2_discrete_random_variables", "W2a_p7", "Example: maximise Bin PMF"),
    ("week2_discrete_random_variables", "W2a_p8", "Example: P(X even) for Binomial"),
    ("week2_discrete_random_variables", "W2a_p9", "Example: exactly one of three events"),
    # ── Week 2b: Geometric, Tail Sum ────────────────────────────────────────
    ("week2_discrete_random_variables", "W2b_p1", "Geometric memoryless property — proof"),
    ("week2_discrete_random_variables", "W2b_p2", "Tail sum formula — proof"),
    ("week2_discrete_random_variables", "W2b_p3", "Application: E[Geom] via tail sum"),
    ("week2_discrete_random_variables", "W2b_p4", "Example: Geometric CDF from scratch"),
    ("week2_discrete_random_variables", "W2b_p5", "Extra: second moment via tail sums"),
    ("week2_discrete_random_variables", "W2b_p6", "Common mistakes and exam strategy"),
    # ── Week 3a: Expectation Algebra ────────────────────────────────────────
    ("week3_expectation_and_continuous", "W3a_p1", "Joint distributions and independence"),
    ("week3_expectation_and_continuous", "W3a_p2", "E[XY] for independent; converse false"),
    ("week3_expectation_and_continuous", "W3a_p3", "Variance of sum and covariance"),
    ("week3_expectation_and_continuous", "W3a_p4", "Best constant predictor a*=E[X]"),
    ("week3_expectation_and_continuous", "W3a_p5", "Example: sum of Binomials"),
    ("week3_expectation_and_continuous", "W3a_p6", "Example: insurance pricing"),
    ("week3_expectation_and_continuous", "W3a_p7", "Example: sum of Geometrics = NegBin"),
    # ── Week 3b: Continuous RVs ─────────────────────────────────────────────
    ("week3_expectation_and_continuous", "W3b_p1", "Continuous RVs — PDF and CDF"),
    ("week3_expectation_and_continuous", "W3b_p2", "Uniform and Exponential"),
    ("week3_expectation_and_continuous", "W3b_p3", "Normal distribution"),
    ("week3_expectation_and_continuous", "W3b_p4", "Example: power-law PDF normalisation"),
    ("week3_expectation_and_continuous", "W3b_p5", "Example: train station"),
    # ── Week 4a: Joint Continuous ───────────────────────────────────────────
    ("week4_joint_distributions", "W4a_p1", "Joint PDF, marginals, independence"),
    ("week4_joint_distributions", "W4a_p2", "Example: triangular support"),
    ("week4_joint_distributions", "W4a_p3", "Example: X^2 transformation"),
    ("week4_joint_distributions", "W4a_p4", "Example: E[e^{-X^2/2}]"),
    # ── Week 4b: Conditional PDF, Tower, Convolution ────────────────────────
    ("week4_joint_distributions", "W4b_p1", "Conditional density"),
    ("week4_joint_distributions", "W4b_p2", "Convolution — PDF of X+Y"),
    ("week4_joint_distributions", "W4b_p3", "Example: joint PDF exam question"),
    ("week4_joint_distributions", "W4b_p4", "Example: tower property verification"),
    # ── Week 5a: Covariance and Correlation ─────────────────────────────────
    ("week5_covariance_and_multivariate", "W5a_p1", "Covariance and correlation"),
    ("week5_covariance_and_multivariate", "W5a_p2", "Cov=0 does NOT imply independence"),
    ("week5_covariance_and_multivariate", "W5a_p3", "Example: E[(X-Y)^2]"),
    ("week5_covariance_and_multivariate", "W5a_p4", "Example: service point optimisation"),
    ("week5_covariance_and_multivariate", "W5a_p5", "Example: half-normal joint density"),
    # ── Week 5b: Jacobian, Normal Sum, Unif+Exp ─────────────────────────────
    ("week5_covariance_and_multivariate", "W5b_p1", "Change of variables — Jacobian"),
    ("week5_covariance_and_multivariate", "W5b_p2", "Example: log transform Unif -> Exp"),
    ("week5_covariance_and_multivariate", "W5b_p3", "Normal closed under convolution"),
    ("week5_covariance_and_multivariate", "W5b_p4", "Example: Unif + Exp density"),
    # ── Week 6a: Generating Functions ───────────────────────────────────────
    ("week6_generating_functions_and_inequalities", "W6a_p1", "PGF definition and properties"),
    ("week6_generating_functions_and_inequalities", "W6a_p2", "PGFs of named distributions"),
    ("week6_generating_functions_and_inequalities", "W6a_p3", "MGF definition and uniqueness"),
    ("week6_generating_functions_and_inequalities", "W6a_p4", "Example: Poisson moments via PGF"),
    ("week6_generating_functions_and_inequalities", "W6a_p5", "Example: coin sum and product covariance"),
    # ── Week 6b: Markov and Chebyshev ───────────────────────────────────────
    ("week6_generating_functions_and_inequalities", "W6b_p1", "Markov's inequality — proof"),
    ("week6_generating_functions_and_inequalities", "W6b_p2", "Chebyshev's inequality — from Markov"),
    ("week6_generating_functions_and_inequalities", "W6b_p3", "Example: standardisation"),
    ("week6_generating_functions_and_inequalities", "W6b_p4", "Example: convergence in dist for max"),
    # ── Week 7: Limit Theorems ───────────────────────────────────────────────
    ("week7_limit_theorems", "W7_p1", "Convergence in probability"),
    ("week7_limit_theorems", "W7_p2", "Convergence in distribution"),
    ("week7_limit_theorems", "W7_p3", "WLLN — proof via Chebyshev"),
    ("week7_limit_theorems", "W7_p4", "CLT — statement"),
    ("week7_limit_theorems", "W7_p5", "CLT — how to use it"),
    ("week7_limit_theorems", "W7_p6", "Example: playlist problem (a)"),
    ("week7_limit_theorems", "W7_p7", "Example: playlist problem (b)"),
    ("week7_limit_theorems", "W7_p8", "Summary: what to memorise"),
    # ── Formula Recaps ───────────────────────────────────────────────────────
    ("formula_sheet_recap", "FormulaRecapWeek1", "Week 1 formula recap"),
    ("formula_sheet_recap", "FormulaRecapWeek2", "Week 2 formula recap"),
    ("formula_sheet_recap", "FormulaRecapWeek3", "Week 3 formula recap"),
    ("formula_sheet_recap", "FormulaRecapWeek4", "Week 4 formula recap"),
    ("formula_sheet_recap", "FormulaRecapWeek5", "Week 5 formula recap"),
    ("formula_sheet_recap", "FormulaRecapWeek6", "Week 6 formula recap"),
    ("formula_sheet_recap", "FormulaRecapWeek7", "Week 7 formula recap"),
    # ── Special ──────────────────────────────────────────────────────────────
    ("formula_sheet_recap", "NotInCompendium",  "Complete NOT-in-compendium list"),
    ("formula_sheet_recap", "FinalExamPrep",    "Exam strategy — all question types"),
]


def list_scenes():
    """Print all scenes in order."""
    print(f"{'#':<4} {'Module':<52} {'Scene':<30} Description")
    print("-" * 110)
    for i, (mod, cls, desc) in enumerate(SCENES, 1):
        print(f"{i:<4} {mod:<52} {cls:<30} {desc}")


def print_commands(quality="-qh"):
    """Print manim render commands for all scenes."""
    for mod, cls, _ in SCENES:
        print(f"python -m manim {quality} {mod}.py {cls}")


def render_all(quality="-ql"):
    """Render all scenes. Use -ql (low quality) for preview, -qh for final."""
    for mod, cls, desc in SCENES:
        print(f"\n{'='*60}")
        print(f"Rendering: {cls}  ({desc})")
        print(f"{'='*60}")
        result = subprocess.run(
            ["python", "-m", "manim", quality, f"{mod}.py", cls],
            capture_output=False
        )
        if result.returncode != 0:
            print(f"ERROR rendering {cls}")


if __name__ == "__main__":
    if "--list" in sys.argv:
        list_scenes()
    elif "--commands" in sys.argv:
        q = "-qh" if "--hq" in sys.argv else "-ql"
        print_commands(q)
    elif "--render-all" in sys.argv:
        q = "-qh" if "--hq" in sys.argv else "-ql"
        render_all(q)
    else:
        print(__doc__)
        print(f"\nTotal scenes: {len(SCENES)}")
        print("\nOptions:")
        print("  python main.py --list              list all scenes")
        print("  python main.py --commands          print render commands (low quality)")
        print("  python main.py --commands --hq     print render commands (high quality)")
        print("  python main.py --render-all        render all scenes (low quality)")
        print("  python main.py --render-all --hq   render all scenes (high quality)")

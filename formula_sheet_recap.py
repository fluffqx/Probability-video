"""
formula_sheet_recap.py
Per-week formula recap scenes + NotInCompendium master list + FinalExamPrep
Each scene is a quick visual summary designed to be watched the night before the exam.
"""

from manim import *
from utils import (
    BG_COLOR, GOLD, PROB_COLOR, RV_COLOR, DIST_COLOR, EX_COLOR,
    COMMENT_COLOR, MEMORISE_COLOR, COMPENDIUM_COLOR,
    ParagraphScene, make_title_card, section_block, label_block,
    safe_scale, gold_box, memorise_label, compendium_label,
    get_mp3_duration, StepSolver
)


class FormulaRecapWeek1(ParagraphScene):
    """Week 1 formula recap: events, probability, conditional, Bayes"""
    MP3_PATH = "narration/audio/paragraphs/FormulaRecapWeek1.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Recap — Week 1", "Events & Probabilities",
                                "G&W Ch. 1; compendium §1.1")
        self.add(title)

        core = VGroup(
            label_block(r"P(A^c)=1-P(A)",
                        "Complement rule  [compendium]", COMPENDIUM_COLOR, eq_fs=28),
            label_block(r"P(A\cup B)=P(A)+P(B)-P(A\cap B)",
                        "Inclusion-exclusion  [compendium]", COMPENDIUM_COLOR, eq_fs=26),
            label_block(r"P(A\mid B)=\frac{P(A\cap B)}{P(B)}",
                        "Conditional probability  [compendium]", COMPENDIUM_COLOR, eq_fs=28),
            label_block(r"P(A)=\sum_i P(B_i)P(A\mid B_i)",
                        "Total probability  [compendium]", COMPENDIUM_COLOR, eq_fs=26),
            label_block(r"P(B_j\mid A)=\frac{P(A\mid B_j)P(B_j)}{\sum_i P(A\mid B_i)P(B_i)}",
                        "Bayes' theorem  [compendium]", COMPENDIUM_COLOR, eq_fs=24),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        safe_scale(core, max_width=13.0, max_height=6.0)
        core.next_to(title, DOWN, buff=0.4)
        self.show(core, wait_time=8.0)

        memorise = section_block([
            "MEMORISE (NOT in compendium):",
            "  Probability space (Omega,F,P) + axioms P1-P3",
            "  Sigma-algebra 3 axioms",
            "  A,B indep => A,B^c indep (proof)",
        ], font_size=23, color=MEMORISE_COLOR)
        memorise.next_to(title, DOWN, buff=0.4)
        self.show_last(memorise)
        self.wait(get_mp3_duration(self.MP3_PATH))


class FormulaRecapWeek2(ParagraphScene):
    """Week 2 formula recap: PMF, CDF, E[X], Var(X), named distributions"""
    MP3_PATH = "narration/audio/paragraphs/FormulaRecapWeek2.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Recap — Week 2", "Discrete Random Variables",
                                "G&W Ch. 2; compendium §1.2, §2")
        self.add(title)

        core = VGroup(
            label_block(r"E[X]=\sum x\,p_X(x),\quad E[g(X)]=\sum g(x)p_X(x)",
                        "Expectation + LOTUS  [compendium §1.2]", COMPENDIUM_COLOR, eq_fs=26),
            label_block(r"\text{Var}(X)=E[X^2]-(E[X])^2",
                        "Variance computing formula  [compendium §1.2]", COMPENDIUM_COLOR, eq_fs=28),
            label_block(r"\text{Bin}(n,p):\;E=np,\;\text{Var}=npq",
                        "Binomial  [compendium §2]", COMPENDIUM_COLOR, eq_fs=28),
            label_block(r"\text{Geom}(p):\;E=1/p,\;\text{Var}=(1-p)/p^2",
                        "Geometric  [compendium §2]", COMPENDIUM_COLOR, eq_fs=28),
            label_block(r"\text{Poi}(\lambda):\;E=\lambda,\;\text{Var}=\lambda",
                        "Poisson  [compendium §2]", COMPENDIUM_COLOR, eq_fs=28),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        safe_scale(core, max_width=13.0, max_height=6.0)
        core.next_to(title, DOWN, buff=0.4)
        self.show(core, wait_time=8.0)

        memorise = section_block([
            "MEMORISE: tail sum proof, memoryless property proof,",
            "sum Bin=Bin (Vandermonde), sum Poi=Poi",
        ], font_size=23)
        memorise.next_to(title, DOWN, buff=0.4)
        mem = memorise_label()
        mem.next_to(memorise, DOWN, buff=0.15)
        self.show_last(VGroup(memorise, mem))
        self.wait(get_mp3_duration(self.MP3_PATH))


class FormulaRecapWeek3(ParagraphScene):
    """Week 3 recap: joint discrete, variance of sum, continuous RVs"""
    MP3_PATH = "narration/audio/paragraphs/FormulaRecapWeek3.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Recap — Week 3", "Expectation Algebra & Continuous RVs",
                                "G&W Ch. 3, Ch. 5; compendium §1.2–1.4, §3")
        self.add(title)

        core = VGroup(
            label_block(r"E[XY]=E[X]E[Y]\text{ if independent}",
                        "Product expectation  [compendium §1.4]", COMPENDIUM_COLOR, eq_fs=28),
            label_block(r"\text{Var}(X+Y)=\text{Var}(X)+\text{Var}(Y)+2\,\text{Cov}(X,Y)",
                        "Variance of sum  [compendium §1.4]", COMPENDIUM_COLOR, eq_fs=24),
            label_block(r"E[g(X)]=\int g(x)f_X(x)\,dx",
                        "LOTUS continuous  [compendium §1.3]", COMPENDIUM_COLOR, eq_fs=28),
            label_block(r"\text{Unif}[a,b]:\;E=\tfrac{a+b}{2},\;\text{Var}=\tfrac{(b-a)^2}{12}",
                        "Uniform  [compendium §3]", COMPENDIUM_COLOR, eq_fs=26),
            label_block(r"\text{Exp}(\lambda):\;E=1/\lambda,\;\text{Var}=1/\lambda^2",
                        "Exponential  [compendium §3]", COMPENDIUM_COLOR, eq_fs=28),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        safe_scale(core, max_width=13.0, max_height=6.0)
        core.next_to(title, DOWN, buff=0.4)
        self.show(core, wait_time=8.0)

        memorise = section_block([
            "MEMORISE: a*=E[X] minimises E[(X-a)^2],",
            "Normal+Normal=Normal, sum Bin=Bin proof",
        ], font_size=23)
        memorise.next_to(title, DOWN, buff=0.4)
        mem = memorise_label()
        mem.next_to(memorise, DOWN, buff=0.15)
        self.show_last(VGroup(memorise, mem))
        self.wait(get_mp3_duration(self.MP3_PATH))


class FormulaRecapWeek4(ParagraphScene):
    """Week 4 recap: joint continuous, marginals, conditional PDF, convolution"""
    MP3_PATH = "narration/audio/paragraphs/FormulaRecapWeek4.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Recap — Week 4", "Joint Continuous Distributions",
                                "G&W Ch. 5–6; compendium §1.3")
        self.add(title)

        core = VGroup(
            label_block(r"f_X(x)=\int f_{X,Y}(x,y)\,dy",
                        "Marginal PDF  [compendium §1.3]", COMPENDIUM_COLOR, eq_fs=28),
            label_block(r"f_{X|Y}(x|y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}",
                        "Conditional PDF  [compendium §1.3]", COMPENDIUM_COLOR, eq_fs=28),
            label_block(r"E[X]=E[E[X\mid Y]]",
                        "Tower property  [compendium §1.4]", COMPENDIUM_COLOR, eq_fs=30),
            label_block(r"f_{X+Y}(z)=\int f_X(t)f_Y(z-t)\,dt",
                        "Convolution formula  [compendium §1.3]", COMPENDIUM_COLOR, eq_fs=26),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        safe_scale(core, max_width=13.0, max_height=5.5)
        core.next_to(title, DOWN, buff=0.4)
        self.show(core, wait_time=7.0)

        memorise = section_block([
            "MEMORISE: non-rectangular support => NOT independent",
            "  (check support BEFORE trying to factor the PDF)",
        ], font_size=23)
        memorise.next_to(title, DOWN, buff=0.4)
        mem = memorise_label()
        mem.next_to(memorise, DOWN, buff=0.15)
        self.show_last(VGroup(memorise, mem))
        self.wait(get_mp3_duration(self.MP3_PATH))


class FormulaRecapWeek5(ParagraphScene):
    """Week 5 recap: covariance, correlation, Jacobian"""
    MP3_PATH = "narration/audio/paragraphs/FormulaRecapWeek5.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Recap — Week 5", "Covariance & Transformations",
                                "G&W Ch. 6–7; compendium §1.4")
        self.add(title)

        core = VGroup(
            label_block(r"\text{Cov}(X,Y)=E[XY]-E[X]E[Y]",
                        "Covariance  [compendium §1.4]", COMPENDIUM_COLOR, eq_fs=28),
            label_block(r"\rho(X,Y)=\text{Cov}(X,Y)/\sqrt{\text{Var}(X)\text{Var}(Y)}",
                        "Correlation, -1<=rho<=1  [compendium §1.4]", COMPENDIUM_COLOR, eq_fs=26),
            label_block(r"f_Y(y)=f_X(g^{-1}(y))\,|dx/dy|",
                        "1D change of variables  [compendium §1.3]", COMPENDIUM_COLOR, eq_fs=28),
            label_block(r"f_{U,V}(u,v)=f_{X,Y}(x,y)\,|J|",
                        "2D Jacobian transformation  [compendium §1.3]", COMPENDIUM_COLOR, eq_fs=28),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        safe_scale(core, max_width=13.0, max_height=5.5)
        core.next_to(title, DOWN, buff=0.4)
        self.show(core, wait_time=7.0)

        memorise = section_block([
            "MEMORISE: Cov=0 does NOT imply independence",
            "  Counterexample: X~Unif[-1,1], Y=X^2",
        ], font_size=23)
        memorise.next_to(title, DOWN, buff=0.4)
        mem = memorise_label()
        mem.next_to(memorise, DOWN, buff=0.15)
        self.show_last(VGroup(memorise, mem))
        self.wait(get_mp3_duration(self.MP3_PATH))


class FormulaRecapWeek6(ParagraphScene):
    """Week 6 recap: PGF, MGF, Markov, Chebyshev"""
    MP3_PATH = "narration/audio/paragraphs/FormulaRecapWeek6.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Recap — Week 6", "Generating Functions & Inequalities",
                                "G&W Ch. 7; compendium §2–3 for PGF/MGF of named dists")
        self.add(title)

        core = VGroup(
            label_block(r"G_X(z)=E[z^X],\quad E[X]=G'(1)",
                        "PGF and mean  [compendium §2]", COMPENDIUM_COLOR, eq_fs=28),
            label_block(r"M_X(t)=E[e^{tX}],\quad E[X^k]=M^{(k)}(0)",
                        "MGF and moments  [compendium §2–3]", COMPENDIUM_COLOR, eq_fs=26),
            label_block(r"G_{X+Y}=G_X G_Y,\;M_{X+Y}=M_X M_Y\;(\text{indep})",
                        "Sum: multiply generating functions  [compendium §2]", COMPENDIUM_COLOR, eq_fs=24),
            label_block(r"P(X\geq t)\leq E[X]/t\quad(X\geq 0,\,t>0)",
                        "Markov's inequality Thm 7.63  [NOT in compendium]", MEMORISE_COLOR, eq_fs=26),
            label_block(r"P(|X-\mu|\geq k)\leq\sigma^2/k^2",
                        "Chebyshev's inequality  [NOT in compendium]", MEMORISE_COLOR, eq_fs=28),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        safe_scale(core, max_width=13.0, max_height=6.0)
        core.next_to(title, DOWN, buff=0.4)
        self.show_last(core)
        self.wait(get_mp3_duration(self.MP3_PATH))


class FormulaRecapWeek7(ParagraphScene):
    """Week 7 recap: convergence, WLLN, CLT"""
    MP3_PATH = "narration/audio/paragraphs/FormulaRecapWeek7.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Recap — Week 7", "Limit Theorems",
                                "Course Handout §3–4  [ALL NOT in compendium]")
        self.add(title)

        core = VGroup(
            label_block(r"X_n\xrightarrow{P}X:\;P(|X_n-X|>\varepsilon)\to 0",
                        "Convergence in probability  [NOT in compendium]", MEMORISE_COLOR, eq_fs=26),
            label_block(r"X_n\xrightarrow{d}X:\;F_{X_n}(x)\to F_X(x)\text{ at cont. pts}",
                        "Convergence in distribution  [NOT in compendium]", MEMORISE_COLOR, eq_fs=24),
            label_block(r"\frac{S_n}{n}\xrightarrow{P}\mu",
                        "WLLN  [NOT in compendium]", MEMORISE_COLOR, eq_fs=32),
            label_block(r"\frac{S_n-n\mu}{\sigma\sqrt{n}}\xrightarrow{d}N(0,1)",
                        "CLT  [NOT in compendium]", MEMORISE_COLOR, eq_fs=30),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        safe_scale(core, max_width=13.0, max_height=5.5)
        core.next_to(title, DOWN, buff=0.4)
        self.show(core, wait_time=8.0)

        memorise = section_block([
            "MEMORISE: WLLN proof via Chebyshev,",
            "counterexample E[X_n]-/->E[X]: X_n=n w.p. 1/n",
        ], font_size=23)
        memorise.next_to(title, DOWN, buff=0.4)
        mem = memorise_label()
        mem.next_to(memorise, DOWN, buff=0.15)
        self.show_last(VGroup(memorise, mem))
        self.wait(get_mp3_duration(self.MP3_PATH))


class NotInCompendium(ParagraphScene):
    """Master scene: complete list of things NOT in the compendium"""
    MP3_PATH = "narration/audio/paragraphs/NotInCompendium.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("EXAM CRITICAL",
                                "Everything NOT in the Compendium",
                                "Must memorise — will be examined without compendium support")
        self.add(title)

        list_a = section_block([
            "DEFINITIONS (must state precisely):",
            "  1. Probability space (Omega, F, P)",
            "  2. Axioms P1-P3 of probability measure",
            "  3. Sigma-algebra — 3 axioms (F1-F3)",
            "  4. Random variable X: Omega -> R",
        ], font_size=24)
        list_a.next_to(title, DOWN, buff=0.45)
        self.show(list_a, wait_time=6.0)

        list_b = section_block([
            "PROOFS (must reproduce):",
            "  5. A,B indep => A,B^c indep",
            "  6. Tail sum E[X] = sum P(X>i) (swap summation)",
            "  7. Geometric memoryless property",
            "  8. a*=E[X] minimises E[(X-a)^2]",
            "  9. Markov's inequality (Theorem 7.63, G&W)",
            " 10. Chebyshev from Markov",
            " 11. WLLN proof via Chebyshev",
        ], font_size=23)
        list_b.next_to(title, DOWN, buff=0.45)
        self.show(list_b, wait_time=8.0)

        list_c = section_block([
            "FACTS + COUNTEREXAMPLES (state + give example):",
            " 12. Sum Bin(m,p)+Bin(n,p) = Bin(m+n,p) [Vandermonde]",
            " 13. Sum Poi(a)+Poi(b) = Poi(a+b)",
            " 14. Cov=0 does NOT imply independence",
            "     Example: X~Unif[-1,1], Y=X^2",
            " 15. Non-rectangular support => NOT independent",
            " 16. Normal+Normal=Normal (closed under convolution)",
            " 17. Conv in dist ≠> E[X_n]->E[X]",
            "     Example: X_n=n w.p. 1/n, 0 otherwise",
        ], font_size=22)
        list_c.next_to(title, DOWN, buff=0.45)
        self.show(list_c, wait_time=9.0)

        list_d = section_block([
            "CONVERGENCE DEFINITIONS (must state precisely):",
            " 18. Convergence in probability",
            " 19. Convergence in distribution",
            " 20. CLT statement (exact form with standardisation)",
        ], font_size=24)
        list_d.next_to(title, DOWN, buff=0.45)
        mem = memorise_label()
        mem.next_to(list_d, DOWN, buff=0.15)
        self.show_last(VGroup(list_d, mem))
        self.wait(get_mp3_duration(self.MP3_PATH))


class FinalExamPrep(ParagraphScene):
    """Exam strategy: how to approach each type of question"""
    MP3_PATH = "narration/audio/paragraphs/FinalExamPrep.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Exam Preparation",
                                "Strategy for Each Question Type",
                                "2MBS10 — Exam Tips")
        self.add(title)

        prob_q = section_block([
            "PROBABILITY / CONDITIONAL PROBABILITY QUESTIONS:",
            "  Define events with letters (A, B, H, T, ...)",
            "  Identify the partition — state it explicitly",
            "  State which theorem: Total Prob or Bayes (with number)",
            "  Compute denominator (P(B)) before numerator",
        ], font_size=24)
        prob_q.next_to(title, DOWN, buff=0.45)
        self.show(prob_q, wait_time=5.0)

        dist_q = section_block([
            "DISTRIBUTION / DENSITY QUESTIONS:",
            "  Name the distribution if possible (Bin, Exp, Normal, ...)",
            "  For transforms: use CDF method or Jacobian",
            "  For joint: check support shape FIRST (rectangular?)",
            "  For independence: f(x,y) = f_X(x)*f_Y(y) for ALL x,y",
        ], font_size=24)
        dist_q.next_to(title, DOWN, buff=0.45)
        self.show(dist_q, wait_time=5.0)

        proof_q = section_block([
            "PROOF QUESTIONS:",
            "  State the starting point (which definition or theorem)",
            "  Write 'by [theorem name]' at each step",
            "  For NOT in compendium proofs: write full argument",
            "  For compendium results: cite section, no re-proof needed",
        ], font_size=24)
        proof_q.next_to(title, DOWN, buff=0.45)
        self.show(proof_q, wait_time=5.0)

        clt_q = section_block([
            "CLT QUESTIONS:",
            "  Identify mu and sigma^2 from distribution",
            "  Write: S_n ~ approx N(n*mu, n*sigma^2)",
            "  Standardise: Z = (x - n*mu) / (sigma*sqrt(n))",
            "  Look up Phi from compendium table §10.1",
            "  For inverse (find n): set up inequality in n, solve",
        ], font_size=24)
        clt_q.next_to(title, DOWN, buff=0.45)
        self.show_last(clt_q)
        self.wait(get_mp3_duration(self.MP3_PATH))

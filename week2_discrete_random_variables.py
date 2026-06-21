"""
week2_discrete_random_variables.py
Week 2a — Discrete Random Variables, PMF, CDF, Expectation, Variance
Week 2b — Named Distributions, Geometric Memorylessness, Tail Sum
Source: G&W Ch. 2 §2.1–2.5, Problems 2.6
"""

from manim import *
from utils import (
    BG_COLOR, GOLD, PROB_COLOR, RV_COLOR, DIST_COLOR, EX_COLOR,
    SAMPLE_COLOR, COMMENT_COLOR, MEMORISE_COLOR, COMPENDIUM_COLOR,
    ParagraphScene, make_title_card, section_block, eq_block,
    label_block, safe_scale, gold_box, memorise_label, compendium_label,
    get_mp3_duration, StepSolver
)


# ============================================================
# WEEK 2a — DISCRETE RANDOM VARIABLES
# ============================================================

class W2a_p1(ParagraphScene):
    """Random variable definition — G&W §2.1 Definition 2.1"""
    MP3_PATH = "narration/audio/paragraphs/W2a_p1.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 2a", "Random Variables",
                                "G&W §2.1, Definition 2.1 [NOT in compendium]")
        self.add(title)

        motivation = section_block([
            "Often we care about a numerical outcome of an experiment,",
            "not the outcome itself.",
            "Example: roll two dice — we care about the sum, not",
            "which specific pair (i,j) appeared.",
            "",
            "A random variable is a function that assigns a number",
            "to each outcome in the sample space.",
        ], font_size=25)
        motivation.next_to(title, DOWN, buff=0.45)
        self.show(motivation, wait_time=5.0)

        defn = label_block(
            r"X : \Omega \to \mathbb{R}",
            "Definition 2.1 (G&W): X is a random variable mapping Omega to R  [NOT in compendium]",
            MEMORISE_COLOR, eq_fs=40)
        defn.next_to(title, DOWN, buff=0.45)
        self.show(defn, wait_time=4.0)

        discrete = section_block([
            "X is discrete if its image Im(X) = {X(omega): omega in Omega}",
            "is a countable subset of R.  (Definition 2.2, G&W)",
            "",
            "Examples: number of heads, number of calls, score on a die.",
        ], font_size=25)
        discrete.next_to(title, DOWN, buff=0.45)
        mem = memorise_label()
        mem.next_to(discrete, DOWN, buff=0.15)
        self.show_last(VGroup(discrete, mem))
        self.wait(get_mp3_duration(self.MP3_PATH))


class W2a_p2(ParagraphScene):
    """PMF and CDF — G&W §2.1 Definitions 2.3, 2.5"""
    MP3_PATH = "narration/audio/paragraphs/W2a_p2.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 2a", "PMF and CDF",
                                "G&W §2.1, Definitions 2.3 and 2.5 [compendium §1.2]")
        self.add(title)

        pmf = label_block(
            r"p_X(x) = P(X = x), \quad \sum_{x \in \text{Im}\,X} p_X(x) = 1",
            "Definition 2.3: probability mass function (PMF)  [compendium §1.2]",
            COMPENDIUM_COLOR, eq_fs=30)
        pmf.next_to(title, DOWN, buff=0.45)
        self.show(pmf, wait_time=5.0)

        cdf = label_block(
            r"F_X(x) = P(X \leq x) = \sum_{k \leq x} p_X(k)",
            "Definition 2.5: cumulative distribution function (CDF)  [compendium §1.2]",
            COMPENDIUM_COLOR, eq_fs=30)
        cdf.next_to(title, DOWN, buff=0.45)
        self.show(cdf, wait_time=5.0)

        props = section_block([
            "Properties of the CDF (all follow from the axioms):",
            "  F is non-decreasing",
            "  lim_{x->-inf} F(x) = 0,   lim_{x->+inf} F(x) = 1",
            "  F is right-continuous: F(x) = lim_{t->x+} F(t)",
            "  P(a < X <= b) = F(b) - F(a)",
        ], font_size=24)
        props.next_to(title, DOWN, buff=0.45)
        self.show_last(props)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W2a_p3(ParagraphScene):
    """Expectation — G&W §2.4 Definition 2.27 and Theorem 2.29 (LOTUS)"""
    MP3_PATH = "narration/audio/paragraphs/W2a_p3.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 2a", "Expectation and LOTUS",
                                "G&W §2.4, Def. 2.27, Theorem 2.29 [compendium §1.2]")
        self.add(title)

        ex_defn = label_block(
            r"E(X) = \sum_{x \in \text{Im}\,X} x\,P(X=x)",
            "Definition 2.27 (G&W): expectation (requires absolute convergence)  [compendium §1.2]",
            COMPENDIUM_COLOR, eq_fs=32)
        ex_defn.next_to(title, DOWN, buff=0.45)
        self.show(ex_defn, wait_time=5.0)

        lotus = label_block(
            r"E(g(X)) = \sum_{x \in \text{Im}\,X} g(x)\,P(X=x)",
            "Theorem 2.29 (G&W): Law of the Unconscious Statistician (LOTUS)  [compendium §1.2]",
            COMPENDIUM_COLOR, eq_fs=30)
        lotus.next_to(title, DOWN, buff=0.45)
        self.show(lotus, wait_time=5.0)

        linearity = label_block(
            r"E(aX+b) = a\,E(X) + b",
            "Theorem 2.30(b): linearity of expectation  [compendium §1.4]",
            COMPENDIUM_COLOR, eq_fs=34)
        linearity.next_to(title, DOWN, buff=0.45)
        self.show_last(linearity)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W2a_p4(ParagraphScene):
    """Variance — G&W §2.4 Definition 2.32"""
    MP3_PATH = "narration/audio/paragraphs/W2a_p4.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 2a", "Variance",
                                "G&W §2.4, Definition 2.32 [compendium §1.2]")
        self.add(title)

        var_defn = label_block(
            r"\text{Var}(X) = E\bigl[(X - E(X))^2\bigr]",
            "Definition 2.32 (G&W): variance measures spread  [compendium §1.2]",
            COMPENDIUM_COLOR, eq_fs=34)
        var_defn.next_to(title, DOWN, buff=0.45)
        self.show(var_defn, wait_time=4.0)

        shortcut = label_block(
            r"\text{Var}(X) = E(X^2) - [E(X)]^2",
            "Computing formula: expand (X-mu)^2 and use linearity  [compendium §1.2]",
            COMPENDIUM_COLOR, eq_fs=34)
        shortcut.next_to(title, DOWN, buff=0.45)
        self.show(shortcut, wait_time=4.0)

        scale = label_block(
            r"\text{Var}(aX+b) = a^2\,\text{Var}(X)",
            "Constants shift don't affect spread; scaling multiplies variance by a^2  [compendium §1.4]",
            COMPENDIUM_COLOR, eq_fs=32)
        scale.next_to(title, DOWN, buff=0.45)
        self.show_last(scale)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W2a_p5(ParagraphScene):
    """Named distributions: Bernoulli, Binomial — G&W §2.2"""
    MP3_PATH = "narration/audio/paragraphs/W2a_p5.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 2a", "Bernoulli & Binomial",
                                "G&W §2.2 [compendium §2]")
        self.add(title)

        bern = label_block(
            r"X \sim \text{Bern}(p): \; P(X=1)=p,\; P(X=0)=1-p",
            "Bernoulli: single trial; E[X]=p, Var(X)=p(1-p)  [compendium §2]",
            COMPENDIUM_COLOR, eq_fs=28)
        bern.next_to(title, DOWN, buff=0.45)
        self.show(bern, wait_time=4.0)

        binom = label_block(
            r"X \sim \text{Bin}(n,p): \; P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}",
            "Binomial: n independent Bern(p) trials  [compendium §2]",
            COMPENDIUM_COLOR, eq_fs=28)
        binom.next_to(title, DOWN, buff=0.45)
        self.show(binom, wait_time=5.0)

        binom_moments = label_block(
            r"E[X] = np, \quad \text{Var}(X) = np(1-p)",
            "Binomial mean and variance  [compendium §2]",
            COMPENDIUM_COLOR, eq_fs=34)
        binom_moments.next_to(title, DOWN, buff=0.45)
        self.show(binom_moments, wait_time=3.0)

        key_fact = section_block([
            "Sum of independent Binomials [NOT in compendium]:",
            "If X~Bin(m,p) and Y~Bin(n,p) independent,",
            "then X+Y ~ Bin(m+n, p).",
            "Proof uses convolution / Vandermonde identity.",
        ], font_size=24)
        key_fact.next_to(title, DOWN, buff=0.45)
        mem = memorise_label()
        mem.next_to(key_fact, DOWN, buff=0.15)
        self.show_last(VGroup(key_fact, mem))
        self.wait(get_mp3_duration(self.MP3_PATH))


class W2a_p6(ParagraphScene):
    """Named distributions: Geometric, Poisson — G&W §2.2"""
    MP3_PATH = "narration/audio/paragraphs/W2a_p6.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 2a", "Geometric & Poisson",
                                "G&W §2.2 [compendium §2]")
        self.add(title)

        geom = label_block(
            r"X \sim \text{Geom}(p): \; P(X=k)=p(1-p)^{k-1},\; k=1,2,\ldots",
            "Geometric: trials until first success  [compendium §2]",
            COMPENDIUM_COLOR, eq_fs=26)
        geom.next_to(title, DOWN, buff=0.45)
        self.show(geom, wait_time=4.0)

        geom_mom = label_block(
            r"E[X] = \frac{1}{p}, \quad \text{Var}(X) = \frac{1-p}{p^2}",
            "Geometric moments  [compendium §2]",
            COMPENDIUM_COLOR, eq_fs=32)
        geom_mom.next_to(title, DOWN, buff=0.45)
        self.show(geom_mom, wait_time=3.0)

        poisson = label_block(
            r"X \sim \text{Poi}(\lambda): \; P(X=k)=\frac{\lambda^k e^{-\lambda}}{k!},\; k=0,1,2,\ldots",
            "Poisson: rare events in large trials  [compendium §2]",
            COMPENDIUM_COLOR, eq_fs=26)
        poisson.next_to(title, DOWN, buff=0.45)
        self.show(poisson, wait_time=4.0)

        poi_mom = label_block(
            r"E[X] = \lambda, \quad \text{Var}(X) = \lambda",
            "Poisson: mean equals variance  [compendium §2]",
            COMPENDIUM_COLOR, eq_fs=32)
        poi_mom.next_to(title, DOWN, buff=0.45)
        self.show(poi_mom, wait_time=3.0)

        poi_sum = section_block([
            "Sum of independent Poissons [NOT in compendium]:",
            "X~Poi(lambda_1), Y~Poi(lambda_2) independent",
            "=> X+Y ~ Poi(lambda_1 + lambda_2).",
        ], font_size=24)
        poi_sum.next_to(title, DOWN, buff=0.45)
        mem = memorise_label()
        mem.next_to(poi_sum, DOWN, buff=0.15)
        self.show_last(VGroup(poi_sum, mem))
        self.wait(get_mp3_duration(self.MP3_PATH))


class W2a_p7(ParagraphScene):
    """Worked example: binomial — Week 2a exercise 1 (maximize PMF)"""
    MP3_PATH = "narration/audio/paragraphs/W2a_p7.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 2a", "Worked Example — Maximize Bin PMF",
                                "Week 2a exercise 1; G&W Exercises 2.1")
        self.add(title)

        setup = section_block([
            "X ~ Bin(n, p). For fixed k in {1,...,n}, find the value of p",
            "that maximises f(p) = P(X_{p,n} = k).",
        ], font_size=26)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=4.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"f(p) = \binom{n}{k} p^k (1-p)^{n-k}",
            "Binomial PMF — Definition 2.2, G&W",
            DIST_COLOR, wait=3.0)
        solver.add_step(2,
            r"\ln f(p) = \text{const} + k\ln p + (n-k)\ln(1-p)",
            "take logarithm to simplify differentiation",
            RV_COLOR, wait=3.0)
        solver.add_step(3,
            r"\frac{d}{dp}\ln f = \frac{k}{p} - \frac{n-k}{1-p} = 0",
            "set derivative to zero",
            RV_COLOR, wait=3.0)
        solver.add_step(4,
            r"k(1-p) = (n-k)p \implies k = np \implies p^* = \frac{k}{n}",
            "solve for p: the mode of Bin(n,p) occurs at p = k/n",
            GOLD, wait=4.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W2a_p8(ParagraphScene):
    """Worked example: P(X even) for Binomial — Week 2a extra exercise"""
    MP3_PATH = "narration/audio/paragraphs/W2a_p8.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 2a", "Worked Example — P(X even) for Binomial",
                                "Week 2a extra exercise; G&W Problems 2.6 no.1")
        self.add(title)

        setup = section_block([
            "X ~ Bin(n, p). Show: P(X is even) = (1 + (1-2p)^n) / 2.",
        ], font_size=26)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=3.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"(p + (1-p))^n = \sum_{k=0}^{n}\binom{n}{k}p^k(1-p)^{n-k} = 1",
            "Binomial theorem with a=p, b=(1-p)",
            PROB_COLOR, wait=3.0)
        solver.add_step(2,
            r"(-p + (1-p))^n = (1-2p)^n = \sum_{k=0}^{n}\binom{n}{k}(-p)^k(1-p)^{n-k}",
            "Binomial theorem with a=-p, b=(1-p)",
            PROB_COLOR, wait=3.0)
        solver.add_step(3,
            r"\frac{1+(1-2p)^n}{2} = \sum_{k \text{ even}}\binom{n}{k}p^k(1-p)^{n-k}",
            "add the two equations; odd-k terms cancel, even-k terms double",
            RV_COLOR, wait=4.0)
        solver.add_step(4,
            r"P(X \text{ even}) = \frac{1+(1-2p)^n}{2}",
            "right side is exactly the sum of Binomial PMF over even k",
            GOLD, wait=3.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W2a_p9(ParagraphScene):
    """Worked example: exactly one of three independent events — Week 2a exam"""
    MP3_PATH = "narration/audio/paragraphs/W2a_p9.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 2a", "Worked Example — Exactly One Event",
                                "Week 2a exam question; independence, Theorem 2.2")
        self.add(title)

        setup = section_block([
            "A, B, C are independent with P(A)=P(B)=P(C)=p.",
            "Find P(exactly one of A,B,C occurs).",
        ], font_size=26)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=4.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"P(\text{exactly one}) = P(A\cap B^c\cap C^c)+P(A^c\cap B\cap C^c)+P(A^c\cap B^c\cap C)",
            "partition: one of three cases by which event occurs",
            PROB_COLOR, wait=4.0)
        solver.add_step(2,
            r"= 3 \cdot P(A)\,P(B^c)\,P(C^c)",
            "mutual independence and symmetry: all three terms are equal",
            RV_COLOR, wait=3.0)
        solver.add_step(3,
            r"= 3p(1-p)^2",
            "substitute P(A)=p, P(B^c)=P(C^c)=1-p",
            GOLD, wait=3.0)
        solver.finalize(wait=2.0)

        check = section_block([
            "Note: this is the Binomial Bin(3,p) probability P(X=1) = C(3,1)p(1-p)^2 = 3p(1-p)^2.",
            "The connection to Binomial confirms the answer.",
        ], font_size=23)
        check.next_to(title, DOWN, buff=5.0)
        self.show_last(check)
        self.wait(get_mp3_duration(self.MP3_PATH))


# ============================================================
# WEEK 2b — GEOMETRIC MEMORYLESSNESS, TAIL SUM
# ============================================================

class W2b_p1(ParagraphScene):
    """Geometric memoryless property — G&W §2.2, Exercise 2.28"""
    MP3_PATH = "narration/audio/paragraphs/W2b_p1.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 2b",
                                "Geometric Distribution — Memoryless Property",
                                "G&W §2.2, Exercise 2.28 [NOT in compendium]")
        self.add(title)

        setup = section_block([
            "X ~ Geom(p): number of tosses until first head.",
            "P(X=k) = p(1-p)^{k-1}.",
            "",
            "Memoryless property: P(X > m+n | X > m) = P(X > n).",
            "Knowing you've already failed m times gives no extra information.",
        ], font_size=25)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=5.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"P(X > k) = \sum_{j=k+1}^{\infty} p(1-p)^{j-1} = (1-p)^k",
            "tail probability of Geometric: geometric series",
            PROB_COLOR, wait=4.0)
        solver.add_step(2,
            r"P(X>m+n \mid X>m) = \frac{P(X>m+n)}{P(X>m)} = \frac{(1-p)^{m+n}}{(1-p)^m}",
            "definition of conditional probability P(A|B)=P(A intersect B)/P(B)",
            RV_COLOR, wait=4.0)
        solver.add_step(3,
            r"= (1-p)^n = P(X > n)",
            "memoryless: the past failures do not matter",
            GOLD, wait=3.0)
        solver.finalize(wait=2.0)

        mem = memorise_label()
        mem.next_to(title, DOWN, buff=5.5)
        self.show_last(mem)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W2b_p2(ParagraphScene):
    """Tail sum formula for expectation — G&W §2.4, Week 2b exam question"""
    MP3_PATH = "narration/audio/paragraphs/W2b_p2.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 2b", "Tail Sum Formula for E[X]",
                                "G&W §2.4 / compendium §1.2; proof NOT in compendium")
        self.add(title)

        statement = label_block(
            r"E[X] = \sum_{i=0}^{\infty} P(X > i) = \sum_{i=1}^{\infty} P(X \geq i)",
            "Tail sum formula: for non-negative integer-valued X  [compendium §1.2 states result]",
            COMPENDIUM_COLOR, eq_fs=28)
        statement.next_to(title, DOWN, buff=0.45)
        self.show(statement, wait_time=5.0)

        proof_intro = section_block([
            "Proof by swapping summation order [NOT in compendium]:",
        ], font_size=26)
        proof_intro.next_to(title, DOWN, buff=0.45)
        self.show(proof_intro, wait_time=2.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"E[X] = \sum_{k=0}^{\infty} k\,P(X=k) = \sum_{k=1}^{\infty} \sum_{i=1}^{k} P(X=k)",
            "write k = 1+1+...+1 (k times) inside the sum",
            RV_COLOR, wait=4.0)
        solver.add_step(2,
            r"= \sum_{i=1}^{\infty} \sum_{k=i}^{\infty} P(X=k)",
            "swap order of summation: i ranges 1 to inf, k ranges i to inf",
            RV_COLOR, wait=4.0)
        solver.add_step(3,
            r"= \sum_{i=1}^{\infty} P(X \geq i)",
            "inner sum = P(X >= i) by definition of tail probability",
            GOLD, wait=3.0)
        solver.finalize(wait=2.0)

        mem = memorise_label()
        mem.next_to(title, DOWN, buff=5.5)
        self.show_last(mem)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W2b_p3(ParagraphScene):
    """Application of tail sum: E[Geom(p)] = 1/p; Week 2b exercise"""
    MP3_PATH = "narration/audio/paragraphs/W2b_p3.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 2b",
                                "Application — E[Geom(p)] via Tail Sum",
                                "Week 2b exercise; G&W §2.2, Problems 2.6")
        self.add(title)

        setup = section_block([
            "X ~ Geom(p). We showed P(X > k) = (1-p)^k.",
            "Use the tail sum formula to derive E[X].",
        ], font_size=26)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=3.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"E[X] = \sum_{i=0}^{\infty} P(X > i) = \sum_{i=0}^{\infty} (1-p)^i",
            "tail sum formula + P(X>i) = (1-p)^i for Geometric",
            PROB_COLOR, wait=4.0)
        solver.add_step(2,
            r"= \frac{1}{1-(1-p)} = \frac{1}{p}",
            "geometric series: sum_{i=0}^inf r^i = 1/(1-r) for |r|<1",
            GOLD, wait=3.0)
        solver.finalize(wait=2.0)

        also = section_block([
            "The tail sum method avoids the delicate calculation",
            "sum_{k=1}^inf k*p*(1-p)^{k-1} directly.",
            "Always consider which method is cleaner for the specific distribution.",
        ], font_size=24)
        also.next_to(title, DOWN, buff=4.8)
        self.show_last(also)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W2b_p4(ParagraphScene):
    """Week 2b exercise: CDF and PMF of geometric (coin flips)"""
    MP3_PATH = "narration/audio/paragraphs/W2b_p4.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 2b",
                                "Worked Example — Geometric CDF from Scratch",
                                "Week 2b recommended exercises, G&W Problems 2.6")
        self.add(title)

        setup = section_block([
            "Biased coin: P(heads)=p. Toss until heads. X = number of tosses.",
            "(1) Find P(X > m).",
            "(2) Find the CDF F_X(x).",
            "(3) Verify the PMF p_X(k) from the CDF.",
        ], font_size=25)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=4.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"P(X > m) = P(\text{first } m \text{ tosses all tails}) = (1-p)^m",
            "X>m means the first m tosses are all tails; tosses are independent",
            PROB_COLOR, wait=4.0)
        solver.add_step(2,
            r"F_X(x) = P(X \leq x) = 1 - P(X > \lfloor x \rfloor) = 1-(1-p)^{\lfloor x\rfloor}",
            "CDF from tail probability; floor because X is integer-valued",
            RV_COLOR, wait=4.0)
        solver.add_step(3,
            r"p_X(k) = F_X(k) - F_X(k-1) = (1-p)^{k-1} - (1-p)^k = p(1-p)^{k-1}",
            "recover PMF from CDF differences — confirms Definition 2.3",
            GOLD, wait=4.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W2b_p5(ParagraphScene):
    """Week 2b extra: sum formula E[E(N^2)-E(N)] = 2*sum i*P(N>i)"""
    MP3_PATH = "narration/audio/paragraphs/W2b_p5.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 2b",
                                "Extra Exercise — Second Moment via Tail Sums",
                                "Week 2b extra exercise")
        self.add(title)

        setup = section_block([
            "Show: sum_{i=0}^inf i*P(N > i) = (E[N^2] - E[N]) / 2",
            "for a random variable N with values in N = {0,1,2,...}.",
            "",
            "Hint: start from sum i*P(N>i) = sum_i sum_{k=i+1}^inf i*P(N=k)",
            "and change summation order.",
        ], font_size=24)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=5.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"\sum_{i=0}^{\infty} i\,P(N>i) = \sum_{i=0}^{\infty} i \sum_{k=i+1}^{\infty} P(N=k)",
            "rewrite P(N>i) as a sum of PMF values",
            PROB_COLOR, wait=4.0)
        solver.add_step(2,
            r"= \sum_{k=1}^{\infty} P(N=k) \sum_{i=0}^{k-1} i = \sum_{k=1}^{\infty} P(N=k)\,\frac{k(k-1)}{2}",
            "swap sums: i runs 0 to k-1; inner sum = k(k-1)/2",
            RV_COLOR, wait=5.0)
        solver.add_step(3,
            r"= \frac{1}{2}\left(\sum_{k=0}^{\infty} k^2 P(N=k) - \sum_{k=0}^{\infty} k\,P(N=k)\right) = \frac{E[N^2]-E[N]}{2}",
            "split k(k-1) = k^2 - k; recognise E[N^2] and E[N]",
            GOLD, wait=5.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W2b_p6(ParagraphScene):
    """Common mistakes and exam strategy for Week 2"""
    MP3_PATH = "narration/audio/paragraphs/W2b_p6.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 2", "Common Mistakes & Exam Strategy",
                                "Week 2 summary")
        self.add(title)

        mistakes = section_block([
            "COMMON MISTAKES:",
            "  x  Writing P(X=k) for a continuous X — use PDF not PMF",
            "  x  Confusing Geom(p) support {1,2,...} vs {0,1,...} versions",
            "  x  Forgetting P(Poi(lambda)) requires lambda > 0",
            "  x  Using E[X^2] = (E[X])^2  — this only holds if Var(X)=0",
        ], font_size=24)
        mistakes.next_to(title, DOWN, buff=0.45)
        self.show(mistakes, wait_time=6.0)

        strategy = section_block([
            "EXAM STRATEGY:",
            "  1. Identify distribution: finite values? -> Binomial/Hypergeom",
            "     Waiting time? -> Geometric. Rare events? -> Poisson.",
            "  2. State parameters explicitly: X ~ Bin(n=10, p=1/3)",
            "  3. Use compendium for E[X], Var(X) — don't rederive",
            "  4. For proofs (tail sum, memoryless): write full argument",
        ], font_size=24)
        strategy.next_to(title, DOWN, buff=0.45)
        self.show_last(strategy)
        self.wait(get_mp3_duration(self.MP3_PATH))

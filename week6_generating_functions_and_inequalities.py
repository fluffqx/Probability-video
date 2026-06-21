"""
week6_generating_functions_and_inequalities.py
Week 6a — PGF, MGF, Characteristic Functions (G&W Ch. 7 §7.1–7.4)
Week 6b — Markov Inequality (G&W Theorem 7.63), Chebyshev (from handout)
Source: G&W Ch. 7 §7.1–7.5; Course Handout §1–2
"""

from manim import *
from utils import (
    BG_COLOR, GOLD, PROB_COLOR, RV_COLOR, DIST_COLOR, EX_COLOR,
    COMMENT_COLOR, MEMORISE_COLOR, COMPENDIUM_COLOR,
    ParagraphScene, make_title_card, section_block, eq_block,
    label_block, safe_scale, gold_box, memorise_label, compendium_label,
    get_mp3_duration, StepSolver
)


# ============================================================
# WEEK 6a — GENERATING FUNCTIONS
# ============================================================

class W6a_p1(ParagraphScene):
    """PGF definition and basic properties — G&W §7.1–7.2"""
    MP3_PATH = "narration/audio/paragraphs/W6a_p1.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 6a", "Probability Generating Functions",
                                "G&W §7.1–7.2 [compendium §2 for each distribution]")
        self.add(title)

        pgf_defn = label_block(
            r"G_X(z) = E[z^X] = \sum_{k=0}^{\infty} P(X=k)\,z^k",
            "PGF: defined for non-negative integer-valued X, |z|<=1  [compendium §2]",
            COMPENDIUM_COLOR, eq_fs=28)
        pgf_defn.next_to(title, DOWN, buff=0.45)
        self.show(pgf_defn, wait_time=5.0)

        moments = label_block(
            r"E[X]=G_X'(1),\quad E[X(X-1)]=G_X''(1)",
            "Extract moments by differentiating at z=1  [compendium §2]",
            COMPENDIUM_COLOR, eq_fs=30)
        moments.next_to(title, DOWN, buff=0.45)
        self.show(moments, wait_time=4.0)

        var_from_pgf = label_block(
            r"\text{Var}(X)=G_X''(1)+G_X'(1)-[G_X'(1)]^2",
            "Variance from PGF: G''(1) + E[X] - (E[X])^2  [compendium §2]",
            COMPENDIUM_COLOR, eq_fs=28)
        var_from_pgf.next_to(title, DOWN, buff=0.45)
        self.show(var_from_pgf, wait_time=4.0)

        sum_indep = label_block(
            r"G_{X+Y}(z)=G_X(z)\,G_Y(z) \text{ if X,Y independent}",
            "Sum: PGF of sum equals product of PGFs (key property)  [compendium §2]",
            COMPENDIUM_COLOR, eq_fs=26)
        sum_indep.next_to(title, DOWN, buff=0.45)
        self.show_last(sum_indep)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W6a_p2(ParagraphScene):
    """PGFs of specific distributions — Bernoulli, Binomial, Geometric, Poisson"""
    MP3_PATH = "narration/audio/paragraphs/W6a_p2.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 6a", "PGFs of Named Distributions",
                                "G&W §7.1 [compendium §2]")
        self.add(title)

        pgfs = VGroup(
            label_block(r"\text{Bern}(p):\;G(z)=1-p+pz",
                        "Bernoulli  [compendium §2]", COMPENDIUM_COLOR, eq_fs=28),
            label_block(r"\text{Bin}(n,p):\;G(z)=(1-p+pz)^n",
                        "Binomial: n independent Bernoulli  [compendium §2]", COMPENDIUM_COLOR, eq_fs=28),
            label_block(r"\text{Geom}(p):\;G(z)=\frac{pz}{1-(1-p)z}",
                        "Geometric  [compendium §2]", COMPENDIUM_COLOR, eq_fs=28),
            label_block(r"\text{Poi}(\lambda):\;G(z)=e^{\lambda(z-1)}",
                        "Poisson  [compendium §2]", COMPENDIUM_COLOR, eq_fs=28),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        safe_scale(pgfs, max_width=13.0, max_height=5.8)
        pgfs.next_to(title, DOWN, buff=0.45)
        self.show_last(pgfs)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W6a_p3(ParagraphScene):
    """MGF definition and uniqueness — G&W §7.4"""
    MP3_PATH = "narration/audio/paragraphs/W6a_p3.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 6a", "Moment Generating Functions",
                                "G&W §7.4 [compendium §2–3]")
        self.add(title)

        mgf_defn = label_block(
            r"M_X(t) = E[e^{tX}] = \sum_{k=0}^{\infty} \frac{t^k}{k!}\,E[X^k]",
            "MGF: defined for t in some interval (-h,h), h>0  [compendium §2–3]",
            COMPENDIUM_COLOR, eq_fs=28)
        mgf_defn.next_to(title, DOWN, buff=0.45)
        self.show(mgf_defn, wait_time=5.0)

        moments_from_mgf = label_block(
            r"E[X^k] = M_X^{(k)}(0) = \left.\frac{d^k}{dt^k}M_X(t)\right|_{t=0}",
            "k-th moment = k-th derivative of MGF evaluated at t=0",
            COMMENT_COLOR, eq_fs=26)
        moments_from_mgf.next_to(title, DOWN, buff=0.45)
        self.show(moments_from_mgf, wait_time=4.0)

        uniqueness = section_block([
            "Uniqueness theorem (G&W Theorem 7.7):",
            "If M_X exists in a neighbourhood of 0, then it uniquely",
            "determines the distribution of X.",
            "",
            "Sum: M_{X+Y}(t) = M_X(t)*M_Y(t) for independent X, Y.",
        ], font_size=24)
        uniqueness.next_to(title, DOWN, buff=0.45)
        self.show_last(uniqueness)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W6a_p4(ParagraphScene):
    """Worked example: Week 6a exercise 1 — Poisson moments via PGF"""
    MP3_PATH = "narration/audio/paragraphs/W6a_p4.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 6a",
                                "Worked Example — Poisson Moments via PGF",
                                "Week 6a exercise 2(a); G&W §7.1")
        self.add(title)

        setup = section_block([
            "X ~ Poi(lambda). Show E[X^n] = lambda*E[(X+1)^{n-1}].",
            "Use this to find E[X^3].",
        ], font_size=26)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=4.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"E[X^n]=\sum_{k=0}^{\infty}k^n\frac{\lambda^k e^{-\lambda}}{k!}=\lambda\sum_{k=1}^{\infty}k^{n-1}\frac{\lambda^{k-1}e^{-\lambda}}{(k-1)!}",
            "write k^n = k * k^{n-1} and cancel k with k! to get (k-1)!",
            PROB_COLOR, wait=5.0)
        solver.add_step(2,
            r"=\lambda\sum_{j=0}^{\infty}(j+1)^{n-1}\frac{\lambda^j e^{-\lambda}}{j!}=\lambda\,E[(X+1)^{n-1}]",
            "substitute j=k-1; recognise Poi(lambda) expectation",
            RV_COLOR, wait=4.0)
        solver.add_step(3,
            r"E[X^3]=\lambda\,E[(X+1)^2]=\lambda(E[X^2]+2E[X]+1)=\lambda(\lambda^2+\lambda+2\lambda+1)",
            "use E[X^2]=lambda^2+lambda (from n=2 case)",
            EX_COLOR, wait=5.0)
        solver.add_step(4,
            r"E[X^3]=\lambda(\lambda^2+3\lambda+1)=\lambda^3+3\lambda^2+\lambda",
            "expand and simplify",
            GOLD, wait=3.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W6a_p5(ParagraphScene):
    """Worked example: covariance of X and Y=product — Week 6a exam"""
    MP3_PATH = "narration/audio/paragraphs/W6a_p5.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 6a", "Worked Example — Coin Sum and Product",
                                "Week 6a exam question")
        self.add(title)

        setup = section_block([
            "Toss fair coin n times: write 1 (heads) or 0 (tails).",
            "X = sum of all results, Y = product of all results.",
            "(a) Are X and Y independent?",
            "(b) Find Cov(X, Y).",
        ], font_size=25)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=5.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"Y=1\iff\text{all heads};\;Y=0\text{ otherwise}",
            "product is 1 only if every result is 1 (heads)",
            PROB_COLOR, wait=3.0)
        solver.add_step(2,
            r"P(Y=1\mid X=n)=1,\;P(Y=1\mid X<n)=0\implies\text{NOT independent}",
            "knowing X=n tells us Y=1 with certainty; not independent",
            MEMORISE_COLOR, wait=4.0)
        solver.add_step(3,
            r"E[XY]=E[X\mid Y=1]\,P(Y=1)=n\cdot(1/2)^n",
            "XY=X when Y=1 (all heads, X=n); XY=0 when Y=0",
            EX_COLOR, wait=4.0)
        solver.add_step(4,
            r"\text{Cov}(X,Y)=E[XY]-E[X]E[Y]=n(1/2)^n-\frac{n}{2}\cdot(1/2)^n=n(1/2)^n\!\left(1-\frac{1}{2}\right)=\frac{n}{2^n}",
            "E[X]=n/2 (Binomial), E[Y]=P(Y=1)=(1/2)^n",
            GOLD, wait=5.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))


# ============================================================
# WEEK 6b — MARKOV AND CHEBYSHEV INEQUALITIES
# ============================================================

class W6b_p1(ParagraphScene):
    """Markov's inequality — G&W Theorem 7.63"""
    MP3_PATH = "narration/audio/paragraphs/W6b_p1.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 6b", "Markov's Inequality",
                                "G&W §7.5, Theorem 7.63 [NOT in compendium]")
        self.add(title)

        motivation = section_block([
            "Question: if we only know E[X], what can we say",
            "about the tail probability P(X >= t)?",
            "",
            "Answer: Markov's inequality gives an upper bound.",
        ], font_size=26)
        motivation.next_to(title, DOWN, buff=0.45)
        self.show(motivation, wait_time=4.0)

        markov = label_block(
            r"P(X \geq t) \leq \frac{E[X]}{t}, \quad X \geq 0,\; t > 0",
            "Theorem 7.63 (G&W) — Markov's inequality  [NOT in compendium]",
            MEMORISE_COLOR, eq_fs=34)
        markov.next_to(title, DOWN, buff=0.45)
        self.show(markov, wait_time=5.0)

        proof = section_block([
            "Proof (G&W §7.5): Let A = {X >= t}.",
            "Key inequality: X >= t * 1_A   (pointwise, for all omega)",
            "Take expectations: E[X] >= t * P(A) = t * P(X >= t).",
            "Divide both sides by t > 0.",
        ], font_size=24)
        proof.next_to(title, DOWN, buff=0.45)
        mem = memorise_label()
        mem.next_to(proof, DOWN, buff=0.15)
        self.show_last(VGroup(proof, mem))
        self.wait(get_mp3_duration(self.MP3_PATH))


class W6b_p2(ParagraphScene):
    """Chebyshev's inequality — derived from Markov; Course Handout §2"""
    MP3_PATH = "narration/audio/paragraphs/W6b_p2.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 6b", "Chebyshev's Inequality",
                                "Course Handout §2 [NOT in compendium]")
        self.add(title)

        chebyshev = label_block(
            r"P(|X-\mu|\geq k)\leq\frac{\sigma^2}{k^2},\quad k>0",
            "Chebyshev's inequality — uses both mean AND variance  [NOT in compendium]",
            MEMORISE_COLOR, eq_fs=32)
        chebyshev.next_to(title, DOWN, buff=0.45)
        self.show(chebyshev, wait_time=5.0)

        derivation = section_block([
            "Proof: apply Markov's inequality to Y = (X - mu)^2:",
            "P((X-mu)^2 >= k^2) <= E[(X-mu)^2] / k^2 = sigma^2 / k^2.",
            "Note: {|X-mu| >= k} = {(X-mu)^2 >= k^2}.",
        ], font_size=24)
        derivation.next_to(title, DOWN, buff=0.45)
        self.show(derivation, wait_time=5.0)

        stronger = section_block([
            "Chebyshev is stronger than Markov because it uses sigma^2.",
            "One-sided version: P(X-mu >= k) <= sigma^2/k^2",
            "  (one-sided tail is a subset of the two-sided event).",
            "",
            "Both Markov and Chebyshev are NOT in the compendium.",
            "Know both statements and the proof of Chebyshev from Markov.",
        ], font_size=23)
        stronger.next_to(title, DOWN, buff=0.45)
        mem = memorise_label()
        mem.next_to(stronger, DOWN, buff=0.15)
        self.show_last(VGroup(stronger, mem))
        self.wait(get_mp3_duration(self.MP3_PATH))


class W6b_p3(ParagraphScene):
    """Worked example: Week 6b exercise 2 — standardise and find Var of (X-mu)/sigma"""
    MP3_PATH = "narration/audio/paragraphs/W6b_p3.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 6b", "Worked Example — Standardisation",
                                "Week 6b exercise 2")
        self.add(title)

        setup = section_block([
            "X has mean mu and variance sigma^2.",
            "Find E[Y] and Var(Y) where Y = (X - mu) / sigma.",
        ], font_size=26)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=3.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"E[Y]=E\!\left[\frac{X-\mu}{\sigma}\right]=\frac{E[X]-\mu}{\sigma}=\frac{\mu-\mu}{\sigma}=0",
            "linearity: E[aX+b]=aE[X]+b with a=1/sigma, b=-mu/sigma",
            EX_COLOR, wait=4.0)
        solver.add_step(2,
            r"\text{Var}(Y)=\text{Var}\!\left(\frac{X}{\sigma}\right)=\frac{\text{Var}(X)}{\sigma^2}=\frac{\sigma^2}{\sigma^2}=1",
            "Var(aX+b) = a^2 Var(X): constant b has no effect",
            DIST_COLOR, wait=4.0)
        solver.add_step(3,
            r"Y=\frac{X-\mu}{\sigma}\text{ is called the standardisation of }X",
            "standardised variable always has mean 0 and variance 1",
            GOLD, wait=3.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W6b_p4(ParagraphScene):
    """Worked example: Week 6b exam — convergence in distribution for max"""
    MP3_PATH = "narration/audio/paragraphs/W6b_p4.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 6b", "Worked Example — Max of i.i.d. RVs",
                                "Week 6b exam question; convergence in distribution")
        self.add(title)

        setup = section_block([
            "Y_i i.i.d. with F_Y(y) = 1 - y^{-alpha} for y >= 1, alpha > 0.",
            "M_n = max(Y_1,...,Y_n). Show n^{-1/alpha}*M_n ->^d M.",
            "Find the distribution of M.",
        ], font_size=24)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=5.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"P(M_n\leq x)=P(Y_1\leq x)^n=[F_Y(x)]^n=(1-x^{-\alpha})^n",
            "CDF of maximum of n i.i.d. RVs = product of individual CDFs",
            PROB_COLOR, wait=4.0)
        solver.add_step(2,
            r"P(n^{-1/\alpha}M_n\leq x)=P(M_n\leq n^{1/\alpha}x)=\left(1-\frac{1}{nx^{\alpha}}\right)^n",
            "scale argument: substitute x -> n^{1/alpha}*x into CDF",
            RV_COLOR, wait=5.0)
        solver.add_step(3,
            r"\to e^{-x^{-\alpha}}\text{ as }n\to\infty\text{ (since }(1-a/n)^n\to e^{-a}\text{)}",
            "standard limit: (1 - a/n)^n -> e^{-a}",
            GOLD, wait=4.0)
        solver.add_step(4,
            r"M\sim\text{Frechet}(\alpha):\;F_M(x)=e^{-x^{-\alpha}},\;x>0",
            "M has the Frechet distribution — a maximum value distribution",
            GOLD, wait=3.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))

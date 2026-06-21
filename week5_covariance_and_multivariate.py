"""
week5_covariance_and_multivariate.py
Week 5a — Covariance, Correlation, Cov=0 counterexample, bivariate expectations
Week 5b — Jacobian transformations, density of sums, normal closed under convolution
Source: G&W Ch. 6 §6.3–6.4, §6.6, §6.8
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
# WEEK 5a — COVARIANCE AND CORRELATION
# ============================================================

class W5a_p1(ParagraphScene):
    """Covariance and correlation definitions — G&W §6.3"""
    MP3_PATH = "narration/audio/paragraphs/W5a_p1.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 5a", "Covariance & Correlation",
                                "G&W §6.3, §7.3 [compendium §1.4]")
        self.add(title)

        cov = label_block(
            r"\text{Cov}(X,Y)=E[(X-\mu_X)(Y-\mu_Y)]=E[XY]-E[X]E[Y]",
            "Covariance: positive when X,Y tend to move together  [compendium §1.4]",
            COMPENDIUM_COLOR, eq_fs=26)
        cov.next_to(title, DOWN, buff=0.45)
        self.show(cov, wait_time=5.0)

        corr = label_block(
            r"\rho(X,Y)=\text{Corr}(X,Y)=\frac{\text{Cov}(X,Y)}{\sqrt{\text{Var}(X)\,\text{Var}(Y)}}",
            "Correlation: normalised covariance; -1 <= rho <= 1  [compendium §1.4]",
            COMPENDIUM_COLOR, eq_fs=28)
        corr.next_to(title, DOWN, buff=0.45)
        self.show(corr, wait_time=5.0)

        props = section_block([
            "Key properties [compendium §1.4]:",
            "  Cov(X,X) = Var(X)",
            "  Cov(aX+b, cY+d) = ac*Cov(X,Y)",
            "  X,Y independent => Cov(X,Y)=0  (converse FALSE!)",
            "  |Corr(X,Y)| = 1 iff Y = aX+b a.s. (perfect linear dependence)",
        ], font_size=24)
        props.next_to(title, DOWN, buff=0.45)
        self.show_last(props)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W5a_p2(ParagraphScene):
    """Cov=0 does NOT imply independence — G&W §7.3, Week 5b ex. 2 also"""
    MP3_PATH = "narration/audio/paragraphs/W5a_p2.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 5a",
                                "Cov = 0 Does NOT Imply Independence",
                                "G&W §7.3 / §3.3 Example 3.22 [NOT in compendium]")
        self.add(title)

        warning = section_block([
            "Independence => Cov = 0.  But Cov = 0 ≠> independence.",
            "",
            "Classic counterexample [NOT in compendium — memorise]:",
            "Let X ~ Unif[-1,1] and Y = X^2.",
        ], font_size=25)
        warning.next_to(title, DOWN, buff=0.45)
        self.show(warning, wait_time=4.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"E[X]=0\;\text{(symmetric)},\quad E[XY]=E[X^3]=\int_{-1}^1 x^3\cdot\tfrac{1}{2}\,dx=0",
            "X^3 is odd on [-1,1], so integral vanishes",
            PROB_COLOR, wait=4.0)
        solver.add_step(2,
            r"\text{Cov}(X,Y)=E[XY]-E[X]E[Y]=0-0=0",
            "covariance is zero",
            DIST_COLOR, wait=3.0)
        solver.add_step(3,
            r"Y=X^2\text{ is a deterministic function of }X \Rightarrow\text{ NOT independent}",
            "knowing X determines Y exactly — extreme dependence!",
            MEMORISE_COLOR, wait=3.0)
        solver.finalize(wait=2.0)

        lesson = section_block([
            "Lesson: Cov measures LINEAR dependence only.",
            "Non-linear dependence (like Y=X^2) can give Cov=0.",
        ], font_size=25)
        lesson.next_to(title, DOWN, buff=5.5)
        self.show_last(lesson)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W5a_p3(ParagraphScene):
    """Worked example: Week 5a exercise 1 — E[(X-Y)^2]"""
    MP3_PATH = "narration/audio/paragraphs/W5a_p3.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 5a", "Worked Example — E[(X-Y)^2]",
                                "Week 5a exercise 1; variance rules")
        self.add(title)

        setup = section_block([
            "X and Y i.i.d. with mean mu and variance sigma^2.",
            "Find E[(X-Y)^2].",
        ], font_size=26)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=3.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"E[(X-Y)^2]=\text{Var}(X-Y)+[E(X-Y)]^2",
            "use E[Z^2] = Var(Z) + (E[Z])^2 with Z=X-Y",
            EX_COLOR, wait=4.0)
        solver.add_step(2,
            r"E[X-Y]=E[X]-E[Y]=\mu-\mu=0",
            "linearity: means are equal",
            RV_COLOR, wait=3.0)
        solver.add_step(3,
            r"\text{Var}(X-Y)=\text{Var}(X)+\text{Var}(Y)=2\sigma^2",
            "X,Y independent: Cov(X,-Y)=-Cov(X,Y)=0, so variances add",
            DIST_COLOR, wait=4.0)
        solver.add_step(4,
            r"E[(X-Y)^2]=2\sigma^2+0=2\sigma^2",
            "same for discrete and continuous (variance rules are universal)",
            GOLD, wait=3.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W5a_p4(ParagraphScene):
    """Worked example: Week 5a exercise 2 — bus service points optimization"""
    MP3_PATH = "narration/audio/paragraphs/W5a_p4.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 5a", "Worked Example — Service Point Optimisation",
                                "Week 5a exercise 2; expectation of Uniform")
        self.add(title)

        setup = section_block([
            "Bus breaks down at X ~ Unif[0,100].",
            "Current: service at 0, 50, 100km.",
            "Proposed: service at 25, 50, 75km.",
            "Which minimises expected distance to nearest service point?",
        ], font_size=24)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=5.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"\text{Current: regions }[0,25),(25,75),(75,100]",
            "nearest service point divides line into three regions",
            PROB_COLOR, wait=3.0)
        solver.add_step(2,
            r"E[D_{\text{current}}]=\frac{1}{100}\left(2\int_0^{25}x\,dx+\int_{25}^{75}|x-50|\,dx\right)",
            "by symmetry: E[D] = (2*integral on [0,25] + integral on [25,75])/100",
            EX_COLOR, wait=5.0)
        solver.add_step(3,
            r"=\frac{1}{100}\left(2\cdot\frac{625}{2}+2\cdot\frac{25^2}{2}\right)=\frac{1}{100}\cdot 1250=12.5\text{ km}",
            "calculate each integral; total = 12.5 km",
            RV_COLOR, wait=5.0)
        solver.add_step(4,
            r"E[D_{\text{proposed}}]=\frac{1}{100}\cdot 3\cdot 2\int_0^{12.5}x\,dx=\frac{6}{100}\cdot\frac{12.5^2}{2}=9.375\text{ km}",
            "proposed: four equal regions of 25km; E[D within each] = 6.25",
            GOLD, wait=5.0)
        solver.finalize(wait=2.0)

        concl = section_block([
            "9.375 < 12.5: yes, the proposed arrangement is better.",
            "Equally spaced points minimise expected distance for uniform breakdowns.",
        ], font_size=24)
        concl.next_to(title, DOWN, buff=5.5)
        self.show_last(concl)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W5a_p5(ParagraphScene):
    """Worked example: Week 5a exam question — joint density with half-normal"""
    MP3_PATH = "narration/audio/paragraphs/W5a_p5.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 5a", "Worked Example — Half-Normal Joint",
                                "Week 5a exam question; G&W §6.1")
        self.add(title)

        setup = section_block([
            "f(x,y) = (sqrt(2)/sqrt(pi)) * (1/x) * e^{-x^2/2}",
            "for 0 <= y <= x, x >= 0.",
            "(a) Marginal of X. (b) Conditional of Y|X=x. (c) E[Y], Var(Y).",
        ], font_size=25)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=5.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"f_X(x)=\int_0^x \frac{\sqrt{2}}{\sqrt{\pi}}\frac{1}{x}e^{-x^2/2}\,dy=\sqrt{\frac{2}{\pi}}e^{-x^2/2}",
            "(a) integrate y from 0 to x; this is the half-normal density",
            RV_COLOR, wait=5.0)
        solver.add_step(2,
            r"f_{Y|X}(y|x)=\frac{f(x,y)}{f_X(x)}=\frac{1}{x},\quad 0\leq y\leq x",
            "(b) Y|X=x ~ Unif[0,x]",
            RV_COLOR, wait=4.0)
        solver.add_step(3,
            r"E[Y|X=x]=\frac{x}{2},\quad E[Y]=E\!\left[\frac{X}{2}\right]=\frac{E[X]}{2}=\frac{1}{2}\sqrt{\frac{2}{\pi}}",
            "(c) E[Y] via tower; E[X] = sqrt(2/pi) for half-normal",
            EX_COLOR, wait=5.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))


# ============================================================
# WEEK 5b — JACOBIAN AND DENSITY OF SUMS
# ============================================================

class W5b_p1(ParagraphScene):
    """Change of variables / Jacobian — G&W §6.6"""
    MP3_PATH = "narration/audio/paragraphs/W5b_p1.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 5b", "Change of Variables — Jacobian",
                                "G&W §6.6 [compendium §1.3]")
        self.add(title)

        one_d = label_block(
            r"f_Y(y) = f_X(g^{-1}(y))\left|\frac{d}{dy}g^{-1}(y)\right|",
            "1D change of variables: Y=g(X), X=g^{-1}(Y)  [compendium §1.3]",
            COMPENDIUM_COLOR, eq_fs=28)
        one_d.next_to(title, DOWN, buff=0.45)
        self.show(one_d, wait_time=5.0)

        two_d = label_block(
            r"f_{U,V}(u,v)=f_{X,Y}(h^{-1}(u,v))\,|J|",
            "2D: (U,V)=g(X,Y); Jacobian |J| = |det(d(x,y)/d(u,v))|  [compendium §1.3]",
            COMPENDIUM_COLOR, eq_fs=26)
        two_d.next_to(title, DOWN, buff=0.45)
        self.show(two_d, wait_time=5.0)

        jacob = label_block(
            r"|J| = \left|\det\begin{pmatrix}\partial x/\partial u & \partial x/\partial v\\ \partial y/\partial u & \partial y/\partial v\end{pmatrix}\right|",
            "Jacobian determinant — absolute value of partial derivatives matrix",
            COMMENT_COLOR, eq_fs=28)
        jacob.next_to(title, DOWN, buff=0.45)
        self.show_last(jacob)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W5b_p2(ParagraphScene):
    """Worked example: Y = -log(X), X~Unif[0,1] => Exp(1)"""
    MP3_PATH = "narration/audio/paragraphs/W5b_p2.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 5b", "Worked Example — log Transform",
                                "G&W §6.6; change of variables 1D")
        self.add(title)

        setup = section_block([
            "X ~ Unif[0,1]. Find the PDF of Y = -log(X).",
        ], font_size=26)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=3.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"y=-\log x \implies x=e^{-y},\quad y>0",
            "invert: express x in terms of y",
            RV_COLOR, wait=3.0)
        solver.add_step(2,
            r"\left|\frac{dx}{dy}\right| = e^{-y}",
            "Jacobian for 1D transformation",
            DIST_COLOR, wait=3.0)
        solver.add_step(3,
            r"f_Y(y)=f_X(e^{-y})\cdot e^{-y}=1\cdot e^{-y}=e^{-y},\quad y>0",
            "f_X(x)=1 on [0,1]; substitute x=e^{-y}",
            GOLD, wait=4.0)
        solver.finalize(wait=2.0)

        concl = section_block([
            "Y = -log(X) ~ Exp(1).",
            "This is the inverse CDF / probability integral transform.",
            "Use it to generate Exponential samples from Uniform samples.",
        ], font_size=24)
        concl.next_to(title, DOWN, buff=5.0)
        self.show_last(concl)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W5b_p3(ParagraphScene):
    """Worked example: Week 5b extra — normal sum closed under convolution"""
    MP3_PATH = "narration/audio/paragraphs/W5b_p3.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 5b",
                                "Normal is Closed Under Convolution",
                                "Week 5b extra exercise [NOT in compendium]")
        self.add(title)

        setup = section_block([
            "X~N(0,1), Y~N(0,1) independent.",
            "Show W = aX + bY ~ N(0, a^2+b^2).",
        ], font_size=26)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=4.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"E[W]=aE[X]+bE[Y]=0",
            "linearity of expectation",
            EX_COLOR, wait=3.0)
        solver.add_step(2,
            r"\text{Var}(W)=a^2\text{Var}(X)+b^2\text{Var}(Y)=a^2+b^2",
            "independence: variances add with squared coefficients",
            DIST_COLOR, wait=3.0)
        solver.add_step(3,
            r"f_W(w)=(f_X*f_Y)(w)\text{ — convolution of two Gaussians}",
            "by convolution formula for sum of independent RVs",
            PROB_COLOR, wait=3.0)
        solver.add_step(4,
            r"=\frac{1}{\sqrt{2\pi(a^2+b^2)}}\exp\!\left(-\frac{w^2}{2(a^2+b^2)}\right)",
            "direct computation (completing the square in the convolution integral)",
            GOLD, wait=4.0)
        solver.finalize(wait=2.0)

        mem = memorise_label()
        mem.next_to(title, DOWN, buff=5.5)
        self.show_last(mem)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W5b_p4(ParagraphScene):
    """Worked example: Week 5b exam — density of U+E, Unif+Exp"""
    MP3_PATH = "narration/audio/paragraphs/W5b_p4.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 5b", "Worked Example — Unif + Exp Density",
                                "Week 5b exam question; convolution G&W §6.2")
        self.add(title)

        setup = section_block([
            "U ~ Unif[0,1] and E ~ Exp(1), independent. Find density of Z = U+E.",
        ], font_size=26)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=3.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"f_Z(z)=\int_0^1 f_E(z-u)\,du = \int_0^1 e^{-(z-u)}\mathbf{1}_{z-u>0}\,du",
            "convolution; constraint z-u>0 means u<z",
            PROB_COLOR, wait=4.0)
        solver.add_step(2,
            r"\text{Case }0<z\leq 1:\;f_Z(z)=\int_0^z e^{-(z-u)}\,du=1-e^{-z}",
            "upper limit is z (not 1) since z<1",
            RV_COLOR, wait=4.0)
        solver.add_step(3,
            r"\text{Case }z>1:\;f_Z(z)=\int_0^1 e^{-(z-u)}\,du=e^{-z}(e-1)",
            "upper limit is 1; lower limit is 0 since z>1 ensures z-u>0 for all u in [0,1]",
            RV_COLOR, wait=4.0)
        solver.add_step(4,
            r"f_Z(z)=\begin{cases}1-e^{-z}&0<z\leq 1\\e^{-z}(e-1)&z>1\end{cases}",
            "combined answer: verify by checking f_Z integrates to 1",
            GOLD, wait=4.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))

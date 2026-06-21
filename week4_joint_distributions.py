"""
week4_joint_distributions.py
Week 4a — Joint Continuous Distributions, Marginals, Independence
Week 4b — Conditional Densities, Tower Property, Convolution
Source: G&W Ch. 5 §5.4–5.6, Ch. 6 §6.1–6.3
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
# WEEK 4a — JOINT CONTINUOUS DISTRIBUTIONS
# ============================================================

class W4a_p1(ParagraphScene):
    """Joint PDF, marginals — G&W §5.5"""
    MP3_PATH = "narration/audio/paragraphs/W4a_p1.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 4a", "Joint PDF and Marginals",
                                "G&W §5.5 [compendium §1.3]")
        self.add(title)

        joint = label_block(
            r"P((X,Y)\in A) = \iint_A f_{X,Y}(x,y)\,dx\,dy",
            "Joint PDF: probability = double integral over region A  [compendium §1.3]",
            COMPENDIUM_COLOR, eq_fs=28)
        joint.next_to(title, DOWN, buff=0.45)
        self.show(joint, wait_time=5.0)

        marginals = label_block(
            r"f_X(x)=\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dy,\quad f_Y(y)=\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dx",
            "Marginal PDFs: integrate out the other variable  [compendium §1.3]",
            COMPENDIUM_COLOR, eq_fs=24)
        marginals.next_to(title, DOWN, buff=0.45)
        self.show(marginals, wait_time=5.0)

        indep = label_block(
            r"X,Y\text{ independent}\iff f_{X,Y}(x,y)=f_X(x)\,f_Y(y)\;\forall x,y",
            "Independence for continuous RVs: joint = product of marginals  [compendium §1.3]",
            COMPENDIUM_COLOR, eq_fs=24)
        indep.next_to(title, DOWN, buff=0.45)
        self.show(indep, wait_time=4.0)

        rect = section_block([
            "KEY FACT [NOT in compendium]: if the support of (X,Y)",
            "is NOT a rectangle (e.g. 0<x<y<1), then X and Y",
            "CANNOT be independent, regardless of whether f factors.",
        ], font_size=24)
        rect.next_to(title, DOWN, buff=0.45)
        mem = memorise_label()
        mem.next_to(rect, DOWN, buff=0.15)
        self.show_last(VGroup(rect, mem))
        self.wait(get_mp3_duration(self.MP3_PATH))


class W4a_p2(ParagraphScene):
    """Worked example: joint PDF on triangular support — Week 4b exercise"""
    MP3_PATH = "narration/audio/paragraphs/W4a_p2.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 4a", "Worked Example — Triangular Support",
                                "Week 4b exercise; G&W §5.5")
        self.add(title)

        setup = section_block([
            "f(x,y) = 1/x for 0 < y < x < 1, zero elsewhere.",
            "Show this is a valid joint PDF.",
            "Find marginals of X and Y. Find E[X] and E[Y].",
        ], font_size=26)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=4.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"\int_0^1\int_0^x \frac{1}{x}\,dy\,dx = \int_0^1 1\,dx = 1\;\checkmark",
            "normalisation: integrate y from 0 to x, then x from 0 to 1",
            PROB_COLOR, wait=4.0)
        solver.add_step(2,
            r"f_X(x)=\int_0^x \frac{1}{x}\,dy = 1,\quad 0<x<1",
            "marginal of X: X ~ Unif[0,1]",
            RV_COLOR, wait=3.0)
        solver.add_step(3,
            r"f_Y(y)=\int_y^1 \frac{1}{x}\,dx = -\ln y,\quad 0<y<1",
            "marginal of Y: integrate x from y to 1",
            RV_COLOR, wait=4.0)
        solver.add_step(4,
            r"E[X]=\int_0^1 x\cdot 1\,dx=\frac{1}{2},\quad E[Y]=\int_0^1 y(-\ln y)\,dy=\frac{1}{4}",
            "E[X] from Unif[0,1]; E[Y] by parts: integral y*(-ln y)=1/4",
            GOLD, wait=5.0)
        solver.finalize(wait=2.0)

        note = section_block([
            "Note: support is 0<y<x<1 — triangular, not rectangular.",
            "Therefore X and Y are NOT independent even before checking.",
        ], font_size=24)
        note.next_to(title, DOWN, buff=5.5)
        self.show_last(note)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W4a_p3(ParagraphScene):
    """Worked example — Week 4a exam question: density transformation"""
    MP3_PATH = "narration/audio/paragraphs/W4a_p3.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 4a", "Worked Example — X^2 Transformation",
                                "Week 4a exam question; G&W §5.6")
        self.add(title)

        setup = section_block([
            "X ~ Unif[0,1]. Find the PDF of U = X^2.",
        ], font_size=26)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=3.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"F_U(u) = P(X^2 \leq u) = P(X \leq \sqrt{u}),\quad u\in[0,1]",
            "CDF method: P(U<=u) = P(X^2<=u); X>=0 so take positive root",
            PROB_COLOR, wait=4.0)
        solver.add_step(2,
            r"F_U(u) = F_X(\sqrt{u}) = \sqrt{u}",
            "since X ~ Unif[0,1], F_X(x) = x for x in [0,1]",
            RV_COLOR, wait=3.0)
        solver.add_step(3,
            r"f_U(u) = F_U'(u) = \frac{1}{2\sqrt{u}},\quad u\in(0,1)",
            "differentiate the CDF to get the PDF",
            GOLD, wait=3.0)
        solver.finalize(wait=2.0)

        note = section_block([
            "This is the Beta(1/2, 1) distribution — X^2 where X~Unif is NOT uniform.",
            "The CDF method (also called the distribution function technique)",
            "is the standard approach for finding the distribution of a function of X.",
        ], font_size=23)
        note.next_to(title, DOWN, buff=5.0)
        self.show_last(note)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W4a_p4(ParagraphScene):
    """Worked example: E[e^{-X^2/2}] — Week 4a exam question part 2"""
    MP3_PATH = "narration/audio/paragraphs/W4a_p4.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 4a", "Worked Example — E[e^{-X^2/2}]",
                                "Week 4a exam question; LOTUS Theorem 5.58")
        self.add(title)

        setup = section_block([
            "X ~ Exp(1). Show E[e^{-X^2/2}] = sqrt(2*pi)*e * P(Z >= 1)",
            "where Z ~ N(0,1).",
        ], font_size=26)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=4.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"E[e^{-X^2/2}]=\int_0^{\infty}e^{-x^2/2}e^{-x}\,dx",
            "LOTUS with g(x)=e^{-x^2/2} and f_X(x)=e^{-x} for x>=0",
            EX_COLOR, wait=4.0)
        solver.add_step(2,
            r"=e^{1/2}\int_0^{\infty}e^{-(x+1)^2/2}\,dx",
            "complete the square: -x^2/2 - x = -(x+1)^2/2 + 1/2",
            RV_COLOR, wait=4.0)
        solver.add_step(3,
            r"=e^{1/2}\sqrt{2\pi}\int_1^{\infty}\frac{1}{\sqrt{2\pi}}e^{-t^2/2}\,dt",
            "substitute t=x+1; the integral is sqrt(2pi)*P(Z>=1)",
            RV_COLOR, wait=4.0)
        solver.add_step(4,
            r"=\sqrt{2\pi}\,e^{1/2}\,P(Z\geq 1)=\sqrt{2\pi}\,e\cdot P(Z\geq 1)",
            "e^{1/2}*e^{1/2}=e; confirm the claimed form",
            GOLD, wait=4.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))


# ============================================================
# WEEK 4b — CONDITIONAL PDF, TOWER PROPERTY, CONVOLUTION
# ============================================================

class W4b_p1(ParagraphScene):
    """Conditional PDF — G&W §6.1"""
    MP3_PATH = "narration/audio/paragraphs/W4b_p1.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 4b", "Conditional Density",
                                "G&W §6.1 [compendium §1.3]")
        self.add(title)

        cond_pdf = label_block(
            r"f_{X|Y}(x|y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}, \quad f_Y(y)>0",
            "Conditional PDF of X given Y=y  [compendium §1.3]",
            COMPENDIUM_COLOR, eq_fs=30)
        cond_pdf.next_to(title, DOWN, buff=0.45)
        self.show(cond_pdf, wait_time=5.0)

        cond_ex = label_block(
            r"E[X\mid Y=y] = \int_{-\infty}^{\infty} x\,f_{X|Y}(x|y)\,dx",
            "Conditional expectation: expectation using conditional density  [compendium §1.3]",
            COMPENDIUM_COLOR, eq_fs=28)
        cond_ex.next_to(title, DOWN, buff=0.45)
        self.show(cond_ex, wait_time=4.0)

        tower = label_block(
            r"E[X] = E[E[X\mid Y]] = \int E[X\mid Y=y]\,f_Y(y)\,dy",
            "Tower property / Law of Total Expectation  [compendium §1.4]",
            COMPENDIUM_COLOR, eq_fs=26)
        tower.next_to(title, DOWN, buff=0.45)
        self.show_last(tower)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W4b_p2(ParagraphScene):
    """Convolution formula for sum of independent RVs — G&W §6.2"""
    MP3_PATH = "narration/audio/paragraphs/W4b_p2.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 4b", "Convolution — PDF of X+Y",
                                "G&W §6.2 [compendium §1.3]")
        self.add(title)

        convol = label_block(
            r"f_{X+Y}(z) = \int_{-\infty}^{\infty} f_X(t)\,f_Y(z-t)\,dt",
            "Convolution formula: X,Y independent  [compendium §1.3]",
            COMPENDIUM_COLOR, eq_fs=28)
        convol.next_to(title, DOWN, buff=0.45)
        self.show(convol, wait_time=5.0)

        why = section_block([
            "Derivation sketch:",
            "P(X+Y<=z) = integral P(Y<=z-x) f_X(x) dx",
            "Differentiate w.r.t. z to get the PDF formula above.",
            "The limits of integration depend on the supports of X and Y.",
        ], font_size=24)
        why.next_to(title, DOWN, buff=0.45)
        self.show(why, wait_time=4.0)

        example = section_block([
            "Example: X,Y ~ Unif[0,1] independent.",
            "Z = X+Y has a TRIANGULAR distribution on [0,2].",
            "f_Z(z) = z for 0<=z<=1; f_Z(z) = 2-z for 1<z<=2.",
        ], font_size=24)
        example.next_to(title, DOWN, buff=0.45)
        self.show_last(example)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W4b_p3(ParagraphScene):
    """Worked example: joint PDF exam question (Week 4b)"""
    MP3_PATH = "narration/audio/paragraphs/W4b_p3.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 4b", "Worked Example — Joint PDF Exam Question",
                                "Week 4b exam question; G&W §6.1")
        self.add(title)

        setup = section_block([
            "f(x,y) = e^{-y} / (2y),  0 < x < 2y,  0 < y < inf.",
            "(a) Marginal PDF of X (expression OK, no closed form required).",
            "(b) Marginal CDF of Y.",
            "(c) Are X and Y independent?",
        ], font_size=25)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=5.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"f_X(x)=\int_{x/2}^{\infty}\frac{e^{-y}}{2y}\,dy,\quad x>0",
            "(a) integrate out y; lower limit y=x/2 from constraint x<2y",
            RV_COLOR, wait=4.0)
        solver.add_step(2,
            r"f_Y(y)=\int_0^{2y}\frac{e^{-y}}{2y}\,dx=e^{-y},\quad y>0",
            "(b) integrate x from 0 to 2y; Y ~ Exp(1)",
            RV_COLOR, wait=4.0)
        solver.add_step(3,
            r"F_Y(y) = \int_0^y e^{-t}\,dt = 1-e^{-y},\quad y>0",
            "CDF of Exp(1)",
            PROB_COLOR, wait=3.0)
        solver.add_step(4,
            r"\text{Support: }0<x<2y\text{ — NOT rectangular} \implies \text{NOT independent}",
            "(c) non-rectangular support: conclusion is immediate",
            MEMORISE_COLOR, wait=3.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W4b_p4(ParagraphScene):
    """Tower property verification; conditional expectation"""
    MP3_PATH = "narration/audio/paragraphs/W4b_p4.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 4b", "Worked Example — Tower Property",
                                "G&W §6.1; Tower property (Law of Total Expectation)")
        self.add(title)

        setup = section_block([
            "Joint PDF: f(x,y) = 2 for 0 < x < y < 1.",
            "We found: E[X|Y=y] = y/2 and f_Y(y) = 2y.",
            "Verify the tower property: E[E[X|Y]] = E[X].",
        ], font_size=25)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=4.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"E[E[X\mid Y]]=\int_0^1 E[X\mid Y=y]\cdot f_Y(y)\,dy",
            "law of total expectation: average E[X|Y=y] over Y",
            EX_COLOR, wait=3.0)
        solver.add_step(2,
            r"=\int_0^1 \frac{y}{2}\cdot 2y\,dy = \int_0^1 y^2\,dy = \frac{1}{3}",
            "substitute E[X|Y=y]=y/2 and f_Y(y)=2y",
            EX_COLOR, wait=4.0)
        solver.add_step(3,
            r"E[X]=\int_0^1\int_0^y x\cdot 2\,dx\,dy=\int_0^1 y^2\,dy=\frac{1}{3}\;\checkmark",
            "direct calculation confirms: tower property verified",
            GOLD, wait=4.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))

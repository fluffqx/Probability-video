"""
week3_expectation_and_continuous.py
Week 3a — Expectation Algebra, PGF intro, Named distributions
Week 3b — Continuous RVs, PDF, CDF, Exponential, Normal
Source: G&W Ch. 3 §3.1–3.4, Ch. 5 §5.1–5.4
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
# WEEK 3a — EXPECTATION ALGEBRA
# ============================================================

class W3a_p1(ParagraphScene):
    """Joint distributions and independence of discrete RVs — G&W §3.1–3.3"""
    MP3_PATH = "narration/audio/paragraphs/W3a_p1.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 3a", "Joint Distributions & Independence",
                                "G&W §3.1–3.3, Def. 3.13, Thm. 3.16")
        self.add(title)

        joint = label_block(
            r"p_{X,Y}(x,y) = P(X=x,\,Y=y)",
            "Joint PMF: probability that X=x AND Y=y simultaneously  [compendium §1.2]",
            COMPENDIUM_COLOR, eq_fs=30)
        joint.next_to(title, DOWN, buff=0.45)
        self.show(joint, wait_time=4.0)

        marginals = label_block(
            r"p_X(x) = \sum_y p_{X,Y}(x,y), \quad p_Y(y) = \sum_x p_{X,Y}(x,y)",
            "Marginal PMFs: sum out the other variable  [compendium §1.2]",
            COMPENDIUM_COLOR, eq_fs=28)
        marginals.next_to(title, DOWN, buff=0.45)
        self.show(marginals, wait_time=4.0)

        indep = label_block(
            r"X,Y \text{ independent} \iff p_{X,Y}(x,y)=p_X(x)\,p_Y(y) \;\forall x,y",
            "Definition 3.13 (G&W): independence via joint = product of marginals",
            COMMENT_COLOR, eq_fs=26)
        indep.next_to(title, DOWN, buff=0.45)
        self.show(indep, wait_time=4.0)

        factor = label_block(
            r"p_{X,Y}(x,y) = f(x)g(y) \implies X,Y \text{ independent}",
            "Theorem 3.16 (G&W): factorization into functions of x and y alone suffices",
            COMMENT_COLOR, eq_fs=26)
        factor.next_to(title, DOWN, buff=0.45)
        self.show_last(factor)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W3a_p2(ParagraphScene):
    """E[XY]=E[X]E[Y] for independent; converse false — G&W Thm 3.19, Ex 3.22"""
    MP3_PATH = "narration/audio/paragraphs/W3a_p2.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 3a", "E[XY] for Independent RVs",
                                "G&W §3.3, Theorems 3.19, 3.20, Example 3.22")
        self.add(title)

        thm = label_block(
            r"X,Y \text{ independent} \implies E[XY] = E[X]\,E[Y]",
            "Theorem 3.19 (G&W): independence implies product of expectations",
            COMMENT_COLOR, eq_fs=28)
        thm.next_to(title, DOWN, buff=0.45)
        self.show(thm, wait_time=4.0)

        converse = section_block([
            "CONVERSE IS FALSE (Example 3.22, G&W):",
            "E[XY]=E[X]E[Y] does NOT imply independence.",
            "",
            "Counterexample: X uniform on {-1,0,1}, Y = |X|.",
            "Then E[XY]=E[X|X|]=E[X^2 sign(X)] = (1/3)(-1)+0+(1/3)(1) = 0",
            "and E[X]=0, so E[XY]=E[X]E[Y]=0, yet P(X=0,Y=1)=0 != P(X=0)P(Y=1).",
        ], font_size=23)
        converse.next_to(title, DOWN, buff=0.45)
        mem = memorise_label()
        mem.next_to(converse, DOWN, buff=0.15)
        self.show_last(VGroup(converse, mem))
        self.wait(get_mp3_duration(self.MP3_PATH))


class W3a_p3(ParagraphScene):
    """Variance of sum; Covariance — G&W §3.4"""
    MP3_PATH = "narration/audio/paragraphs/W3a_p3.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 3a", "Variance of a Sum",
                                "G&W §3.4 [compendium §1.4]")
        self.add(title)

        cov_defn = label_block(
            r"\text{Cov}(X,Y) = E[(X-\mu_X)(Y-\mu_Y)] = E[XY]-E[X]E[Y]",
            "Covariance: measures linear dependence  [compendium §1.4]",
            COMPENDIUM_COLOR, eq_fs=28)
        cov_defn.next_to(title, DOWN, buff=0.45)
        self.show(cov_defn, wait_time=5.0)

        var_sum = label_block(
            r"\text{Var}(X+Y) = \text{Var}(X)+\text{Var}(Y)+2\,\text{Cov}(X,Y)",
            "Variance of sum: general formula  [compendium §1.4]",
            COMPENDIUM_COLOR, eq_fs=28)
        var_sum.next_to(title, DOWN, buff=0.45)
        self.show(var_sum, wait_time=4.0)

        indep_case = label_block(
            r"X,Y \text{ indep.} \implies \text{Cov}(X,Y)=0 \implies \text{Var}(X+Y)=\text{Var}(X)+\text{Var}(Y)",
            "Independence => Cov=0 => variances add  [compendium §1.4]",
            COMPENDIUM_COLOR, eq_fs=24)
        indep_case.next_to(title, DOWN, buff=0.45)
        self.show(indep_case, wait_time=4.0)

        general = label_block(
            r"\text{Var}\!\left(\sum_{i=1}^n a_i X_i\right) = \sum_{i=1}^n a_i^2 \text{Var}(X_i) + 2\sum_{i<j} a_i a_j \text{Cov}(X_i,X_j)",
            "General variance of linear combination  [compendium §1.4]",
            COMPENDIUM_COLOR, eq_fs=22)
        general.next_to(title, DOWN, buff=0.45)
        self.show_last(general)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W3a_p4(ParagraphScene):
    """Best constant predictor a* = E[X] minimises MSE — NOT in compendium"""
    MP3_PATH = "narration/audio/paragraphs/W3a_p4.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 3a", "Best Constant Predictor",
                                "G&W §2.4 / Week 5b exercise 2 [NOT in compendium]")
        self.add(title)

        statement = section_block([
            "Claim: a* = E[X] minimises f(a) = E[(X-a)^2].",
            "Proof:",
        ], font_size=26)
        statement.next_to(title, DOWN, buff=0.45)
        self.show(statement, wait_time=3.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"E[(X-a)^2] = E[X^2 - 2aX + a^2] = E[X^2]-2a\,E[X]+a^2",
            "expand and apply linearity of expectation (Theorem 2.30)",
            EX_COLOR, wait=4.0)
        solver.add_step(2,
            r"\frac{d}{da}\bigl(E[X^2]-2a\,E[X]+a^2\bigr) = -2E[X]+2a = 0",
            "differentiate with respect to a and set to zero",
            RV_COLOR, wait=3.0)
        solver.add_step(3,
            r"a^* = E[X]; \quad \frac{d^2}{da^2} = 2 > 0 \text{ (minimum)}",
            "solve: a*=E[X]; second derivative positive confirms minimum",
            GOLD, wait=3.0)
        solver.finalize(wait=2.0)

        mem = memorise_label()
        mem.next_to(title, DOWN, buff=5.5)
        self.show_last(mem)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W3a_p5(ParagraphScene):
    """Worked example: sum of independent Binomials (exam question, Week 3a)"""
    MP3_PATH = "narration/audio/paragraphs/W3a_p5.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 3a", "Worked Example — Sum of Binomials",
                                "Week 3a exam question; G&W §2.2 [NOT in compendium]")
        self.add(title)

        setup = section_block([
            "X_m ~ Bin(m, p) and X_n ~ Bin(n, p) independent.",
            "Find the PMF of X_m + X_n.",
            "",
            "Claim: X_m + X_n ~ Bin(m+n, p). [NOT in compendium]",
        ], font_size=26)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=4.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"P(X_m+X_n=k) = \sum_{j=0}^{k} P(X_m=j)\,P(X_n=k-j)",
            "convolution formula for sum of independent RVs",
            PROB_COLOR, wait=4.0)
        solver.add_step(2,
            r"= \sum_{j=0}^{k}\binom{m}{j}p^j q^{m-j}\binom{n}{k-j}p^{k-j}q^{n-k+j}",
            "substitute Binomial PMFs with q = 1-p",
            PROB_COLOR, wait=4.0)
        solver.add_step(3,
            r"= p^k q^{m+n-k}\sum_{j=0}^{k}\binom{m}{j}\binom{n}{k-j} = \binom{m+n}{k}p^k q^{m+n-k}",
            "Vandermonde identity: sum C(m,j)C(n,k-j) = C(m+n,k)",
            GOLD, wait=5.0)
        solver.finalize(wait=2.0)

        concl = section_block([
            "This shows X_m + X_n ~ Bin(m+n, p).",
            "The Vandermonde identity C(m+n,k) = sum C(m,j)C(n,k-j)",
            "is the key combinatorial fact used in the proof.",
        ], font_size=24)
        concl.next_to(title, DOWN, buff=5.5)
        self.show_last(concl)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W3a_p6(ParagraphScene):
    """Worked example: insurance company — Week 3a exercise 1"""
    MP3_PATH = "narration/audio/paragraphs/W3a_p6.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 3a", "Worked Example — Insurance Pricing",
                                "Week 3a exercise 1; expectation calculation")
        self.add(title)

        setup = section_block([
            "An insurance policy pays x euros if event E occurs.",
            "E occurs with probability p.",
            "For what price should the policy be sold to yield 10% expected profit?",
        ], font_size=25)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=4.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"\text{Let price} = c. \text{Profit} = c - x \cdot \mathbf{1}_E",
            "revenue c minus payout x with probability p",
            RV_COLOR, wait=3.0)
        solver.add_step(2,
            r"E[\text{profit}] = c - x\,P(E) = c - xp",
            "linearity of expectation (Theorem 2.30)",
            EX_COLOR, wait=3.0)
        solver.add_step(3,
            r"E[\text{profit}] = 0.10 \times c \implies c - xp = 0.10c",
            "set expected profit = 10% of price",
            RV_COLOR, wait=3.0)
        solver.add_step(4,
            r"c = \frac{xp}{0.90} = \frac{10xp}{9}",
            "solve for c: price = payout * probability / (1 - profit margin)",
            GOLD, wait=3.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W3a_p7(ParagraphScene):
    """Worked example: geometric sum via induction — Week 3a extra"""
    MP3_PATH = "narration/audio/paragraphs/W3a_p7.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 3a", "Worked Example — Sum of Geometrics",
                                "Week 3a extra exercise; G&W Exercises 3.3")
        self.add(title)

        setup = section_block([
            "X_1,...,X_n i.i.d. Geom(p). Show by induction that",
            "X_1 + ... + X_n ~ NegBin(n, p) (negative binomial).",
            "",
            "NegBin(n,p): P(S=k) = C(k-1,n-1)*p^n*(1-p)^{k-n}, k=n,n+1,...",
        ], font_size=25)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=5.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"\text{Base case } n=1: X_1\sim\text{Geom}(p)=\text{NegBin}(1,p).\;\checkmark",
            "NegBin(1,p) PMF = p*(1-p)^{k-1} = Geom(p) PMF",
            PROB_COLOR, wait=3.0)
        solver.add_step(2,
            r"S_n = S_{n-1}+X_n,\;P(S_n=k)=\sum_{j=n-1}^{k-1}P(S_{n-1}=j)P(X_n=k-j)",
            "inductive step: convolution of NegBin(n-1,p) with Geom(p)",
            PROB_COLOR, wait=5.0)
        solver.add_step(3,
            r"=\sum_{j=n-1}^{k-1}\binom{j-1}{n-2}p^{n-1}q^{j-(n-1)}\cdot pq^{k-j-1}",
            "substitute PMFs; q = 1-p",
            RV_COLOR, wait=4.0)
        solver.add_step(4,
            r"=p^n q^{k-n}\sum_{j=n-1}^{k-1}\binom{j-1}{n-2}=p^n q^{k-n}\binom{k-1}{n-1}",
            "hockey-stick identity: sum C(j-1,n-2) = C(k-1,n-1)",
            GOLD, wait=5.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))


# ============================================================
# WEEK 3b — CONTINUOUS RANDOM VARIABLES
# ============================================================

class W3b_p1(ParagraphScene):
    """Continuous RVs, PDF, CDF — G&W Ch. 5 §5.1–5.2"""
    MP3_PATH = "narration/audio/paragraphs/W3b_p1.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 3b", "Continuous RVs — PDF and CDF",
                                "G&W §5.1–5.2, Def. 5.2 [compendium §1.3]")
        self.add(title)

        intro = section_block([
            "A continuous RV X has a probability density function f_X.",
            "Probabilities are areas under the curve — not point masses.",
            "P(X = x) = 0 for every specific value x.",
        ], font_size=26)
        intro.next_to(title, DOWN, buff=0.45)
        self.show(intro, wait_time=4.0)

        pdf_defn = label_block(
            r"P(a \leq X \leq b) = \int_a^b f_X(x)\,dx, \quad \int_{-\infty}^{\infty}f_X(x)\,dx=1,\;f_X(x)\geq 0",
            "Definition 5.2 (G&W): PDF conditions  [compendium §1.3]",
            COMPENDIUM_COLOR, eq_fs=26)
        pdf_defn.next_to(title, DOWN, buff=0.45)
        self.show(pdf_defn, wait_time=5.0)

        cdf_rel = label_block(
            r"F_X(x)=P(X\leq x)=\int_{-\infty}^x f_X(t)\,dt, \quad f_X(x)=F_X'(x)",
            "CDF-PDF relationship  [compendium §1.3]",
            COMPENDIUM_COLOR, eq_fs=28)
        cdf_rel.next_to(title, DOWN, buff=0.45)
        self.show(cdf_rel, wait_time=4.0)

        lotus = label_block(
            r"E[g(X)] = \int_{-\infty}^{\infty} g(x)\,f_X(x)\,dx",
            "LOTUS for continuous RVs (G&W Theorem 5.58)  [compendium §1.3]",
            COMPENDIUM_COLOR, eq_fs=30)
        lotus.next_to(title, DOWN, buff=0.45)
        self.show_last(lotus)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W3b_p2(ParagraphScene):
    """Uniform and Exponential distributions — G&W §5.3"""
    MP3_PATH = "narration/audio/paragraphs/W3b_p2.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 3b", "Uniform & Exponential Distributions",
                                "G&W §5.3 [compendium §3]")
        self.add(title)

        unif = label_block(
            r"X\sim\text{Unif}[a,b]:\;f(x)=\frac{1}{b-a}\;\text{on }[a,b]",
            "Uniform: E[X]=(a+b)/2, Var(X)=(b-a)^2/12  [compendium §3]",
            COMPENDIUM_COLOR, eq_fs=28)
        unif.next_to(title, DOWN, buff=0.45)
        self.show(unif, wait_time=4.0)

        exp_pdf = label_block(
            r"X\sim\text{Exp}(\lambda):\;f(x)=\lambda e^{-\lambda x},\;x\geq 0",
            "Exponential: models waiting times  [compendium §3]",
            COMPENDIUM_COLOR, eq_fs=30)
        exp_pdf.next_to(title, DOWN, buff=0.45)
        self.show(exp_pdf, wait_time=4.0)

        exp_mom = label_block(
            r"E[X]=\frac{1}{\lambda},\;\text{Var}(X)=\frac{1}{\lambda^2},\;P(X>t)=e^{-\lambda t}",
            "Exponential moments and tail  [compendium §3]",
            COMPENDIUM_COLOR, eq_fs=28)
        exp_mom.next_to(title, DOWN, buff=0.45)
        self.show(exp_mom, wait_time=4.0)

        exp_mem = section_block([
            "Exponential is the continuous analogue of Geometric.",
            "It is the unique memoryless continuous distribution:",
            "P(X > s+t | X > s) = P(X > t).",
        ], font_size=24)
        exp_mem.next_to(title, DOWN, buff=0.45)
        self.show_last(exp_mem)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W3b_p3(ParagraphScene):
    """Normal distribution — G&W §5.4"""
    MP3_PATH = "narration/audio/paragraphs/W3b_p3.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 3b", "Normal Distribution",
                                "G&W §5.4 [compendium §3]")
        self.add(title)

        normal_pdf = label_block(
            r"X\sim N(\mu,\sigma^2):\;f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}",
            "Normal PDF: bell curve centred at mu  [compendium §3]",
            COMPENDIUM_COLOR, eq_fs=26)
        normal_pdf.next_to(title, DOWN, buff=0.45)
        self.show(normal_pdf, wait_time=5.0)

        standard = label_block(
            r"Z=\frac{X-\mu}{\sigma}\sim N(0,1),\quad P(X\leq x)=\Phi\!\left(\frac{x-\mu}{\sigma}\right)",
            "Standardise to Z-score; Phi is the standard normal CDF  [compendium §3]",
            COMPENDIUM_COLOR, eq_fs=26)
        standard.next_to(title, DOWN, buff=0.45)
        self.show(standard, wait_time=5.0)

        closure = section_block([
            "Normal+Normal=Normal [NOT in compendium]:",
            "If X~N(mu_1,sigma_1^2) and Y~N(mu_2,sigma_2^2) independent,",
            "then X+Y ~ N(mu_1+mu_2, sigma_1^2+sigma_2^2).",
            "Proof uses moment generating functions (Week 6).",
        ], font_size=24)
        closure.next_to(title, DOWN, buff=0.45)
        mem = memorise_label()
        mem.next_to(closure, DOWN, buff=0.15)
        self.show_last(VGroup(closure, mem))
        self.wait(get_mp3_duration(self.MP3_PATH))


class W3b_p4(ParagraphScene):
    """Worked example: PDF normalisation and P(interval) — Week 3b exercise 1"""
    MP3_PATH = "narration/audio/paragraphs/W3b_p4.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 3b", "Worked Example — Power-Law PDF",
                                "Week 3b exercise 1; G&W §5.2")
        self.add(title)

        setup = section_block([
            "For what values of C and m is f(x) = C*x^{-2m} (for x>1) a PDF?",
        ], font_size=26)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=3.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"\int_1^{\infty} Cx^{-2m}\,dx \text{ must equal } 1",
            "normalisation condition: integral of PDF = 1",
            PROB_COLOR, wait=3.0)
        solver.add_step(2,
            r"\int_1^{\infty} x^{-2m}\,dx = \left[\frac{x^{-2m+1}}{-2m+1}\right]_1^{\infty}",
            "this converges only if exponent -2m+1 < 0, i.e. m > 1/2",
            RV_COLOR, wait=4.0)
        solver.add_step(3,
            r"\text{For } m>1/2: \int_1^{\infty} x^{-2m}\,dx = \frac{1}{2m-1}",
            "evaluate the improper integral",
            RV_COLOR, wait=3.0)
        solver.add_step(4,
            r"C\cdot\frac{1}{2m-1}=1 \implies C = 2m-1",
            "solve for C; valid for m > 1/2",
            GOLD, wait=3.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W3b_p5(ParagraphScene):
    """Worked example: train station — Uniform RV probability — Week 3b exercise 2"""
    MP3_PATH = "narration/audio/paragraphs/W3b_p5.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 3b", "Worked Example — Train Station",
                                "Week 3b exercise 2; Uniform distribution")
        self.add(title)

        setup = section_block([
            "Trains to A leave every 15 min starting 7:00.",
            "Trains to B leave every 15 min starting 7:05.",
            "Passenger arrives Unif[7:00, 8:00]. Takes the next train.",
            "(a) P(arrives at destination A)?",
        ], font_size=25)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=5.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"\text{In each 15-min cycle: A at 0, B at 5.}",
            "relative to start of cycle: A-train at minute 0, B-train at minute 5",
            PROB_COLOR, wait=3.0)
        solver.add_step(2,
            r"P(\text{takes A}) = P(\text{arrival in }[0,5)\text{ within cycle}) = \frac{5}{15}=\frac{1}{3}",
            "within each 15-min cycle: A is earlier for the first 5 minutes",
            PROB_COLOR, wait=4.0)
        solver.add_step(3,
            r"P(\text{takes B}) = \frac{10}{15}=\frac{2}{3}",
            "B is earlier for the remaining 10 minutes of the cycle",
            GOLD, wait=3.0)
        solver.add_step(4,
            r"\text{Part (b): shift to }[7\!:\!10,8\!:\!10]\text{ — same } 1/3 \text{ by periodicity}",
            "the probability doesn't change: the pattern repeats every 15 min",
            COMMENT_COLOR, wait=3.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))

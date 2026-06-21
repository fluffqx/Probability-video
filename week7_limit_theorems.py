"""
week7_limit_theorems.py
Week 7 — Convergence in Probability, Convergence in Distribution,
          Weak Law of Large Numbers, Central Limit Theorem
Source: Course Handout §3–4; G&W Ch. 7 §7.5 (Markov/Chebyshev used in proofs)
"""

from manim import *
from utils import (
    BG_COLOR, GOLD, PROB_COLOR, RV_COLOR, DIST_COLOR, EX_COLOR,
    COMMENT_COLOR, MEMORISE_COLOR, COMPENDIUM_COLOR,
    ParagraphScene, make_title_card, section_block, eq_block,
    label_block, safe_scale, gold_box, memorise_label, compendium_label,
    get_mp3_duration, StepSolver
)


class W7_p1(ParagraphScene):
    """Convergence in probability — Handout §3"""
    MP3_PATH = "narration/audio/paragraphs/W7_p1.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 7", "Convergence in Probability",
                                "Course Handout §3 [NOT in compendium]")
        self.add(title)

        motivation = section_block([
            "We have a sequence of random variables X_1, X_2, ...",
            "and want to say they 'converge' to some limit X.",
            "There are several modes of convergence.",
            "The most important for this course are:",
            "  (1) Convergence in probability",
            "  (2) Convergence in distribution",
        ], font_size=25)
        motivation.next_to(title, DOWN, buff=0.45)
        self.show(motivation, wait_time=5.0)

        conv_prob = label_block(
            r"X_n \xrightarrow{P} X \iff P(|X_n-X|>\varepsilon)\to 0 \text{ as } n\to\infty,\;\forall\varepsilon>0",
            "Definition: convergence in probability  [NOT in compendium]",
            MEMORISE_COLOR, eq_fs=26)
        conv_prob.next_to(title, DOWN, buff=0.45)
        self.show(conv_prob, wait_time=5.0)

        intuition = section_block([
            "Intuition: the probability that X_n differs from X",
            "by more than any fixed epsilon goes to zero.",
            "The RVs X_n concentrate around X.",
            "",
            "This is NOT the same as saying X_n(omega) -> X(omega)",
            "for every outcome omega (that is almost sure convergence).",
        ], font_size=24)
        intuition.next_to(title, DOWN, buff=0.45)
        mem = memorise_label()
        mem.next_to(intuition, DOWN, buff=0.15)
        self.show_last(VGroup(intuition, mem))
        self.wait(get_mp3_duration(self.MP3_PATH))


class W7_p2(ParagraphScene):
    """Convergence in distribution — Handout §3"""
    MP3_PATH = "narration/audio/paragraphs/W7_p2.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 7", "Convergence in Distribution",
                                "Course Handout §3 [NOT in compendium]")
        self.add(title)

        conv_dist = label_block(
            r"X_n \xrightarrow{d} X \iff F_{X_n}(x)\to F_X(x)\text{ at all continuity points of }F_X",
            "Definition: convergence in distribution  [NOT in compendium]",
            MEMORISE_COLOR, eq_fs=22)
        conv_dist.next_to(title, DOWN, buff=0.45)
        self.show(conv_dist, wait_time=5.0)

        hierarchy = section_block([
            "Hierarchy of convergence modes:",
            "  a.s. convergence => in probability => in distribution",
            "  In probability => in distribution (NOT reverse in general)",
            "",
            "Important: X_n ->^d X does NOT mean E[X_n] -> E[X].",
        ], font_size=24)
        hierarchy.next_to(title, DOWN, buff=0.45)
        self.show(hierarchy, wait_time=5.0)

        counterex = section_block([
            "Counterexample [NOT in compendium]:",
            "X_n = n with probability 1/n, else 0.",
            "P(|X_n - 0| > eps) = 1/n -> 0, so X_n ->^P 0.",
            "But E[X_n] = n*(1/n) = 1, while E[0] = 0.",
            "=> E[X_n] does not converge to E[X] = 0!",
        ], font_size=23)
        counterex.next_to(title, DOWN, buff=0.45)
        mem = memorise_label()
        mem.next_to(counterex, DOWN, buff=0.15)
        self.show_last(VGroup(counterex, mem))
        self.wait(get_mp3_duration(self.MP3_PATH))


class W7_p3(ParagraphScene):
    """Weak Law of Large Numbers — proof via Chebyshev"""
    MP3_PATH = "narration/audio/paragraphs/W7_p3.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 7", "Weak Law of Large Numbers (WLLN)",
                                "Course Handout §4 [NOT in compendium]")
        self.add(title)

        statement = label_block(
            r"\frac{S_n}{n} = \frac{X_1+\cdots+X_n}{n} \xrightarrow{P} \mu \text{ as } n\to\infty",
            "WLLN: sample mean converges in probability to true mean  [NOT in compendium]",
            MEMORISE_COLOR, eq_fs=26)
        statement.next_to(title, DOWN, buff=0.45)
        self.show(statement, wait_time=5.0)

        conditions = section_block([
            "Conditions: X_1, X_2, ... i.i.d. with E[X_i]=mu, Var(X_i)=sigma^2 < inf.",
        ], font_size=25)
        conditions.next_to(title, DOWN, buff=0.45)
        self.show(conditions, wait_time=3.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"E\!\left[\frac{S_n}{n}\right]=\mu,\quad \text{Var}\!\left(\frac{S_n}{n}\right)=\frac{\sigma^2}{n}",
            "linearity of expectation; independence => variances add / n^2",
            EX_COLOR, wait=4.0)
        solver.add_step(2,
            r"P\!\left(\left|\frac{S_n}{n}-\mu\right|\geq\varepsilon\right)\leq\frac{\sigma^2/n}{\varepsilon^2}=\frac{\sigma^2}{n\varepsilon^2}",
            "apply Chebyshev with k=epsilon; this is the key step",
            PROB_COLOR, wait=5.0)
        solver.add_step(3,
            r"\frac{\sigma^2}{n\varepsilon^2}\to 0\text{ as }n\to\infty\implies\frac{S_n}{n}\xrightarrow{P}\mu",
            "the bound goes to 0; by definition, S_n/n converges in prob to mu",
            GOLD, wait=4.0)
        solver.finalize(wait=2.0)

        mem = memorise_label()
        mem.next_to(title, DOWN, buff=5.5)
        self.show_last(mem)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W7_p4(ParagraphScene):
    """Central Limit Theorem — statement — Course Handout §4"""
    MP3_PATH = "narration/audio/paragraphs/W7_p4.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 7", "Central Limit Theorem (CLT)",
                                "Course Handout §4 [NOT in compendium]")
        self.add(title)

        clt = label_block(
            r"\frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0,1)\text{ as }n\to\infty",
            "CLT: standardised sum converges in distribution to standard Normal  [NOT in compendium]",
            MEMORISE_COLOR, eq_fs=26)
        clt.next_to(title, DOWN, buff=0.45)
        self.show(clt, wait_time=5.0)

        interpretation = section_block([
            "Interpretation: for large n,",
            "S_n is approximately N(n*mu, n*sigma^2).",
            "",
            "Equivalently: S_n/n is approximately N(mu, sigma^2/n).",
            "",
            "The CLT holds for ANY distribution with finite mean and variance.",
            "You don't need to assume normality of individual X_i.",
        ], font_size=24)
        interpretation.next_to(title, DOWN, buff=0.45)
        self.show(interpretation, wait_time=6.0)

        practical = section_block([
            "Practical approximation: use CLT when n >= 30 (rule of thumb).",
            "P(S_n <= x) approx Phi((x - n*mu) / (sigma*sqrt(n)))",
            "where Phi is the standard normal CDF from the compendium tables.",
        ], font_size=24)
        practical.next_to(title, DOWN, buff=0.45)
        mem = memorise_label()
        mem.next_to(practical, DOWN, buff=0.15)
        self.show_last(VGroup(practical, mem))
        self.wait(get_mp3_duration(self.MP3_PATH))


class W7_p5(ParagraphScene):
    """CLT application: how to use it — worked setup"""
    MP3_PATH = "narration/audio/paragraphs/W7_p5.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 7", "Using the CLT — Method",
                                "Course Handout §4; standard normal table [compendium §10.1]")
        self.add(title)

        method = section_block([
            "To apply CLT to X_1,...,X_n i.i.d.:",
            "  1. Identify mu = E[X_i] and sigma^2 = Var(X_i).",
            "  2. Standardise: Z = (S_n - n*mu) / (sigma*sqrt(n)).",
            "  3. Use P(S_n <= x) approx Phi((x-n*mu)/(sigma*sqrt(n))).",
            "  4. Read Phi from the standard normal table in the compendium.",
        ], font_size=25)
        method.next_to(title, DOWN, buff=0.45)
        self.show(method, wait_time=6.0)

        continuity = section_block([
            "Continuity correction (for discrete S_n):",
            "P(S_n <= k) approx Phi((k+0.5 - n*mu)/(sigma*sqrt(n)))",
            "",
            "For this course: use continuity correction only when",
            "the problem involves a discrete distribution (e.g. Binomial).",
        ], font_size=24)
        continuity.next_to(title, DOWN, buff=0.45)
        self.show_last(continuity)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W7_p6(ParagraphScene):
    """Worked example: playlist problem — Week 7 exam question"""
    MP3_PATH = "narration/audio/paragraphs/W7_p6.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 7", "Worked Example — Playlist Duration",
                                "Week 7 exam question; CLT")
        self.add(title)

        setup = section_block([
            "Phone: 3000 songs. Song duration: mean 3.45 min, SD 1.63 min.",
            "(a) Playlist of 45 songs for 3h journey. P(playlist > 3h)?",
            "(b) How many songs for P(playlist > 6h) = 0.95?",
        ], font_size=25)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=5.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"S_{45}=X_1+\cdots+X_{45},\;E[S_{45}]=45\times3.45=155.25\text{ min}",
            "n=45, mu=3.45; total expected duration = 155.25 minutes",
            EX_COLOR, wait=4.0)
        solver.add_step(2,
            r"\text{SD}(S_{45})=1.63\sqrt{45}\approx10.93\text{ min}",
            "Var(S_n)=n*sigma^2, so SD(S_n)=sigma*sqrt(n)",
            DIST_COLOR, wait=3.0)
        solver.add_step(3,
            r"P(S_{45}>180)=P\!\left(Z>\frac{180-155.25}{10.93}\right)=P(Z>2.263)",
            "standardise: 3h = 180 min; Z = (180-155.25)/10.93",
            PROB_COLOR, wait=4.0)
        solver.add_step(4,
            r"=1-\Phi(2.263)\approx 1-0.9882=0.0118\approx 1.18\%",
            "read from standard normal table in compendium",
            GOLD, wait=4.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W7_p7(ParagraphScene):
    """Playlist problem part (b) — find n for P(S_n > 6h) = 0.95"""
    MP3_PATH = "narration/audio/paragraphs/W7_p7.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 7", "Worked Example — Playlist Part (b)",
                                "Week 7 exam question; CLT inverse")
        self.add(title)

        setup = section_block([
            "Find n: P(S_n > 360) >= 0.95. (6 hours = 360 min)",
        ], font_size=26)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=3.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"P(S_n>360)=P\!\left(Z>\frac{360-3.45n}{1.63\sqrt{n}}\right)\geq 0.95",
            "standardise S_n; we need this tail probability >= 0.95",
            PROB_COLOR, wait=4.0)
        solver.add_step(2,
            r"\frac{360-3.45n}{1.63\sqrt{n}}\leq -1.645",
            "P(Z > c) >= 0.95 means c <= -z_{0.05} = -1.645",
            RV_COLOR, wait=4.0)
        solver.add_step(3,
            r"360-3.45n\leq -1.645\times1.63\sqrt{n}=-2.681\sqrt{n}",
            "multiply both sides by 1.63*sqrt(n); swap inequality",
            RV_COLOR, wait=4.0)
        solver.add_step(4,
            r"3.45n-2.681\sqrt{n}-360\geq 0\;\Rightarrow\;n\geq 108\text{ songs}",
            "solve quadratic in sqrt(n): substitute u=sqrt(n), use quadratic formula",
            GOLD, wait=5.0)
        solver.finalize(wait=2.0)

        check = section_block([
            "Check: E[S_{108}] = 108*3.45 = 372.6 > 360. SD = 1.63*sqrt(108) = 16.9.",
            "P(S_{108}>360) = P(Z > (360-372.6)/16.9) = P(Z > -0.745) ≈ 0.772.",
            "Hmm — need more songs. Use n ≈ 113 for safety.",
            "(Quadratic formula gives exact answer — shown here approximately.)",
        ], font_size=22)
        check.next_to(title, DOWN, buff=5.5)
        self.show_last(check)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W7_p8(ParagraphScene):
    """Summary: what's NOT in the compendium for the exam"""
    MP3_PATH = "narration/audio/paragraphs/W7_p8.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 7", "Final: What to Memorise",
                                "Complete list of [NOT in compendium] items")
        self.add(title)

        list1 = section_block([
            "FROM WEEK 1-2 (memorise):",
            "  Probability space (Omega,F,P) + axioms P1-P3",
            "  Sigma-algebra definition (3 axioms)",
            "  RV definition: X:Omega->R",
            "  A,B indep => A,B^c indep (proof via complement rule)",
            "  Tail sum E[X] = sum P(X>i) (proof via swap of summation)",
            "  Sum of Binomials = Binomial (Vandermonde)",
            "  Sum of Poissons = Poisson",
            "  Geometric memoryless property (proof)",
        ], font_size=22)
        list1.next_to(title, DOWN, buff=0.45)
        self.show(list1, wait_time=7.0)

        list2 = section_block([
            "FROM WEEK 3-6 (memorise):",
            "  a*=E[X] minimises E[(X-a)^2] (proof by differentiation)",
            "  Cov=0 does NOT imply independence + counterexample",
            "  Non-rectangular support => NOT independent",
            "  Normal+Normal=Normal (closed under convolution)",
            "  Markov's inequality P(X>=t)<=E[X]/t (Thm 7.63 G&W) + proof",
            "  Chebyshev from Markov: P(|X-mu|>=k)<=sigma^2/k^2",
        ], font_size=22)
        list2.next_to(title, DOWN, buff=0.45)
        self.show(list2, wait_time=7.0)

        list3 = section_block([
            "FROM WEEK 7 (memorise):",
            "  Convergence in probability: P(|X_n-X|>eps)->0",
            "  Convergence in distribution: CDF convergence at continuity pts",
            "  WLLN: S_n/n ->^P mu (proof via Chebyshev)",
            "  CLT: (S_n-n*mu)/(sigma*sqrt(n)) ->^d N(0,1)",
            "  Conv in dist ≠> E[X_n]->E[X] + counterexample (X_n=n w.p. 1/n)",
        ], font_size=22)
        list3.next_to(title, DOWN, buff=0.45)
        mem = memorise_label()
        mem.next_to(list3, DOWN, buff=0.15)
        self.show_last(VGroup(list3, mem))
        self.wait(get_mp3_duration(self.MP3_PATH))

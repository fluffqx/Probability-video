"""
week1a_probability_spaces.py
Week 1a — Events and Probabilities
Source: Grimmett & Welsh, Probability: An Introduction, 2nd ed. (2014)
        Chapters 1.1–1.5
Architecture: one Scene per narration paragraph.
"""

from manim import *
from utils import (
    BG_COLOR, GOLD, PROB_COLOR, RV_COLOR, DIST_COLOR, EX_COLOR,
    SAMPLE_COLOR, COMMENT_COLOR, MEMORISE_COLOR, COMPENDIUM_COLOR,
    ParagraphScene, make_title_card, section_block, eq_block,
    label_block, safe_scale, gold_box, memorise_label, compendium_label,
    get_mp3_duration, StepSolver
)

_TITLE = make_title_card("Week 1a", "Events and Probabilities",
                         "G&W Ch. 1 §1.1–1.5")


# ============================================================
# MOTIVATION
# ============================================================

class W1a_p1(ParagraphScene):
    """Motivation: what is probability theory about?"""
    MP3_PATH = "narration/audio/paragraphs/W1a_p1.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 1a", "Events and Probabilities",
                                "G&W Ch. 1 §1.1–1.5")
        self.add(title)

        block = section_block([
            "Probability theory is the mathematical study of",
            "actions whose outcome cannot be predicted in advance.",
            "",
            "Examples: tossing a coin, rolling a die,",
            "measuring the lifetime of a light bulb.",
            "",
            "Our goal: build a precise mathematical framework",
            "that captures randomness and lets us reason about it.",
        ])
        block.next_to(title, DOWN, buff=0.45)
        self.show_last(block)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W1a_p2(ParagraphScene):
    """Sample space definition — G&W §1.2"""
    MP3_PATH = "narration/audio/paragraphs/W1a_p2.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 1a", "Sample Space",
                                "G&W §1.2, Definition 1.1")
        self.add(title)

        defn = section_block([
            "Definition 1.1 (G&W). The set of all possible outcomes",
            "of an experiment is called the sample space,",
            "denoted Omega.",
            "",
            "Each element omega in Omega is called an elementary event.",
        ], font_size=27)
        defn.next_to(title, DOWN, buff=0.45)
        self.show(defn, wait_time=4.0)

        examples = section_block([
            "Examples:",
            "  Fair die:   Omega = {1, 2, 3, 4, 5, 6}",
            "  Coin flip:  Omega = {H, T}",
            "  Lifetime:   Omega = (0, infinity)",
            "  Two coins:  Omega = {HH, HT, TH, TT}",
        ], font_size=26)
        examples.next_to(title, DOWN, buff=0.45)
        self.show_last(examples)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W1a_p3(ParagraphScene):
    """Events as subsets; sigma-algebra — G&W §1.2"""
    MP3_PATH = "narration/audio/paragraphs/W1a_p3.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 1a", "Events and Sigma-Algebras",
                                "G&W §1.2, Definition 1.2")
        self.add(title)

        defn = section_block([
            "An event is a subset A of Omega.",
            "We say event A 'occurs' if the outcome lies in A.",
            "",
            "Set operations on events:",
            "  A union B  =  'A or B occurs'",
            "  A intersect B  =  'both A and B occur'",
            "  A complement  =  'A does not occur'",
        ], font_size=26)
        defn.next_to(title, DOWN, buff=0.45)
        self.show(defn, wait_time=5.0)

        sigma = section_block([
            "A sigma-algebra F on Omega is a collection of subsets",
            "satisfying three axioms (NOT in compendium):",
            "",
            "  (F1)  Omega belongs to F",
            "  (F2)  If A in F, then A-complement in F",
            "  (F3)  If A_1, A_2, ... in F, then",
            "        their union also belongs to F",
        ], font_size=25)
        sigma.next_to(title, DOWN, buff=0.45)

        mem = memorise_label()
        mem.next_to(sigma, DOWN, buff=0.2)
        grp = VGroup(sigma, mem)
        self.show_last(grp)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W1a_p4(ParagraphScene):
    """Probability measure — three axioms P1-P3 — G&W §1.3"""
    MP3_PATH = "narration/audio/paragraphs/W1a_p4.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 1a", "Probability Measure — Axioms",
                                "G&W §1.3, Definition 1.3 [NOT in compendium]")
        self.add(title)

        axioms = section_block([
            "A probability measure P on (Omega, F) satisfies:",
            "",
            "  (P1)  P(A) >= 0  for all A in F",
            "  (P2)  P(Omega) = 1",
            "  (P3)  If A_1, A_2, ... are pairwise disjoint events,",
            "        P(A_1 union A_2 union ...) = P(A_1) + P(A_2) + ...",
            "        (countable additivity)",
        ], font_size=25)
        axioms.next_to(title, DOWN, buff=0.45)
        self.show(axioms, wait_time=6.0)

        triple = section_block([
            "The triple (Omega, F, P) is called a probability space.",
            "",
            "This is the formal foundation of all probability theory.",
            "The three axioms P1-P3 are NOT in the compendium —",
            "you must state them precisely from memory.",
        ], font_size=26)
        triple.next_to(title, DOWN, buff=0.45)
        mem = memorise_label()
        mem.next_to(triple, DOWN, buff=0.2)
        grp = VGroup(triple, mem)
        self.show_last(grp)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W1a_p5(ParagraphScene):
    """Consequences of the axioms — G&W §1.3 Proposition 1.4"""
    MP3_PATH = "narration/audio/paragraphs/W1a_p5.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 1a", "Consequences of the Axioms",
                                "G&W §1.3, Proposition 1.4 [compendium §1.1]")
        self.add(title)

        props = section_block([
            "From P1-P3 we can derive (all in compendium §1.1):",
        ], font_size=26)
        props.next_to(title, DOWN, buff=0.45)
        self.show(props, wait_time=2.0)

        eqs = VGroup(
            label_block(r"P(A^c) = 1 - P(A)",
                        "Complement rule  [compendium]", COMPENDIUM_COLOR),
            label_block(r"P(\emptyset) = 0",
                        "Empty set has probability zero  [compendium]", COMPENDIUM_COLOR),
            label_block(r"P(A \cup B) = P(A)+P(B)-P(A\cap B)",
                        "Boole's law / inclusion-exclusion  [compendium]", COMPENDIUM_COLOR),
            label_block(r"P(A) \leq P(B) \text{ if } A \subseteq B",
                        "Monotonicity  [compendium]", COMPENDIUM_COLOR),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        safe_scale(eqs, max_width=13.0, max_height=5.5)
        eqs.next_to(title, DOWN, buff=0.45)
        self.show_last(eqs)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W1a_p6(ParagraphScene):
    """Conditional probability — definition and intuition — G&W §1.4"""
    MP3_PATH = "narration/audio/paragraphs/W1a_p6.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 1a", "Conditional Probability",
                                "G&W §1.4, Definition 1.15 [compendium §1.1]")
        self.add(title)

        intuition = section_block([
            "Conditional probability answers:",
            "'Given that B occurred, how likely is A?'",
            "",
            "We restrict the sample space to B and re-normalise.",
        ], font_size=26)
        intuition.next_to(title, DOWN, buff=0.45)
        self.show(intuition, wait_time=4.0)

        defn_eq = label_block(
            r"P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0",
            "Definition 1.15 (G&W)  [compendium §1.1]",
            COMPENDIUM_COLOR, eq_fs=38)
        defn_eq.next_to(title, DOWN, buff=0.45)
        self.show(defn_eq, wait_time=5.0)

        chain = label_block(
            r"P(A \cap B) = P(A \mid B)\,P(B) = P(B \mid A)\,P(A)",
            "Chain rule — multiply both sides  [compendium §1.1]",
            COMPENDIUM_COLOR, eq_fs=32)
        chain.next_to(title, DOWN, buff=0.45)
        self.show_last(chain)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W1a_p7(ParagraphScene):
    """Total probability and Bayes' theorem — G&W §1.4"""
    MP3_PATH = "narration/audio/paragraphs/W1a_p7.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 1a", "Total Probability & Bayes",
                                "G&W §1.4, Theorems 1.16–1.17 [compendium §1.1]")
        self.add(title)

        partition = section_block([
            "A partition of Omega: events B_1,...,B_n are",
            "pairwise disjoint and their union is Omega.",
        ], font_size=26)
        partition.next_to(title, DOWN, buff=0.45)
        self.show(partition, wait_time=3.0)

        total = label_block(
            r"P(A) = \sum_{i=1}^{n} P(B_i)\,P(A \mid B_i)",
            "Theorem 1.16 — Total probability  [compendium §1.1]",
            COMPENDIUM_COLOR, eq_fs=32)
        total.next_to(title, DOWN, buff=0.45)
        self.show(total, wait_time=5.0)

        bayes = label_block(
            r"P(B_j \mid A) = \frac{P(A \mid B_j)\,P(B_j)}{\displaystyle\sum_{i=1}^{n} P(A \mid B_i)\,P(B_i)}",
            "Theorem 1.17 — Bayes' theorem  [compendium §1.1]",
            COMPENDIUM_COLOR, eq_fs=30)
        bayes.next_to(title, DOWN, buff=0.45)
        self.show_last(bayes)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W1a_p8(ParagraphScene):
    """Worked example: HIV test — from Week 1a exam question"""
    MP3_PATH = "narration/audio/paragraphs/W1a_p8.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 1a", "Worked Example — HIV Test",
                                "Week 1a exam question; Bayes' Theorem 1.17")
        self.add(title)

        setup = section_block([
            "Given:  P(HIV) = 0.001",
            "        P(+ | no HIV) = 0.01   (false positive)",
            "        P(+ | HIV) = 0.99      (true positive)",
            "",
            "Question: P(HIV | +) = ?",
        ], font_size=26)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=5.0)

        step1 = section_block([
            "We apply Bayes' theorem.",
            "Let H = 'has HIV', T = 'tests positive'.",
            "",
            "Denominator (total probability):",
        ], font_size=24)
        step1.next_to(title, DOWN, buff=0.45)
        self.show(step1, wait_time=3.0)

        denom = label_block(
            r"P(T) = P(T|H)P(H) + P(T|H^c)P(H^c)",
            "Total probability formula applied to partition {H, H^c}",
            COMMENT_COLOR, eq_fs=28)
        denom.next_to(title, DOWN, buff=0.45)
        self.show(denom, wait_time=3.0)

        calc = label_block(
            r"= 0.99\times 0.001 + 0.01\times 0.999 = 0.01098",
            "Substitute the given values", COMMENT_COLOR, eq_fs=30)
        calc.next_to(title, DOWN, buff=0.45)
        self.show(calc, wait_time=3.0)

        final = label_block(
            r"P(H \mid T) = \frac{0.99 \times 0.001}{0.01098} \approx 0.0901",
            "Bayes' theorem: P(H|T) = P(T|H)P(H)/P(T)  — about 9%!",
            GOLD, eq_fs=30)
        final.next_to(title, DOWN, buff=0.45)
        box = gold_box(final)
        grp = VGroup(final, box)
        self.show_last(grp)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W1a_p9(ParagraphScene):
    """Part (b) of HIV test: finding threshold for false positive"""
    MP3_PATH = "narration/audio/paragraphs/W1a_p9.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 1a", "Worked Example — HIV Test (b)",
                                "Week 1a exam question, part (b)")
        self.add(title)

        q = section_block([
            "Question (b): How small must P(+ | no HIV) = epsilon be",
            "so that P(HIV | +) > 0.99?",
        ], font_size=26)
        q.next_to(title, DOWN, buff=0.45)
        self.show(q, wait_time=3.0)

        setup = label_block(
            r"P(H|T) = \frac{0.99 \times 0.001}{0.99\times 0.001 + \varepsilon\times 0.999} > 0.99",
            "Set up the Bayes inequality in terms of epsilon", COMMENT_COLOR, eq_fs=26)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=4.0)

        solve = section_block([
            "Rearranging: 0.99 * 0.001 > 0.99 * (0.99*0.001 + epsilon*0.999)",
            "=> 0.00099 > 0.99*0.00099 + 0.99*epsilon*0.999",
            "=> 0.00099*(1 - 0.99) > 0.99*0.999*epsilon",
            "=> epsilon < 0.00099 * 0.01 / (0.99*0.999) ≈ 0.00001",
        ], font_size=23)
        solve.next_to(title, DOWN, buff=0.45)
        self.show(solve, wait_time=5.0)

        conclusion = section_block([
            "The false positive rate must be below about 0.001%.",
            "This shows how rare a disease makes correct diagnosis hard",
            "even with a highly accurate test — a key exam insight.",
        ], font_size=25)
        conclusion.next_to(title, DOWN, buff=0.45)
        self.show_last(conclusion)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W1a_p10(ParagraphScene):
    """Worked example: Box problem — Total probability with Bayes"""
    MP3_PATH = "narration/audio/paragraphs/W1a_p10.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 1a", "Worked Example — Two Boxes",
                                "Week 1a exercise 2; Bayes Theorem 1.17")
        self.add(title)

        setup = section_block([
            "Box 1: 3 white, 7 black balls.",
            "Box 2: 6 white, 4 black balls.",
            "Transfer one ball from Box 1 to Box 2.",
            "Draw from Box 2 — it's white. P(transferred ball was white)?",
        ], font_size=25)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=5.0)

        step1 = section_block([
            "Let W1 = 'transferred ball was white' (prior: P(W1) = 3/10).",
            "Let W2 = 'ball drawn from Box 2 is white'.",
            "",
            "Likelihoods:",
            "  P(W2 | W1) = 7/11   (Box 2 now has 7 white out of 11)",
            "  P(W2 | W1^c) = 6/11 (Box 2 has 6 white out of 11)",
        ], font_size=24)
        step1.next_to(title, DOWN, buff=0.45)
        self.show(step1, wait_time=6.0)

        bayes_calc = label_block(
            r"P(W_1 \mid W_2) = \frac{\tfrac{7}{11}\cdot\tfrac{3}{10}}{\tfrac{7}{11}\cdot\tfrac{3}{10} + \tfrac{6}{11}\cdot\tfrac{7}{10}} = \frac{21}{21+42} = \frac{1}{3}",
            "Bayes' theorem — substitute and simplify", GOLD, eq_fs=26)
        bayes_calc.next_to(title, DOWN, buff=0.45)
        box = gold_box(bayes_calc)
        self.show_last(VGroup(bayes_calc, box))
        self.wait(get_mp3_duration(self.MP3_PATH))


# ============================================================
# WEEK 1b — Independence, Combinatorics
# ============================================================

class W1b_p1(ParagraphScene):
    """Independence definition — G&W §1.5 Definition 1.22"""
    MP3_PATH = "narration/audio/paragraphs/W1b_p1.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 1b", "Independence of Events",
                                "G&W §1.5, Definition 1.22 [compendium §1.1]")
        self.add(title)

        intro = section_block([
            "Intuitively: A and B are independent if knowing B",
            "happened gives no information about A.",
        ], font_size=26)
        intro.next_to(title, DOWN, buff=0.45)
        self.show(intro, wait_time=3.0)

        defn = label_block(
            r"A \text{ and } B \text{ are independent} \iff P(A \cap B) = P(A)\,P(B)",
            "Definition 1.22 (G&W)  [compendium §1.1]",
            COMPENDIUM_COLOR, eq_fs=30)
        defn.next_to(title, DOWN, buff=0.45)
        self.show(defn, wait_time=5.0)

        equiv = label_block(
            r"P(A \cap B) = P(A)P(B) \iff P(A \mid B) = P(A) \text{ (if } P(B)>0\text{)}",
            "Equivalent formulation via conditional probability", COMMENT_COLOR, eq_fs=26)
        equiv.next_to(title, DOWN, buff=0.45)
        self.show(equiv, wait_time=4.0)

        mutual = section_block([
            "Mutual independence of A_1,...,A_n (G&W §1.5):",
            "P(A_{i1} intersect ... intersect A_{ik}) = P(A_{i1})*...*P(A_{ik})",
            "for ALL subsets {i1,...,ik} of {1,...,n}.",
            "",
            "Pairwise independence does NOT imply mutual independence!",
        ], font_size=24)
        mutual.next_to(title, DOWN, buff=0.45)
        self.show_last(mutual)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W1b_p2(ParagraphScene):
    """Independence: A,B independent => A, B^c independent. Proof."""
    MP3_PATH = "narration/audio/paragraphs/W1b_p2.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 1b",
                                "Independence Preserved Under Complement",
                                "G&W §1.5, Proposition 1.23 [NOT in compendium]")
        self.add(title)

        statement = section_block([
            "Proposition 1.23 (G&W).",
            "If A and B are independent, then:",
            "  A and B^c are independent,",
            "  A^c and B are independent,",
            "  A^c and B^c are independent.",
            "",
            "Proof for A and B^c: [NOT in compendium — memorise]",
        ], font_size=25)
        statement.next_to(title, DOWN, buff=0.45)
        self.show(statement, wait_time=5.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"P(A \cap B^c) = P(A) - P(A \cap B)",
            "since A = (A intersect B) union (A intersect B^c), disjoint",
            RV_COLOR, wait=4.0)
        solver.add_step(2,
            r"= P(A) - P(A)\,P(B)",
            "use A,B independent: P(A intersect B) = P(A)P(B)",
            RV_COLOR, wait=3.0)
        solver.add_step(3,
            r"= P(A)\bigl(1 - P(B)\bigr) = P(A)\,P(B^c)",
            "factor and use complement rule P(B^c) = 1 - P(B)",
            GOLD, wait=3.0)
        solver.finalize(wait=2.0)

        mem = memorise_label()
        mem.next_to(title, DOWN, buff=5.5)
        self.show_last(mem)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W1b_p3(ParagraphScene):
    """Exam question: if A subset B, can they be independent?"""
    MP3_PATH = "narration/audio/paragraphs/W1b_p3.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 1b",
                                "Exam Question — Subset and Independence",
                                "Week 1b exam question")
        self.add(title)

        q = section_block([
            "Question: If A subset B, can A and B be independent?",
            "0 < P(A) < 1, 0 < P(B) < 1.",
        ], font_size=26)
        q.next_to(title, DOWN, buff=0.45)
        self.show(q, wait_time=3.0)

        reasoning = section_block([
            "If A subset B, then A intersect B = A.",
            "Independence requires P(A intersect B) = P(A)P(B).",
            "So we need: P(A) = P(A)*P(B) => P(B) = 1.",
            "But P(B) < 1 by assumption. Contradiction.",
            "",
            "Therefore: if A subset B with 0<P(B)<1, they CANNOT be independent.",
        ], font_size=24)
        reasoning.next_to(title, DOWN, buff=0.45)
        self.show_last(reasoning)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W1b_p4(ParagraphScene):
    """Combinatorics: multiplication principle, permutations — G&W §1.6"""
    MP3_PATH = "narration/audio/paragraphs/W1b_p4.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 1b", "Counting — Permutations",
                                "G&W §1.6 [compendium — binomial implicit]")
        self.add(title)

        mult = section_block([
            "Multiplication principle:",
            "If task 1 has m ways and task 2 has n ways,",
            "then together there are m*n ways.",
        ], font_size=26)
        mult.next_to(title, DOWN, buff=0.45)
        self.show(mult, wait_time=3.0)

        perm = label_block(
            r"P(n,k) = \frac{n!}{(n-k)!} = n(n-1)\cdots(n-k+1)",
            "Permutations: ordered selections of k from n without replacement",
            COMMENT_COLOR, eq_fs=30)
        perm.next_to(title, DOWN, buff=0.45)
        self.show(perm, wait_time=4.0)

        comb = label_block(
            r"\binom{n}{k} = \frac{n!}{k!\,(n-k)!}",
            "Combinations: unordered selections of k from n  [compendium, implicit]",
            COMPENDIUM_COLOR, eq_fs=36)
        comb.next_to(title, DOWN, buff=0.45)
        self.show(comb, wait_time=4.0)

        binom_thm = label_block(
            r"(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}",
            "Binomial theorem — essential identity used throughout the course",
            COMMENT_COLOR, eq_fs=32)
        binom_thm.next_to(title, DOWN, buff=0.45)
        self.show_last(binom_thm)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W1b_p5(ParagraphScene):
    """Combinatorics worked example: full house on five dice"""
    MP3_PATH = "narration/audio/paragraphs/W1b_p5.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 1b", "Worked Example — Full House",
                                "Week 1b exercise 1; G&W §1.6")
        self.add(title)

        setup = section_block([
            "Five fair dice are rolled.",
            "Full house: three dice show value a, two dice show value b (a≠b).",
            "Find P(full house).",
        ], font_size=26)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=4.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"\text{Total equally likely outcomes: } 6^5 = 7776",
            "sample space size; each outcome is a 5-tuple of die values",
            PROB_COLOR, wait=3.0)
        solver.add_step(2,
            r"\text{Choose value for triple: } 6 \text{ ways}",
            "6 choices for which number appears three times",
            RV_COLOR, wait=3.0)
        solver.add_step(3,
            r"\text{Choose value for pair: } 5 \text{ ways (a ≠ b)}",
            "5 remaining choices for the pair value",
            RV_COLOR, wait=3.0)
        solver.add_step(4,
            r"\text{Arrange 3 triples among 5 dice: } \binom{5}{3} = 10",
            "choose which 3 of the 5 dice show the triple value",
            RV_COLOR, wait=3.0)
        solver.add_step(5,
            r"P(\text{full house}) = \frac{6 \times 5 \times 10}{6^5} = \frac{300}{7776} = \frac{25}{648}",
            "favourable outcomes / total outcomes ≈ 3.86%",
            GOLD, wait=4.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W1b_p6(ParagraphScene):
    """Birthday problem — G&W §1.6, Week 1b extra exercise"""
    MP3_PATH = "narration/audio/paragraphs/W1b_p6.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 1b", "Worked Example — Birthday Problem",
                                "Week 1b extra exercise; G&W §1.6")
        self.add(title)

        setup = section_block([
            "n students in a room, birthdays independent, uniform on 365 days.",
            "(a) P(at least one student shares Gene's birthday)?",
            "(b) Minimum n so this probability >= 0.5?",
            "(c) P(at least one pair shares a birthday)?",
        ], font_size=25)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=5.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"P(\text{none share Gene's birthday}) = \left(\frac{364}{365}\right)^{n-1}",
            "each of the other n-1 students independently avoids Gene's birthday",
            PROB_COLOR, wait=4.0)
        solver.add_step(2,
            r"P(\text{at least one shares}) = 1 - \left(\frac{364}{365}\right)^{n-1}",
            "complement rule — this is (a)",
            PROB_COLOR, wait=3.0)
        solver.add_step(3,
            r"1-\left(\tfrac{364}{365}\right)^{n-1} \geq 0.5 \implies n \geq 1 + \frac{\log 0.5}{\log(364/365)} \approx 254",
            "solve for n — minimum is n=254 for part (b)",
            GOLD, wait=5.0)
        solver.finalize(wait=2.0)

        pair_note = section_block([
            "For (c): P(at least one pair) = 1 - P(all distinct).",
            "P(all n distinct) = 365*364*...*(365-n+1) / 365^n.",
            "This exceeds 0.5 when n >= 23 — the famous answer!",
        ], font_size=24)
        pair_note.next_to(title, DOWN, buff=5.5)
        self.show_last(pair_note)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W1b_p7(ParagraphScene):
    """Football problem — conditional probability on paths"""
    MP3_PATH = "narration/audio/paragraphs/W1b_p7.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 1b", "Worked Example — Football Scores",
                                "Week 1a extra exercise; G&W Problems 1.11 no.14a")
        self.add(title)

        setup = section_block([
            "Final score: 5-3 (Team A scored 5, Team B scored 3).",
            "Goals arrive one at a time, total 8 goals.",
            "Find P(B was ahead 2-1 at some point during the game).",
        ], font_size=25)
        setup.next_to(title, DOWN, buff=0.45)
        self.show(setup, wait_time=5.0)

        approach = section_block([
            "Assume all orderings of goals (5 A's and 3 B's) are equally likely.",
            "Total sequences = C(8,3) = 56  (choose which 3 of 8 goals are B's).",
            "",
            "For B to be ahead 2-1: at some point the sequence has seen",
            "exactly 1 A goal and 2 B goals.",
            "Count paths through state (1,2) [A score = 1, B score = 2].",
        ], font_size=23)
        approach.next_to(title, DOWN, buff=0.45)
        self.show(approach, wait_time=6.0)

        solver = StepSolver(self, title, start_buff=0.45)
        solver.add_step(1,
            r"\text{Paths to (1,2): } \binom{3}{2} = 3 \text{ ways (choose when B's occur)}",
            "choose 2 of first 3 goals to be B-goals, with 1 A-goal first or between",
            PROB_COLOR, wait=4.0)
        solver.add_step(2,
            r"\text{Paths from (1,2) to (5,3): } \binom{5}{1} = 5 \text{ ways}",
            "4 more A-goals and 1 more B-goal to reach 5-3; choose position of last B",
            PROB_COLOR, wait=4.0)
        solver.add_step(3,
            r"P = \frac{3 \times 5}{56} = \frac{15}{56} \approx 0.268",
            "favourable paths / total paths",
            GOLD, wait=4.0)
        solver.finalize(wait=2.0)
        self.wait(get_mp3_duration(self.MP3_PATH))


class W1b_p8(ParagraphScene):
    """Common mistakes in probability — exam strategy"""
    MP3_PATH = "narration/audio/paragraphs/W1b_p8.mp3"

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(self.MP3_PATH, time_offset=0)
        title = make_title_card("Week 1b", "Common Mistakes & Exam Strategy",
                                "Week 1 summary")
        self.add(title)

        mistakes = section_block([
            "COMMON MISTAKES:",
            "  x  Confusing P(A|B) with P(B|A) — always check direction",
            "  x  Assuming pairwise independence => mutual independence",
            "  x  Forgetting to verify P(B) > 0 before conditioning",
            "  x  Overcounting in combinatorics (divide by symmetry!)",
        ], font_size=24)
        mistakes.next_to(title, DOWN, buff=0.45)
        self.show(mistakes, wait_time=6.0)

        strategy = section_block([
            "EXAM STRATEGY for conditional probability questions:",
            "  1. Define events with notation: let A = '...', B = '...'",
            "  2. Write down which rule applies (Bayes / total prob)",
            "  3. State the partition explicitly",
            "  4. Compute denominator first (total probability)",
            "  5. State the theorem number used (e.g. Theorem 1.17)",
        ], font_size=24)
        strategy.next_to(title, DOWN, buff=0.45)
        self.show_last(strategy)
        self.wait(get_mp3_duration(self.MP3_PATH))

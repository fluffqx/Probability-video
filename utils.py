"""
utils.py — Shared layout helpers, colours, and base classes for 2MBS10.
Architecture: one Scene per narration paragraph.
Every Scene:
  1. self.add_sound(mp3_path, time_offset=0)  ← first line in construct()
  2. self.add(title)                          ← NOT self.play(Write(...))
  3. show content blocks with FadeIn(mob, run_time=0.1) → wait → FadeOut
  4. self.wait(MP3_DURATION)                  ← measured with mutagen
  5. do NOT FadeOut last content              ← tpad handles freeze
"""

from manim import *

# ---------------------------------------------------------------------------
# COLOUR PALETTE
# ---------------------------------------------------------------------------
BG_COLOR        = "#0f0f0f"   # dark background
SAMPLE_COLOR    = "#58C4DD"   # sample spaces, sets, events
PROB_COLOR      = "#FF9F40"   # probability values, measures
RV_COLOR        = "#83C167"   # random variables, functions
DIST_COLOR      = "#9B59B6"   # distributions, parameters
EX_COLOR        = "#FFFF00"   # expectations, moments, integrals
GOLD            = "#FFD700"   # final answers, key results, boxes
COMMENT_COLOR   = "#AAAAAA"   # annotations, grey labels
MEMORISE_COLOR  = "#FF4444"   # NOT in compendium — must memorise
COMPENDIUM_COLOR= "#55AA55"   # IN compendium — can look up
MISTAKE_COLOR   = "#FF6600"   # common mistakes
CORRECT_COLOR   = "#00DD88"   # correct approach

# ---------------------------------------------------------------------------
# LAYOUT CONSTANTS
# ---------------------------------------------------------------------------
SW       = 14.2   # scene width
SH       = 8.0    # scene height
TITLE_H  = 3.4    # y-position of title
BODY_TOP = 2.7    # y where body content starts
BODY_BOT = -3.5   # y where body content must end
SAFE_H   = 6.2    # safe vertical space

# ---------------------------------------------------------------------------
# AUDIO HELPERS
# ---------------------------------------------------------------------------
def get_mp3_duration(path: str) -> float:
    """Return duration of an MP3 file in seconds using mutagen."""
    try:
        from mutagen.mp3 import MP3
        return MP3(path).info.length
    except Exception:
        return 4.0  # fallback


# ---------------------------------------------------------------------------
# LAYOUT HELPERS
# ---------------------------------------------------------------------------
def safe_scale(mob, max_width: float = 13.0, max_height: float = 4.0):
    """Scale a mobject down if it exceeds safe screen dimensions."""
    w = mob.get_width()
    h = mob.get_height()
    if w > max_width:
        mob.scale(max_width / w)
    if mob.get_height() > max_height:
        mob.scale(max_height / mob.get_height())
    return mob


def make_title_card(week_str: str, topic_str: str, ref_str: str) -> VGroup:
    """Creates a 3-line permanent title: week | topic | source reference."""
    week  = Text(week_str,  font_size=22, color=COMMENT_COLOR)
    topic = Text(topic_str, font_size=30, color=GOLD)
    ref   = Text(ref_str,   font_size=20, color=COMMENT_COLOR)
    grp   = VGroup(week, topic, ref).arrange(DOWN, buff=0.15)
    grp.to_edge(UP, buff=0.2)
    return grp


def section_block(lines: list, font_size: int = 26) -> VGroup:
    """
    Create a block of text lines arranged vertically.
    Empty strings become spacers. Max 4 lines recommended.
    Always call safe_scale() after.
    """
    mobs = []
    for line in lines:
        if line == "":
            mobs.append(Text(" ", font_size=font_size // 2))
        else:
            mobs.append(Text(line, font_size=font_size))
    grp = VGroup(*mobs).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
    return safe_scale(grp)


def eq_block(latex: str, font_size: int = 36) -> MathTex:
    """Single equation block, scaled to fit."""
    mob = MathTex(latex, font_size=font_size)
    return safe_scale(mob)


def label_block(latex: str, label: str, label_color=COMMENT_COLOR,
                eq_fs: int = 34, lbl_fs: int = 20) -> VGroup:
    """Equation + small label below it."""
    eq  = MathTex(latex, font_size=eq_fs)
    lbl = Text(label, font_size=lbl_fs, color=label_color)
    grp = VGroup(eq, lbl).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
    return safe_scale(grp)


def memorise_label() -> Text:
    """Red [NOT IN COMPENDIUM — memorise] label."""
    return Text("[NOT IN COMPENDIUM — memorise]", font_size=18, color=MEMORISE_COLOR)


def compendium_label() -> Text:
    """Green [compendium] label."""
    return Text("[compendium]", font_size=18, color=COMPENDIUM_COLOR)


def gold_box(mob) -> SurroundingRectangle:
    """Gold box around a mobject."""
    return SurroundingRectangle(mob, color=GOLD, buff=0.12)


def step_label(n: int) -> Text:
    return Text(f"Step {n}:", font_size=26, color=GOLD)


# ---------------------------------------------------------------------------
# PARAGRAPH SCENE BASE CLASS
# ---------------------------------------------------------------------------
class ParagraphScene(Scene):
    """
    Base class for every paragraph scene.

    Subclasses must implement:
        MP3_PATH  = "narration/audio/paragraphs/SceneName_pN.mp3"
        TITLE     = make_title_card(...)

    All subclasses call:
        self.add_sound(self.MP3_PATH, time_offset=0)   ← first
        self.add(self.TITLE)                            ← second
        ... content blocks with show() helper ...
        self.wait(get_mp3_duration(self.MP3_PATH))      ← last
    """
    MP3_PATH = ""
    TITLE    = None

    def show(self, mob, wait_time: float = None):
        """
        FadeIn → hold → FadeOut pattern for a content block.
        mob must be positioned relative to self.TITLE (permanent reference).
        If wait_time is None, use MP3 duration minus a small offset.
        """
        self.play(FadeIn(mob, run_time=0.1))
        if wait_time is not None:
            self.wait(wait_time)
        self.play(FadeOut(mob, run_time=0.1))

    def show_last(self, mob):
        """
        FadeIn without FadeOut — for the LAST content block in a scene.
        tpad will freeze on this frame until audio ends.
        """
        self.play(FadeIn(mob, run_time=0.1))

    def body_pos(self, mob, ref=None, buff: float = 0.45):
        """Position mob below ref (default: self.TITLE) with buff."""
        anchor = ref if ref is not None else self.TITLE
        mob.next_to(anchor, DOWN, buff=buff)
        return mob


# ---------------------------------------------------------------------------
# STEP SOLVER (for proofs and calculations with pagination)
# ---------------------------------------------------------------------------
class StepSolver:
    """
    Manages step-by-step proofs on screen.
    Auto-pages when content overflows BODY_BOT.
    Each step: step label + equation + optional annotation.
    """

    def __init__(self, scene: Scene, title_mob, start_buff: float = 0.45):
        self.scene      = scene
        self.title      = title_mob
        self.start_buff = start_buff
        self.steps      = []   # list of VGroup currently on screen
        self._last_mob  = None

    def _page_if_needed(self, new_mob):
        """If adding new_mob would overflow, clear screen and reset."""
        if self._last_mob is None:
            return
        bottom = self._last_mob.get_bottom()[1] - new_mob.get_height() - 0.3
        if bottom < BODY_BOT:
            # Fade all current steps, start fresh
            self.scene.play(FadeOut(VGroup(*self.steps), run_time=0.2))
            self.steps = []
            self._last_mob = None

    def add_step(self, n: int, latex: str, annotation: str = "",
                 color=WHITE, fs: int = 32, wait: float = 3.0):
        """Add one proof step to the screen."""
        lbl = step_label(n)
        eq  = MathTex(latex, font_size=fs, color=color)
        safe_scale(eq, max_width=12.5, max_height=1.8)

        row = VGroup(lbl, eq).arrange(RIGHT, buff=0.3)

        if annotation:
            ann = Text(annotation, font_size=18, color=COMMENT_COLOR)
            safe_scale(ann, max_width=12.5, max_height=0.5)
            grp = VGroup(row, ann).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        else:
            grp = row

        safe_scale(grp, max_width=13.0, max_height=2.0)

        self._page_if_needed(grp)

        if self._last_mob is None:
            grp.next_to(self.title, DOWN, buff=self.start_buff)
        else:
            grp.next_to(self._last_mob, DOWN, buff=0.28)

        self.scene.play(FadeIn(grp, run_time=0.1))
        self.scene.wait(wait)
        self.steps.append(grp)
        self._last_mob = grp

    def finalize(self, wait: float = 2.0):
        """Draw a gold box around the last step."""
        if self._last_mob is None:
            return
        box = gold_box(self._last_mob)
        self.scene.play(Create(box, run_time=0.3))
        self.scene.wait(wait)
        self.steps.append(box)

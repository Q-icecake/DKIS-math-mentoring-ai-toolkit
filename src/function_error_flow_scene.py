from manim import *


class FunctionErrorFlowScene(Scene):
    """Manim scene for the math mentoring project.

    Theme:
    - Show how a student gets stuck in a function problem.
    - Connect error types to a visual explanation of y = 2x + 1.
    - End with a recommended learning path.

    Render example:
        manim -qm function_error_flow_scene.py FunctionErrorFlowScene
    """

    def construct(self):
        self.camera.background_color = WHITE

        # ---------- Colors ----------
        main_blue = BLUE_D
        soft_red = RED_D
        soft_green = GREEN_D
        soft_orange = ORANGE
        dark = BLACK
        gray = GREY_B

        # ---------- Title ----------
        title = Text(
            "함수 문제에서 학생이 막히는 과정",
            font="NanumGothic",
            font_size=34,
            color=dark,
        )
        title.to_edge(UP)

        subtitle = Text(
            "설문 + 오류 유형 분석 + LSTM 파일럿 결과를 바탕으로 한 시각화 예시",
            font="NanumGothic",
            font_size=19,
            color=gray,
        )
        subtitle.next_to(title, DOWN, buff=0.18)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)

        # ---------- Problem Card ----------
        problem_box = RoundedRectangle(
            corner_radius=0.18,
            width=12.5,
            height=1.05,
            stroke_color=main_blue,
            stroke_width=2,
            fill_color=BLUE_E,
            fill_opacity=0.08,
        )
        problem_box.move_to([0, 2.45, 0])

        problem_text = Text(
            "문제 예시: 일차함수 y = 2x + 1 에서 그래프의 기울기와 y절편을 설명하시오.",
            font="NanumGothic",
            font_size=23,
            color=dark,
        )
        problem_text.move_to(problem_box.get_center())

        self.play(Create(problem_box), Write(problem_text))
        self.wait(1)

        # ---------- Left Side: Error Flow ----------
        flow_title = Text(
            "학생 오류 흐름",
            font="NanumGothic",
            font_size=25,
            color=dark,
        )
        flow_title.move_to([-4.25, 1.4, 0])
        self.play(Write(flow_title))

        def make_card(title_text, desc_text, color):
            box = RoundedRectangle(
                corner_radius=0.15,
                width=3.6,
                height=0.92,
                stroke_color=color,
                stroke_width=2,
                fill_color=color,
                fill_opacity=0.08,
            )
            title_obj = Text(
                title_text,
                font="NanumGothic",
                font_size=19,
                color=color,
            )
            desc_obj = Text(
                desc_text,
                font="NanumGothic",
                font_size=15,
                color=dark,
            )
            title_obj.move_to(box.get_center() + UP * 0.18)
            desc_obj.move_to(box.get_center() + DOWN * 0.18)
            return VGroup(box, title_obj, desc_obj)

        card1 = make_card("1. 문제 접근 오류", "무엇부터 볼지 모름", soft_orange)
        card2 = make_card("2. 전략 선택 오류", "기울기와 절편 판단이 어려움", soft_red)
        card3 = make_card("3. 개념 이해 오류", "기울기의 의미가 불명확함", main_blue)

        card1.move_to([-4.25, 0.65, 0])
        card2.move_to([-4.25, -0.45, 0])
        card3.move_to([-4.25, -1.55, 0])

        arrow1 = Arrow(card1.get_bottom(), card2.get_top(), buff=0.08, color=gray)
        arrow2 = Arrow(card2.get_bottom(), card3.get_top(), buff=0.08, color=gray)

        self.play(FadeIn(card1))
        self.play(Create(arrow1), FadeIn(card2))
        self.play(Create(arrow2), FadeIn(card3))
        self.wait(1)

        # ---------- Right Side: Function Graph ----------
        graph_title = Text(
            "Manim 함수 그래프 시각화",
            font="NanumGothic",
            font_size=25,
            color=dark,
        )
        graph_title.move_to([2.4, 1.4, 0])
        self.play(Write(graph_title))

        axes = Axes(
            x_range=[-2, 4, 1],
            y_range=[-2, 8, 2],
            x_length=5.2,
            y_length=3.7,
            axis_config={"color": gray, "stroke_width": 2},
            tips=False,
        )
        axes.move_to([2.4, -0.3, 0])

        labels = axes.get_axis_labels(x_label=MathTex("x"), y_label=MathTex("y"))
        labels.set_color(dark)

        graph = axes.plot(lambda x: 2 * x + 1, x_range=[-1.2, 3.0], color=main_blue)

        equation = MathTex("y = 2x + 1", color=main_blue)
        equation.scale(0.9)
        equation.move_to([4.2, 1.15, 0])

        self.play(Create(axes), FadeIn(labels))
        self.play(Create(graph), Write(equation))
        self.wait(0.8)

        # ---------- y-intercept ----------
        y_intercept_dot = Dot(axes.c2p(0, 1), color=soft_red)
        y_intercept_label = Text(
            "y절편 = 1",
            font="NanumGothic",
            font_size=18,
            color=soft_red,
        )
        y_intercept_label.next_to(y_intercept_dot, LEFT, buff=0.18)

        self.play(FadeIn(y_intercept_dot), Write(y_intercept_label))
        self.wait(0.8)

        # ---------- Slope: run 1, rise 2 ----------
        p1 = axes.c2p(1, 3)
        p2 = axes.c2p(2, 3)
        p3 = axes.c2p(2, 5)

        run_line = Line(p1, p2, color=soft_green, stroke_width=5)
        rise_line = Line(p2, p3, color=soft_green, stroke_width=5)

        run_label = Text(
            "1만큼 이동",
            font="NanumGothic",
            font_size=16,
            color=soft_green,
        )
        run_label.next_to(run_line, DOWN, buff=0.1)

        rise_label = Text(
            "2만큼 증가",
            font="NanumGothic",
            font_size=16,
            color=soft_green,
        )
        rise_label.next_to(rise_line, RIGHT, buff=0.1)

        slope_text = Text(
            "기울기 = y의 증가량 / x의 증가량 = 2 / 1",
            font="NanumGothic",
            font_size=20,
            color=soft_green,
        )
        slope_text.move_to([2.4, -2.55, 0])

        self.play(Create(run_line), Write(run_label))
        self.play(Create(rise_line), Write(rise_label))
        self.play(Write(slope_text))
        self.wait(1.5)

        # ---------- Recommendation Path ----------
        self.play(FadeOut(slope_text), FadeOut(run_label), FadeOut(rise_label))

        recommend_box = RoundedRectangle(
            corner_radius=0.18,
            width=12.4,
            height=1.0,
            stroke_color=soft_green,
            stroke_width=2,
            fill_color=GREEN_E,
            fill_opacity=0.08,
        )
        recommend_box.to_edge(DOWN, buff=0.35)

        recommend_text = Text(
            "추천 학습 경로: 문제 접근 순서 카드 → 함수 그래프 시각화 → 예제 중심 복습",
            font="NanumGothic",
            font_size=22,
            color=dark,
        )
        recommend_text.move_to(recommend_box.get_center())

        self.play(Create(recommend_box), Write(recommend_text))
        self.wait(2)

        final_text = Text(
            "모델은 학생을 대신 판단하는 것이 아니라, 멘토링을 더 정확하게 돕는 보조 도구이다.",
            font="NanumGothic",
            font_size=21,
            color=gray,
        )
        final_text.next_to(recommend_box, UP, buff=0.25)

        self.play(Write(final_text))
        self.wait(2)

from manim import *
import os
from PIL import Image  # Add import for PIL

# Vision Transformer
# By WAT.ai
# zoom into the name


class MovingNetworkBackground(Scene):
    def construct(self):
        # Number of nodes and connections
        num_nodes = 15
        node_positions = [
            np.random.uniform(-6, 6, size=(2,)) for _ in range(num_nodes)
        ]

        # Create dots (nodes)
        dots = VGroup(*[Dot(point=np.append(pos, 0), radius=0.05, color=GRAY_A) for pos in node_positions])
        self.add(dots)

        # Create connections (edges) with darker color
        lines = VGroup()
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                line = Line(
                    np.append(node_positions[i], 0),
                    np.append(node_positions[j], 0),
                    stroke_color=GREY_BROWN,
                    stroke_opacity=0.3,
                    stroke_width=1,
                )
                lines.add(line)
        self.add(lines)

        # Animate nodes and edges moving smoothly
        for _ in range(100):
            new_positions = [
                pos + np.random.uniform(-0.05, 0.05, size=(2,))
                for pos in node_positions
            ]
            node_positions = new_positions

            animations = []
            for dot, new_pos in zip(dots, node_positions):
                animations.append(dot.animate.move_to(np.append(new_pos, 0)))

            for line, (i, j) in zip(lines, [(i, j) for i in range(num_nodes) for j in range(i + 1, num_nodes)]):
                line.put_start_and_end_on(
                    np.append(node_positions[i], 0),
                    np.append(node_positions[j], 0),
                )

            self.play(*animations, run_time=0.5, rate_func=smooth)

        self.wait(1)

class WriteTitleAndLogo(Scene):
    def construct(self):
        # Create the title text
        title = Text("Vision Transformers", font="Lato, sans-serif", font_size=144).set_color("#f0bc0c")
        title.scale(0.7)  # Adjust scaling
        title.move_to(ORIGIN)  # Center the title

        # Load the logo SVG file
        logo = SVGMobject("/Users/yanajakhwal/Desktop/Projects/manim/ViT/assets/images/watai_logo.svg")
        logo.scale(0.5)  # Scale the logo
        
        # Position the logo just below the title
        logo.next_to(title, DOWN, buff=0.05)  # Adjust the buffer for a snug fit

        # Animate the writing of the title
        self.play(Write(title, run_time=3))
        self.wait(1)

        # Slightly shift the title upwards
        self.play(title.animate.shift(UP * (logo.height + 0.05)), run_time=1)

        # Animate drawing the logo below the title
        self.play(Create(logo, run_time=3))
        self.wait()

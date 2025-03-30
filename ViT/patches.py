from manim import *
import os
from PIL import Image  # Add import for PIL

class PicToPatches(MovingCameraScene):
    def construct(self):
        # Parameters
        self.camera.frame.save_state()

        patch_folder = "assets/images/image_patches_3x3"  # Path to your image
        grid_size = 3  # Number of rows and columns
        patch_scale = 0.3 # Scale factor for patches

        total_patches = grid_size * grid_size

        patches = []
        for row in range(grid_size):
            for col in range(grid_size):
                patch_filename = f"patch_{row}_{col}.png"
                patch_path = os.path.join(patch_folder, patch_filename)
                if not os.path.isfile(patch_path):
                    raise FileNotFoundError(f"Patch image not found: {patch_path}")
                patch = ImageMobject(patch_path)
                patch.scale(patch_scale)
                patches.append(patch)

        # Assemble patches into a grid
        patches_group = Group(*patches)
        patches_group.arrange_in_grid(rows=grid_size, buff=0)  # No spacing between patches

        # Display the assembled image
        self.play(FadeIn(patches_group))
        self.wait(1)

        # Animate the patches so that they separate from each other
        self.play(patches_group.animate.arrange_in_grid(rows=grid_size, buff=0.5))
        self.wait(1)

        # Scale down the patches to fit the screen when flattened
        self.play(patches_group.animate.scale(0.5))

        self.play(patches_group.animate.arrange_in_grid(rows=1, cols=grid_size*grid_size, buff=0.5))
        self.wait(1)
        metric_initial = Tex(r"""
            Image Size: 15 $\times$ 15 \\
            Patch Size: 5 $\times$ 5 \\
            Number of Patches: 9 \\
            Transformer sequence length: 9
        """).to_edge(UP)
        

        self.play(Write(metric_initial))
        self.wait(1)
        self.wait(1)
        self.play(FadeOut(metric_initial))
        # Go back to the original arrangement

        self.play(patches_group.animate.arrange_in_grid(rows=grid_size, buff=0))
        self.play(patches_group.animate.scale(2))


        patch_folder = "assets/images/image_patches_5x5"  # Path to your image
        grid_size = 5  # Number of rows and columns
        patch_scale = 0.3

        total_patches = grid_size * grid_size

        patches_2 = []
        for row in range(grid_size):
            for col in range(grid_size):
                patch_filename = f"patch_{row}_{col}.png"
                patch_path = os.path.join(patch_folder, patch_filename)
                if not os.path.isfile(patch_path):
                    raise FileNotFoundError(f"Patch image not found: {patch_path}")
                patch = ImageMobject(patch_path)
                patch.scale(patch_scale)
                patches_2.append(patch)

        patches_group_2 = Group(*patches_2)
        patches_group_2.arrange_in_grid(rows=grid_size, buff=0)  # No spacing between patches

        # Display the assembled image
        self.play(FadeOut(patches_group))
        self.play(FadeIn(patches_group_2))

        self.play(patches_group_2.animate.arrange_in_grid(rows=grid_size, buff=0.5))
        self.wait(1)

        self.play(patches_group_2.animate.scale(0.5))

        self.play(patches_group_2.animate.arrange_in_grid(rows=1, cols=grid_size*grid_size, buff=0.1))
        self.wait(1)

        metric_initial = Tex(r"""
            Image Size: 15 $\times$ 15 \\
            Patch Size: 3 $\times$ 3 \\
            Number of Patches: 25 \\
            Transformer sequence length: 25
        """).to_edge(UP)

        self.play(Write(metric_initial))
        self.wait(1)
        self.play(FadeOut(metric_initial))

        self.play(FadeOut(patches_group_2))
        self.wait(1)

        self.play(FadeIn(patches_group))
        self.wait(1)
        self.play(patches_group.animate.scale(0.5))
        self.play(patches_group.animate.arrange_in_grid(rows=1, cols=grid_size*grid_size, buff=0.5).to_edge(UP))
        
        self.wait(1)

        self.play(self.camera.frame.animate.set(width=patches_group[0].width*2).move_to(patches_group[0]))
        self.wait(1)

        self.play(FadeOut(patches_group[0]))

        image_matrix = Matrix([
            [r"a_{11}", r"a_{12}", ".", ".", "."],
            [r"a_{21}", r"a_{22}", ".", ".", "."],
            [".", ".", "", "", ""],
            [".", ".", "", "", ""],
            [".", ".", "", "", r"a_{pp}"]
        ]).scale(0.1)
        
        image_matrix.move_to(patches_group[0].get_center())  # Move matrix to the first patch's position
        self.play(FadeIn(image_matrix))
        
        # Add axis labels around the matrix
        label_image = Tex(r'$\mathbb{R}^{p \times p \times c}$').scale(0.1).next_to(image_matrix, direction=UP, buff=0.05)
        self.play(FadeIn(label_image))
        note_image = Tex(r'Each value in the matrix has c channels. Usually 3 for RGB values').scale(0.1).next_to(image_matrix, direction=UP, buff=0.15)
        self.play(FadeIn(note_image))
        self.wait(1)
        self.play(FadeOut(note_image))
        self.play(FadeOut(label_image))
        self.wait(1)

        note_image = Tex(r'$i = p^{2}c$').scale(0.1).next_to(image_matrix, direction=UP, buff=0.15)
        self.play(FadeIn(note_image))
        self.wait(1)
        self.play(FadeOut(note_image))

        image_matrix_2 = Matrix([
            [r"a_{1}"], 
            [r"a_{2}"], 
            [r"a_{3}"], 
            [r"\cdot"], 
            [r"\cdot"], 
            [r"a_{i}"]
        ], h_buff=1.1).scale(0.1).move_to(patches_group[0].get_center())
        
        # Shift the centered dots up
        image_matrix_2.get_entries()[3].shift(UP * 0.013).shift(LEFT * 0.015)
        image_matrix_2.get_entries()[4].shift(UP * 0.013).shift(LEFT * 0.015)

        self.play(Transform(image_matrix, image_matrix_2))
        self.wait(1)
        self.play(image_matrix.animate.to_edge(LEFT, buff=1.75))

        # times = Tex(r'$\cdot$').scale(0.3)
        # times.move_to(patches_group[0].get_center())
        # times.shift(LEFT * 0.47)
        # self.play(FadeIn(times))    
        self.wait(1)
        embedding_matrix = Matrix([
            [r"b_{11}", r"b_{12}", ".", ".", "."],
            [r"b_{21}", r"b_{22}", ".", ".", "."],
            [".", ".", "", "", ""],
            [".", ".", "", "", ""],
            [".", ".", "", "", r"b_{Di}"]
        ]).scale(0.1)
        embedding_matrix.move_to(patches_group[0].get_center())
        embedding_matrix.to_edge(LEFT, buff=1)
        self.play(FadeIn(embedding_matrix))

        label_embedding = Tex(r'$\mathbb{R}^{D \times i}$').scale(0.1).next_to(embedding_matrix, direction=UP, buff=0.1)
        self.play(FadeIn(label_embedding))
        label_image = Tex(r'$\mathbb{R}^{i}$').scale(0.1).next_to(image_matrix, direction=UP, buff=0.1)
        self.play(FadeIn(label_image))
        self.wait(1)

        plus = Tex(r'$+$').scale(0.1)
        plus.move_to(patches_group[0].get_center())
        plus.shift(RIGHT * 0.30)
        self.play(FadeIn(plus))    
        self.wait(1)

        bias_matrix = Matrix([
            [r"c_{1}"], 
            [r"c_{2}"], 
            [r"c_{3}"], 
            [r"\cdot"], 
            [r"\cdot"], 
            [r"c_{D}"]
        ]).scale(0.1)
        bias_matrix.get_entries()[3].shift(UP * 0.013).shift(LEFT * 0.015)
        bias_matrix.get_entries()[4].shift(UP * 0.013).shift(LEFT * 0.015)

        bias_matrix.move_to(patches_group[0].get_center())
        bias_matrix.to_edge(LEFT, buff=2.2)
        self.play(FadeIn(bias_matrix))
        self.wait(1)

        label_bias = Tex(r'$\mathbb{R}^{D}$').scale(0.1).next_to(bias_matrix, direction=UP, buff=0.1)
        label_bias.shift(RIGHT * 0.01)
        self.play(FadeIn(label_bias))
        self.wait(1)

        embedded_matrix = Matrix([
            [r"e_{1}"], 
            [r"e_{2}"], 
            [r"e_{3}"], 
            [r"\cdot"], 
            [r"\cdot"], 
            [r"e_{D}"]
        ]).scale(0.1)
        embedded_matrix.get_entries()[3].shift(UP * 0.013).shift(LEFT * 0.015)
        embedded_matrix.get_entries()[4].shift(UP * 0.013).shift(LEFT * 0.015)
        embedded_matrix.move_to(patches_group[0].get_center())

        self.play(
            Transform(image_matrix, embedded_matrix),
            Transform(embedding_matrix, embedded_matrix),
            Transform(bias_matrix, embedded_matrix),
            FadeOut(label_bias),
            FadeOut(label_image),
            FadeOut(label_embedding),
            FadeOut(plus)
        )
        # self.play(FadeOut(image_matrix), FadeOut(embedding_matrix), FadeOut(bias_matrix), FadeOut(label_bias), FadeOut(label_image), FadeOut(label_embedding), FadeOut(plus), FadeOut(times))

        self.wait(1)

        # self.play(FadeIn(embedded_matrix))
        # self.wait(1)
        
        label_embedded = Tex(r'$\mathbb{R}^{D}$').scale(0.1).next_to(embedded_matrix, direction=UP, buff=0.1)
        label_embedded.shift(RIGHT * 0.01)
        self.play(FadeIn(label_embedded))
        self.wait(1)
        self.play(FadeOut(label_embedded))

        first_item = Tex(r"$X_{1}$").scale(0.1)
        first_item.move_to(embedded_matrix.get_center())

        self.play(
            Transform(embedded_matrix, first_item),
            Transform(image_matrix, first_item),
            Transform(embedding_matrix, first_item),
            Transform(bias_matrix, first_item),
            FadeOut(embedded_matrix),
            FadeOut(embedding_matrix),
            FadeOut(bias_matrix)
            )
        
        self.wait(1)

        self.play(
            Restore(self.camera.frame),
            first_item.animate.scale(10),
            FadeOut(image_matrix)
        )

        second_item = Tex(r"$X_{2}$")
        third_item = Tex(r"$X_{3}$")
        fourth_item = Tex(r"$X_{4}$")
        fifth_item = Tex(r"$X_{5}$")
        sixth_item = Tex(r"$X_{6}$")
        seventh_item = Tex(r"$X_{7}$")
        eighth_item = Tex(r"$X_{8}$")
        ninth_item = Tex(r"$X_{9}$")

        second_item.move_to(patches_group[1].get_center())
        third_item.move_to(patches_group[2].get_center())
        fourth_item.move_to(patches_group[3].get_center())
        fifth_item.move_to(patches_group[4].get_center())
        sixth_item.move_to(patches_group[5].get_center())
        seventh_item.move_to(patches_group[6].get_center())
        eighth_item.move_to(patches_group[7].get_center())
        ninth_item.move_to(patches_group[8].get_center())

        self.wait(1)

        self.play(
            FadeOut(patches_group[1]), 
            FadeIn(second_item),
            FadeOut(patches_group[2]),
            FadeIn(third_item),
            FadeOut(patches_group[3]),
            FadeIn(fourth_item),
            FadeOut(patches_group[4]),
            FadeIn(fifth_item),
            FadeOut(patches_group[5]),
            FadeIn(sixth_item),
            FadeOut(patches_group[6]),
            FadeIn(seventh_item),
            FadeOut(patches_group[7]),
            FadeIn(eighth_item),
            FadeOut(patches_group[8]),
            FadeIn(ninth_item)
            )
        
        self.wait(1)

        firstadd = Tex(r"$+$").next_to(first_item, direction=DOWN, buff=0.1)
        secondadd = Tex(r"$+$").next_to(second_item, direction=DOWN, buff=0.1)
        thirdadd = Tex(r"$+$").next_to(third_item, direction=DOWN, buff=0.1)
        fourthadd = Tex(r"$+$").next_to(fourth_item, direction=DOWN, buff=0.1)
        fifthadd = Tex(r"$+$").next_to(fifth_item, direction=DOWN, buff=0.1)
        sixthadd = Tex(r"$+$").next_to(sixth_item, direction=DOWN, buff=0.1)
        seventhadd = Tex(r"$+$").next_to(seventh_item, direction=DOWN, buff=0.1)
        eighthadd = Tex(r"$+$").next_to(eighth_item, direction=DOWN, buff=0.1)
        ninthadd = Tex(r"$+$").next_to(ninth_item, direction=DOWN, buff=0.1)

        self.play(
            FadeIn(firstadd),
            FadeIn(secondadd),
            FadeIn(thirdadd),
            FadeIn(fourthadd),
            FadeIn(fifthadd),
            FadeIn(sixthadd),
            FadeIn(seventhadd),
            FadeIn(eighthadd),
            FadeIn(ninthadd)
        )

        first_item_encoding = Tex(r"$P_{1}$")
        second_item_encoding = Tex(r"$P_{2}$")
        third_item_encoding = Tex(r"$P_{3}$")
        fourth_item_encoding = Tex(r"$P_{4}$")
        fifth_item_encoding = Tex(r"$P_{5}$")
        sixth_item_encoding = Tex(r"$P_{6}$")
        seventh_item_encoding = Tex(r"$P_{7}$")
        eighth_item_encoding = Tex(r"$P_{8}$")
        ninth_item_encoding = Tex(r"$P_{9}$")

        first_item_encoding.next_to(first_item, direction=DOWN, buff=0.6)
        second_item_encoding.next_to(second_item, direction=DOWN, buff=0.6)
        third_item_encoding.next_to(third_item, direction=DOWN, buff=0.6)
        fourth_item_encoding.next_to(fourth_item, direction=DOWN, buff=0.6)
        fifth_item_encoding.next_to(fifth_item, direction=DOWN, buff=0.6)
        sixth_item_encoding.next_to(sixth_item, direction=DOWN, buff=0.6)
        seventh_item_encoding.next_to(seventh_item, direction=DOWN, buff=0.6)
        eighth_item_encoding.next_to(eighth_item, direction=DOWN, buff=0.6)
        ninth_item_encoding.next_to(ninth_item, direction=DOWN, buff=0.6)

        self.play(
            FadeIn(first_item_encoding),
            FadeIn(second_item_encoding),
            FadeIn(third_item_encoding),
            FadeIn(fourth_item_encoding),
            FadeIn(fifth_item_encoding),
            FadeIn(sixth_item_encoding),
            FadeIn(seventh_item_encoding),
            FadeIn(eighth_item_encoding),
            FadeIn(ninth_item_encoding)
            )
        
        self.wait(1)

        encoding_explanation = Tex(r"Each patch has a learnable positional encoding vector in $\mathbb{R}^{D}$ added to it ").scale(0.7)

        self.play(Write(encoding_explanation))


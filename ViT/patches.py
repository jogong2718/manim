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
        self.play(FadeIn(patches_group_2))
        self.play(FadeOut(patches_group))


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

        m1 = Tex("(132, 223, 23)")
        m2 = Tex("(122, 253, 74)")
        m3 = Tex("(112, 195, 111)")
        m4 = Tex("(0, 253, 64)")

        # Scale down the RGB matrices
        m1.scale(0.1)
        m2.scale(0.1)
        m3.scale(0.1)
        m4.scale(0.1)

        image_matrix = Matrix([
            [r"a_{1,1}", r"a_{1,2}", ".", ".", "."],
            [r"a_{2,1}", r"a_{2,2}", ".", ".", "."],
            [".", ".", "", "", ""],
            [".", ".", "", "", ""],
            [".", ".", "", "", r"a_{m,n}"]
        ]).scale(0.1)
        
        image_matrix.move_to(patches_group[0].get_center())  # Move matrix to the first patch's position
        self.play(FadeIn(image_matrix))
        
        # Add axis labels around the matrix
        label_image = Tex(r'$\mathbb{R}^{m \times n}$').scale(0.1).next_to(image_matrix, direction=UP, buff=0.05)
        self.play(FadeIn(label_image))
        note_image = Tex(r'Each value in the matrix is an rgb value with 3 channels').scale(0.1).next_to(image_matrix, direction=UP, buff=0.15)
        self.play(FadeIn(note_image))
        self.wait(1)
        self.play(FadeOut(note_image))
        self.play(FadeOut(label_image))
        self.wait(1)

        image_matrix_2 = Matrix([
            [r"a_{1}", r"a_{2}", r"a_{3}", r"\cdot", r"\cdot", r"a_{m \times n}"]
        ], h_buff=1.1).scale(0.1).move_to(patches_group[0].get_center())
        
        # Shift the centered dots to the left
        image_matrix_2.get_entries()[3].shift(LEFT * 0.03).shift(UP * 0.013)
        image_matrix_2.get_entries()[4].shift(LEFT * 0.07).shift(UP * 0.013)

        self.play(Transform(image_matrix, image_matrix_2))
        self.wait(1)
        self.play(image_matrix.animate.to_edge(LEFT, buff=1))

        times = Tex(r'$\times$').scale(0.1)
        times.move_to(patches_group[0].get_center())
        self.play(FadeIn(times))    
        self.wait(1)
        embedding_matrix = Matrix([
            [r"b_{1,1}", r"b_{1,2}", ".", ".", "."],
            [r"b_{2,1}", r"b_{2,2}", ".", ".", "."],
            [".", ".", "", "", ""],
            [".", ".", "", "", ""],
            [".", ".", "", "", r"b_{D,n}"]
        ]).scale(0.1)
        embedding_matrix.move_to(patches_group[0].get_center())
        embedding_matrix.to_edge(LEFT, buff=1.8)
        self.play(FadeIn(embedding_matrix))

        label_embedding = Tex(r'$\mathbb{R}^{D \times n}$').scale(0.1).next_to(embedding_matrix, direction=UP, buff=0.1)
        self.play(FadeIn(label_embedding))
        label_image = Tex(r'$\mathbb{R}^{m \times n}$').scale(0.1).next_to(image_matrix, direction=UP, buff=0.1)
        self.play(FadeIn(label_image))
        self.wait(1)
        self.play(Restore(self.camera.frame))
        self.wait(1)


from manim import *
import os
from PIL import Image  # Add import for PIL

class PicToPatches(MovingCameraScene):
    def construct(self):
        # Parameters
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

        self.play(MovingCamera.auto_zoom(mobjects=patches_group[0], margin= 0,
        only_mobjects_in_frame = False,
        animate= True,))

        # Prepare for splitting: move patches slightly outwards
        # center = patches_group.get_center()
        # for patch in patches:
        #     direction = patch.get_center() - center
        #     if direction.get_length() == 0:  # handle a patch at the center
        #         direction = UP * 0.2
        #     else:
        #         direction = direction / direction.get_length() * 0.2
        #     patch.shift(direction)

        # self.play(patches_group.animate.arrange_in_grid(rows=grid_size, buff=0))

        # self.wait(1)

        # Animate patches moving outward from the center
        # animations = []
        # for patch in patches:
        #     direction = patch.get_center() - ORIGIN
        #     # Normalize direction to avoid zero vector
        #     if direction == ORIGIN:
        #         direction = UP
        #     else:
        #         direction = direction / np.linalg.norm(direction)
        #     # Shift patches outward
        #     animations.append(patch.animate.shift(direction * 3))
        # self.play(*animations, run_time=2)
        # self.wait(1)

        # # Optionally, fade out the patches
        # self.play(*[FadeOut(patch) for patch in patches])
        # self.wait(1)

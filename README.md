## Manim Projects

## About

This repository contains various Manim projects demonstrating AI technologies and concepts.

## Generating MP4 Videos

1. Install Manim and any dependencies listed in the requirements.
2. Navigate to the directory containing your desired scene file.
3. Use the following command to generate an MP4 video (here using patches.py as an example):

   ```bash
   manim -pqh patches.py PicToPatches
   ```

   - -p: Preview the output video after rendering.
   - -q: Specify quality (options include l, m, h, p).
   - -h: High quality or -qk for 4K. Use l for testing purposes as it takes much less time to render.
   - PicToPatches is the scene class name in the file.

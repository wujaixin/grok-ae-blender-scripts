#!/usr/bin/env python3
"""Blender Batch Render Script - Grok Recommended
Usage: Paste in Blender Scripting tab and run.
Renders all scenes to PNG."""
import bpy
import os

def batch_render(output_dir="/tmp/blender_renders"):
    os.makedirs(output_dir, exist_ok=True)
    for scene in bpy.data.scenes:
        bpy.context.window.scene = scene
        scene.render.filepath = os.path.join(output_dir, scene.name + ".png")
        scene.render.image_settings.file_format = 'PNG'
        print(f"Rendering {scene.name}...")
        bpy.ops.render.render(write_still=True)
    print("Batch render done!")

if __name__ == "__main__":
    batch_render()
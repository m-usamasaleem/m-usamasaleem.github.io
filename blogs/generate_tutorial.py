#!/usr/bin/env python3
"""
Tutorial Generator Script
Generate new tutorial pages from the template by replacing placeholder values.
"""

import os
import re
from datetime import datetime

def generate_tutorial(tutorial_data):
    """
    Generate a tutorial page from template using provided data.
    
    Args:
        tutorial_data (dict): Dictionary containing tutorial information
    """
    
    # Read the template
    template_path = "template.html"
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # Replace all placeholders with actual content
    for placeholder, value in tutorial_data.items():
        template_content = template_content.replace(placeholder, str(value))
    
    # Create output filename
    output_filename = f"tutorials/{tutorial_data['TUTORIAL_SLUG']}.html"
    
    # Write the generated tutorial
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(template_content)
    
    print(f"✅ Tutorial generated: {output_filename}")
    return output_filename

def create_sample_tutorial():
    """Create a sample tutorial to demonstrate the template usage."""
    
    sample_data = {
        'TUTORIAL_TITLE': 'Introduction to 3D Human Pose Estimation',
        'TUTORIAL_DESCRIPTION': 'A comprehensive tutorial on 3D human pose estimation using deep learning',
        'TUTORIAL_SLUG': '3d-pose-estimation-intro',
        'TUTORIAL_CATEGORY': 'Computer Vision',
        'TUTORIAL_DIFFICULTY': 'Intermediate',
        'TUTORIAL_READING_TIME': '15 min read',
        'TUTORIAL_INTRO_TEXT': 'Learn the fundamentals of 3D human pose estimation, from basic concepts to advanced deep learning implementations.',
        'TUTORIAL_INTRODUCTION_CONTENT': '3D human pose estimation is a fundamental computer vision task that involves predicting the 3D positions of human body joints from images or videos. This tutorial will guide you through the essential concepts and practical implementation.',
        'TUTORIAL_SPECIFIC_PREREQUISITES': 'Understanding of convolutional neural networks (CNNs) and PyTorch basics',
        'TUTORIAL_OVERVIEW_CONTENT': 'We will cover the complete pipeline from data preprocessing to model training and evaluation, including state-of-the-art architectures.',
        'TUTORIAL_KEY_CONCEPT_1': 'Camera calibration and projection matrices',
        'TUTORIAL_KEY_CONCEPT_2': '2D to 3D lifting techniques',
        'TUTORIAL_KEY_CONCEPT_3': 'Multi-view geometry principles',
        'TUTORIAL_IMPLEMENTATION_INTRO': 'Let\'s implement a basic 3D pose estimation pipeline step by step.',
        'TUTORIAL_CODE_SNIPPET_1': '''# Install required packages
pip install torch torchvision
pip install opencv-python
pip install numpy matplotlib

# Import libraries
import torch
import torch.nn as nn
import cv2
import numpy as np''',
        'TUTORIAL_CODE_SNIPPET_2': '''# Data preprocessing function
def preprocess_image(image_path):
    """Preprocess input image for pose estimation."""
    image = cv2.imread(image_path)
    image = cv2.resize(image, (256, 256))
    image = image / 255.0
    image = np.transpose(image, (2, 0, 1))
    return torch.FloatTensor(image).unsqueeze(0)''',
        'TUTORIAL_CODE_SNIPPET_3': '''# Simple 3D pose estimation model
class PoseEstimationModel(nn.Module):
    def __init__(self, num_joints=17):
        super(PoseEstimationModel, self).__init__()
        self.backbone = nn.Sequential(
            nn.Conv2d(3, 64, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 128, 3, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d((1, 1))
        )
        self.fc = nn.Linear(128, num_joints * 3)  # 3D coordinates
        
    def forward(self, x):
        features = self.backbone(x)
        features = features.view(features.size(0), -1)
        pose_3d = self.fc(features)
        return pose_3d.view(-1, 17, 3)  # Reshape to (batch, joints, 3)''',
        'TUTORIAL_IMPORTANT_NOTES': 'Ensure proper camera calibration for accurate 3D reconstruction. The quality of 2D pose estimation significantly affects 3D accuracy.',
        'TUTORIAL_RESULTS_CONTENT': 'Our model achieves competitive results on standard benchmarks. The following visualizations show the 3D pose predictions.',
        'TUTORIAL_IMAGE_1': '/images/tutorials/pose_estimation_result.png',
        'TUTORIAL_IMAGE_1_ALT': '3D Pose Estimation Results',
        'TUTORIAL_IMAGE_1_CAPTION': 'Sample 3D pose estimation results on test images',
        'TUTORIAL_IMAGE_2': '/images/tutorials/pose_comparison.png',
        'TUTORIAL_IMAGE_2_ALT': 'Pose Comparison',
        'TUTORIAL_IMAGE_2_CAPTION': 'Comparison with ground truth annotations',
        'TUTORIAL_CONCLUSION_CONTENT': 'This tutorial covered the essential concepts and implementation of 3D human pose estimation. You now have a solid foundation to explore more advanced techniques.',
        'TUTORIAL_LEARNING_1': 'Understanding of 3D pose estimation fundamentals',
        'TUTORIAL_LEARNING_2': 'Implementation of basic pose estimation models',
        'TUTORIAL_LEARNING_3': 'Best practices for pose estimation pipelines',
        'TUTORIAL_REFERENCE_1': 'Martinez, J., et al. "A simple yet effective baseline for 3d human pose estimation." ICCV 2017.',
        'TUTORIAL_REFERENCE_2': 'Pavlakos, G., et al. "Coarse-to-fine volumetric prediction for single-image 3d human pose." CVPR 2017.',
        'TUTORIAL_REFERENCE_3': 'Zhou, X., et al. "Towards 3d human pose estimation in the wild: a weakly-supervised approach." ICCV 2017.',
        'TUTORIAL_RELATED_1': 'pose-estimation-advanced.html',
        'TUTORIAL_RELATED_1_TITLE': 'Advanced 3D Pose Estimation Techniques',
        'TUTORIAL_RELATED_2': 'multi-view-pose.html',
        'TUTORIAL_RELATED_2_TITLE': 'Multi-View 3D Pose Estimation',
        'TUTORIAL_RESOURCE_1': 'https://github.com/example/pose-estimation-tutorial',
        'TUTORIAL_RESOURCE_2': '/tutorials/pose-estimation-tutorial.pdf'
    }
    
    return generate_tutorial(sample_data)

def interactive_tutorial_generator():
    """Interactive tutorial generator with user input."""
    
    print("🎓 Tutorial Generator")
    print("=" * 50)
    
    tutorial_data = {}
    
    # Collect tutorial information
    tutorial_data['TUTORIAL_TITLE'] = input("Tutorial Title: ")
    tutorial_data['TUTORIAL_DESCRIPTION'] = input("Description: ")
    tutorial_data['TUTORIAL_SLUG'] = input("URL Slug (e.g., my-tutorial): ")
    tutorial_data['TUTORIAL_CATEGORY'] = input("Category (Computer Vision/Generative AI/3D Vision/Motion Synthesis): ")
    tutorial_data['TUTORIAL_DIFFICULTY'] = input("Difficulty (Beginner/Intermediate/Advanced): ")
    tutorial_data['TUTORIAL_READING_TIME'] = input("Reading Time (e.g., 10 min read): ")
    
    print("\n📝 Content Sections:")
    tutorial_data['TUTORIAL_INTRO_TEXT'] = input("Introduction Text: ")
    tutorial_data['TUTORIAL_INTRODUCTION_CONTENT'] = input("Introduction Content: ")
    tutorial_data['TUTORIAL_SPECIFIC_PREREQUISITES'] = input("Specific Prerequisites: ")
    tutorial_data['TUTORIAL_OVERVIEW_CONTENT'] = input("Overview Content: ")
    
    print("\n🔑 Key Concepts (comma-separated):")
    key_concepts = input().split(',')
    tutorial_data['TUTORIAL_KEY_CONCEPT_1'] = key_concepts[0].strip() if len(key_concepts) > 0 else "Key concept 1"
    tutorial_data['TUTORIAL_KEY_CONCEPT_2'] = key_concepts[1].strip() if len(key_concepts) > 1 else "Key concept 2"
    tutorial_data['TUTORIAL_KEY_CONCEPT_3'] = key_concepts[2].strip() if len(key_concepts) > 2 else "Key concept 3"
    
    # Generate the tutorial
    output_file = generate_tutorial(tutorial_data)
    print(f"\n✅ Tutorial created successfully!")
    print(f"📁 File: {output_file}")
    print(f"🌐 URL: https://m-usamasaleem.github.io/blogs/tutorials/{tutorial_data['TUTORIAL_SLUG']}.html")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "sample":
        create_sample_tutorial()
    else:
        interactive_tutorial_generator()

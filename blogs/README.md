# Tutorial System Documentation

This directory contains the tutorial system for the Computer Vision and GenAI blog section.

## 📁 File Structure

```
blogs/
├── index.html              # Main tutorials listing page
├── template.html           # Base template for all tutorials
├── generate_tutorial.py    # Script to generate new tutorials
├── README.md              # This documentation
└── tutorials/             # Individual tutorial pages
    ├── 3d-pose-estimation.html
    └── [other tutorials...]
```

## 🚀 Quick Start

### Option 1: Interactive Generator
```bash
cd blogs
python generate_tutorial.py
```

### Option 2: Generate Sample Tutorial
```bash
cd blogs
python generate_tutorial.py sample
```

### Option 3: Manual Creation
1. Copy `template.html` to `tutorials/your-tutorial.html`
2. Replace all placeholder values (TUTORIAL_*)
3. Add your content

## 📝 Template Placeholders

The template uses the following placeholders that you need to replace:

### Basic Information
- `TUTORIAL_TITLE` - The main title of your tutorial
- `TUTORIAL_DESCRIPTION` - Meta description for SEO
- `TUTORIAL_SLUG` - URL-friendly name (e.g., "my-tutorial")
- `TUTORIAL_CATEGORY` - Computer Vision/Generative AI/3D Vision/Motion Synthesis
- `TUTORIAL_DIFFICULTY` - Beginner/Intermediate/Advanced
- `TUTORIAL_READING_TIME` - Estimated reading time (e.g., "15 min read")

### Content Sections
- `TUTORIAL_INTRO_TEXT` - Brief introduction paragraph
- `TUTORIAL_INTRODUCTION_CONTENT` - Detailed introduction
- `TUTORIAL_SPECIFIC_PREREQUISITES` - Tutorial-specific requirements
- `TUTORIAL_OVERVIEW_CONTENT` - Overview of what will be covered
- `TUTORIAL_KEY_CONCEPT_1/2/3` - Key concepts to be learned
- `TUTORIAL_IMPLEMENTATION_INTRO` - Introduction to implementation section
- `TUTORIAL_CODE_SNIPPET_1/2/3` - Code examples
- `TUTORIAL_IMPORTANT_NOTES` - Important warnings or notes
- `TUTORIAL_RESULTS_CONTENT` - Results and analysis content
- `TUTORIAL_CONCLUSION_CONTENT` - Conclusion content
- `TUTORIAL_LEARNING_1/2/3` - What readers will learn

### Images and Media
- `TUTORIAL_IMAGE_1/2` - Image file paths
- `TUTORIAL_IMAGE_1/2_ALT` - Alt text for images
- `TUTORIAL_IMAGE_1/2_CAPTION` - Image captions

### References and Links
- `TUTORIAL_REFERENCE_1/2/3` - Academic references
- `TUTORIAL_RELATED_1/2` - Related tutorial links
- `TUTORIAL_RELATED_1/2_TITLE` - Related tutorial titles
- `TUTORIAL_RESOURCE_1/2` - Additional resources (GitHub, PDFs, etc.)

## 🎨 Features

### Responsive Design
- Mobile-first approach
- Collapsible sidebar on mobile
- Responsive images and code blocks

### Navigation
- Sticky table of contents
- Smooth scrolling to sections
- Back to top functionality
- Breadcrumb navigation

### Code Highlighting
- Syntax highlighting with Prism.js
- Support for Python, JavaScript, HTML, CSS
- Copy-to-clipboard functionality

### Interactive Elements
- Search and filter on main page
- Category badges
- Difficulty indicators
- Reading time estimates

## 📋 Tutorial Guidelines

### Structure
1. **Introduction** - What the tutorial covers
2. **Prerequisites** - What readers need to know
3. **Overview** - High-level explanation
4. **Implementation** - Step-by-step code
5. **Results** - Show outputs and analysis
6. **Conclusion** - Summary and next steps
7. **References** - Academic sources

### Content Tips
- Use clear, concise language
- Include code examples
- Add visualizations when possible
- Provide practical examples
- Include troubleshooting tips
- Link to related tutorials

### Code Examples
- Use proper syntax highlighting
- Include comments explaining complex parts
- Provide complete, runnable examples
- Show expected outputs

## 🔧 Customization

### Adding New Categories
1. Update the category filter in `index.html`
2. Add category-specific styling if needed
3. Update the template categories

### Styling Changes
- Modify CSS in the template file
- Use consistent color scheme
- Maintain responsive design
- Test on different screen sizes

### Adding New Features
- Extend the template with new sections
- Add JavaScript functionality
- Include additional media types
- Enhance navigation features

## 🌐 Deployment

Tutorials are automatically accessible at:
```
https://m-usamasaleem.github.io/blogs/tutorials/[tutorial-slug].html
```

### SEO Optimization
- Use descriptive titles
- Include relevant keywords
- Add meta descriptions
- Use proper heading structure
- Include alt text for images

## 📞 Support

For questions or issues:
1. Check this documentation
2. Review existing tutorials for examples
3. Test your tutorial locally before deployment
4. Ensure all links work correctly

## 🔄 Updates

To update the template:
1. Modify `template.html`
2. Update existing tutorials if needed
3. Test changes across different browsers
4. Update this documentation

---

**Note**: This tutorial system is designed to be accessible only to those with direct links, as requested. No navigation links are provided from the main site.

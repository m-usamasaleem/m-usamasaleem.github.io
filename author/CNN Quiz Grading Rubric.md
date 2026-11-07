# CNN Quiz Grading Rubric

## Convolution Operations and Filter/Kernel Mechanics (25%)
- **good**: Correctly performs most convolution calculations with minor arithmetic errors, understands stride and padding concepts, and can generally explain filter behavior and weight sharing with only slight conceptual gaps.
- **excellent**: Accurately computes convolution outputs by hand, correctly applies stride and padding, demonstrates clear understanding of how filters detect local features, and explains shared weights and their role in translation invariance with no errors.
- **satisfactory**: Demonstrates basic understanding of convolution as a sliding operation and can set up calculations, but makes recurring arithmetic mistakes or shows partial confusion about stride, padding, or the role of individual filter weights.
- **needs_improvement**: Shows fundamental misunderstanding of the convolution operation, cannot correctly apply filters to input data, confuses key terms such as stride and padding, or leaves calculations incomplete or entirely incorrect.

## Feature Map Dimensions and Pooling Layers (20%)
- **good**: Calculates feature map dimensions correctly in most cases with isolated formula errors, understands pooling types and their general purpose, and only makes minor mistakes when combining multiple parameters.
- **excellent**: Correctly derives output feature map dimensions using the standard formula for any combination of input size, kernel size, stride, and padding; accurately explains max and average pooling, their effect on spatial dimensions, and their role in reducing computation and controlling overfitting.
- **satisfactory**: Can apply the dimension formula in straightforward cases but struggles when stride or padding takes non-default values; understands that pooling reduces spatial size but confuses max and average pooling behavior or their specific benefits.
- **needs_improvement**: Cannot reliably compute output dimensions, applies the formula incorrectly or inconsistently, and demonstrates little understanding of what pooling layers do or why they are used in CNN architectures.

## Backpropagation Through Convolutional Layers (20%)
- **good**: Demonstrates solid understanding of backward pass through convolution with minor gaps, correctly identifies that shared weights accumulate gradients, and generally explains pooling gradient routing with only small inaccuracies.
- **excellent**: Clearly explains how gradients flow backward through convolutional layers, correctly describes how filter weights are updated via gradient descent, addresses the role of the chain rule, and accurately discusses how pooling layers handle gradient routing (e.g., max pooling mask).
- **satisfactory**: Shows a general awareness that backpropagation updates filter weights and that gradients pass backward, but cannot precisely explain the mechanics of gradient accumulation for shared weights or the handling of gradients through pooling.
- **needs_improvement**: Confuses forward and backward passes, cannot explain how filter weights are updated, or demonstrates a fundamental misunderstanding of how the chain rule applies in the context of convolutional layers.

## CNN Architecture Design Principles (20%)
- **good**: Demonstrates sound understanding of common architectural patterns and can justify most design decisions; may overlook nuanced trade-offs or provide incomplete reasoning for one or two choices but shows overall competency.
- **excellent**: Articulates well-reasoned design choices such as progressively increasing filter depth, decreasing spatial resolution, appropriate use of activation functions, batch normalization, and dropout; can justify trade-offs between depth, width, and computational cost with reference to established architectures (e.g., VGG, ResNet concepts).
- **satisfactory**: Identifies basic architectural components and their typical ordering but provides limited or superficial justification for design choices; may conflate the purpose of different layers or show uncertainty about when to apply regularization techniques.
- **needs_improvement**: Cannot describe a coherent CNN architecture, misorders or misidentifies layer types, provides no meaningful justification for design decisions, or demonstrates significant confusion about the purpose of core architectural components.

## Practical Implementation Considerations (15%)
- **good**: Shows awareness of most key implementation considerations and connects them reasonably to theory; may miss one area such as weight initialization or provide a slightly imprecise explanation of a technique without major conceptual errors.
- **excellent**: Accurately addresses practical topics such as data preprocessing and normalization, weight initialization strategies, learning rate selection, and common pitfalls (vanishing gradients, overfitting); can connect theoretical concepts to real implementation decisions with specific and correct examples.
- **satisfactory**: Mentions common implementation steps like normalization or dropout but lacks depth or precision; explanations are generic and do not demonstrate a strong link between theory and practice, or one significant area is overlooked.
- **needs_improvement**: Demonstrates little awareness of practical implementation requirements, provides incorrect guidance on preprocessing or training procedures, or cannot connect any theoretical CNN concepts to what would be done in a real implementation.

## Conceptual Clarity and Reasoning Quality (10%)
- **good**: Answers are generally clear and use mostly correct terminology; reasoning is sound with only minor lapses in precision or organization, and the student shows coherent understanding of the subject with rare inconsistencies.
- **excellent**: Answers are precise, well-organized, and use correct technical terminology throughout; reasoning is logical and complete, explanations are concise without sacrificing accuracy, and the student demonstrates integrated understanding across multiple CNN topics.
- **satisfactory**: Answers convey a basic understanding but use imprecise or inconsistent terminology; reasoning is sometimes circular or incomplete, and the student struggles to connect ideas across different parts of the quiz.
- **needs_improvement**: Answers are unclear, poorly organized, or rely heavily on incorrect terminology; reasoning is difficult to follow or largely absent, and the student does not demonstrate an integrated understanding of CNN concepts.

## DataCompression&Visualizer

```bash
DataCompression&Visualizer is an interactive visualization tool for binary encoding trees used in data compression algorithms.
It animates the construction of a binary tree from a set of characters and their frequencies,
helping users intuitively understand how codes are assigned to minimize storage space.
```

### Features

```text
Animated Tree Construction: Step-by-step visualization of tree building.

Bit Assignment Display: Shows the binary codes assigned to each character.

Interactive & Sequential Animation: Leaves, edges, and bit labels appear gradually for clarity.

High-Quality Video Output: Export animations in 1080p or higher resolution.

Educational Tool: Ideal for learning compression algorithms, coding theory, or data structures.
```

### Installation

```bash
Clone the repository:

git clone https://github.com/yourusername/CodeTreeViz.git
cd CodeTreeViz


Install dependencies:

pip install manim


⚠ Make sure you have ffmpeg installed for video rendering.
```

### Usage

```text
Define your characters and frequencies in main.py:

s = "abcdef"
freq = [5, 9, 10, 3, 23, 19]
```

### Run the animation:

```text
manim -pqh animate.py HuffmanTree


-pqh → preview high-quality (1080p60fps).

The output video will be in media/videos/animate/1080p60/HuffmanTree.mp4.
```

### How it Works

```
Builds a binary tree from character frequencies.

Assigns shorter codes to more frequent characters.

Recursively animates the tree with edges and node labels.

Displays final codes for each character at the bottom of the animation.
```

### License

```text
MIT License © 2025 Aryan Sinha
```

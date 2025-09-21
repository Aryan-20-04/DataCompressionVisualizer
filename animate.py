from manim import *
from main import s, freq, huffmanCodes
class HuffmanTree(Scene):
    def construct(self):
        root, codes = huffmanCodes(s, freq)
    
        depth = self.get_tree_depth(root)
        
        y_position = max(2, 4 - depth * 0.5)
        start_y = UP * y_position
        root_circle = self.draw_node(root, start_y, color=YELLOW)
        
        initial_x_offset = max(2.5, min(4.5, 9 / max(depth, 1)))
        initial_y_offset = max(1.2, min(2.0, 4 / max(depth, 1)))
        
        self.draw_tree(root, root_circle, initial_x_offset, initial_y_offset)
        self.wait(1)
        
        self.display_codes(codes)
        self.wait(2)

    def get_tree_depth(self, node, current_depth=0):
        if not node:
            return current_depth
        
        if not hasattr(node, 'left') or not hasattr(node, 'right'):
            return current_depth + 1
            
        if node.left is None and node.right is None:
            return current_depth + 1
        
        left_depth = self.get_tree_depth(node.left, current_depth + 1) if node.left else current_depth
        right_depth = self.get_tree_depth(node.right, current_depth + 1) if node.right else current_depth
        
        return max(left_depth, right_depth)

    def draw_node(self, node, pos, color=BLUE):
        """Draw a single node with character and frequency"""
        circle = Circle(radius=0.35, color=color).move_to(pos)
        
        if hasattr(node, 'char') and node.char:
            char_display = node.char if node.char != ' ' else 'SP'
            label = Text(f"{char_display}:{node.data}", font_size=18).move_to(pos)
        else:
            label = Text(str(node.data), font_size=18).move_to(pos)
        
        self.play(Create(circle), Write(label), run_time=0.4)
        return VGroup(circle, label)

    def draw_tree(self, node, parent_vgroup, x_offset, y_offset):
        if not node or not hasattr(node, 'left') or not hasattr(node, 'right'):
            return
        if node.left is None and node.right is None:
            return

        parent_pos = parent_vgroup.get_center()
        
        if node.left:
            left_pos = parent_pos + LEFT * x_offset + DOWN * y_offset
            if abs(left_pos[0]) < 7.5 and left_pos[1] > -3.5:
                left_circle = self.draw_node(node.left, left_pos)
                
                line_left = Line(parent_pos, left_pos, color=WHITE)
                self.play(Create(line_left), run_time=0.2)
                
                label_pos = (parent_pos + left_pos) / 2
                zero_label = Text("0", font_size=14, color=GREEN).move_to(label_pos)
                self.play(Write(zero_label), run_time=0.2)
                
                self.draw_tree(node.left, left_circle, x_offset * 0.75, y_offset * 0.9)

        if node.right:
            right_pos = parent_pos + RIGHT * x_offset + DOWN * y_offset
            if abs(right_pos[0]) < 7.5 and right_pos[1] > -3.5:
                right_circle = self.draw_node(node.right, right_pos)
                line_right = Line(parent_pos, right_pos, color=WHITE)
                self.play(Create(line_right), run_time=0.2)
                label_pos = (parent_pos + right_pos) / 2
                one_label = Text("1", font_size=14, color=RED).move_to(label_pos)
                self.play(Write(one_label), run_time=0.2)
                self.draw_tree(node.right, right_circle, x_offset * 0.75, y_offset * 0.9)

    def display_codes(self, codes):
        code_title = Text("Huffman Codes:", font_size=24, color=YELLOW)
        code_title.to_edge(UP).shift(DOWN * 0.3)
        self.play(Write(code_title))
        code_texts = []
        items = list(codes.items())
        cols = min(3, len(items))
        rows = (len(items) + cols - 1) // cols
        
        for i, (char, code) in enumerate(items):
        
            char_display = char if char != ' ' else 'SPACE'
            text = Text(f"{char_display}: {code}", font_size=18)
         
            col = i % cols
            row = i // cols
            
            start_x = -(cols - 1) * 1.5
            pos = (start_x + col * 3) * RIGHT + (1.5 - row * 0.5) * DOWN
            text.move_to(pos)
            code_texts.append(text)
        
        code_group = VGroup(*code_texts)
        self.play(FadeIn(code_group, shift=UP), run_time=1)

    def show_codes(self, codes):
        title = Text("Generated Codes:", font_size=20, color=YELLOW)
        title.to_edge(DOWN).shift(UP * 2)
        self.play(Write(title))
        
        code_texts = []
        for i, (char, code) in enumerate(codes.items()):
            text = Text(f"{char}: {code}", font_size=16)
            text.next_to(title, DOWN, buff=0.3 + i * 0.3)
            code_texts.append(text)
        
        for text in code_texts:
            self.play(Write(text), run_time=0.3)
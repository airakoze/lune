from unidecode import unidecode

class Lune_Parser:
    # Transform utf characters to unicode 
    # since Lune is compatible with utf characters
    def transform_to_unicode(self, string):
        return unidecode(string)

    def translate(self, tree):
        if tree.data == "block":
            return "\n".join(map(self.translate, tree.children))
        elif tree.data == "assignment": 
            left_hand, right_hand = tree.children
            return self.transform_to_unicode(left_hand.children[0]) + " = " + self.transform_to_unicode(right_hand.children[0])
        elif tree.data == "var":
            return self.transform_to_unicode(tree.children[0])
        elif tree.data == "literal":
            return self.transform_to_unicode(tree.children[0])
        elif tree.data == "greater_than":
            left_hand, right_hand = tree.children
            return self.translate(left_hand) + " > " + self.translate(right_hand)
        elif tree.data == "less_than":
            left_hand, right_hand = tree.children
            return self.translate(left_hand) + " < " + self.translate(right_hand)
        elif tree.data == "greater_equal":
            left_hand, right_hand = tree.children
            return self.translate(left_hand) + " >= " + self.translate(right_hand)
        elif tree.data == "less_equal":
            left_hand, right_hand = tree.children
            return self.translate(left_hand) + " <= " + self.translate(right_hand)
        elif tree.data == "equal":
            left_hand, right_hand = tree.children
            return self.translate(left_hand) + " == " + self.translate(right_hand) 
        elif tree.data == "not_equal":
            left_hand, right_hand = tree.children
            return self.translate(left_hand) + " ~= " + self.translate(right_hand) 
        elif tree.data == "or":
            left_hand, right_hand = tree.children
            return self.translate(left_hand) + " or " + self.translate(right_hand) 
        elif tree.data == "and":
            left_hand, right_hand = tree.children
            return self.translate(left_hand) + " and " + self.translate(right_hand) 
        elif tree.data == "or_symbol":
            left_hand, right_hand = tree.children
            return self.translate(left_hand) + " | " + self.translate(right_hand) 
        elif tree.data == "and_symbol":
            left_hand, right_hand = tree.children
            return self.translate(left_hand) + " & " + self.translate(right_hand) 
        elif tree.data == "lshift":
            left_hand, right_hand = tree.children
            return self.translate(left_hand) + " << " + self.translate(right_hand) 
        elif tree.data == "rshift":
            left_hand, right_hand = tree.children
            return self.translate(left_hand) + " >> " + self.translate(right_hand) 
        elif tree.data == "str_concat":
            left_hand, right_hand = tree.children
            return self.translate(left_hand) + " .. " + self.translate(right_hand) 
        elif tree.data == "add":
            left_hand, right_hand = tree.children
            return self.translate(left_hand) + " + " + self.translate(right_hand) 
        elif tree.data == "sub":
            left_hand, right_hand = tree.children
            return self.translate(left_hand) + " - " + self.translate(right_hand) 
        elif tree.data == "mult":
            left_hand, right_hand = tree.children
            return self.translate(left_hand) + " * " + self.translate(right_hand) 
        elif tree.data == "div":
            left_hand, right_hand = tree.children
            return self.translate(left_hand) + " / " + self.translate(right_hand) 
        elif tree.data == "int_div":
            left_hand, right_hand = tree.children
            return self.translate(left_hand) + " // " + self.translate(right_hand)
        elif tree.data == "mod":
            left_hand, right_hand = tree.children
            return self.translate(left_hand) + " % " + self.translate(right_hand)
        elif tree.data == "exp":
            left_hand, right_hand = tree.children
            return self.translate(left_hand) + " ^ " + self.translate(right_hand)
        elif tree.data == "not":
            return "not " + self.translate(tree.children[0])
        elif tree.data == "negation":
            return "-" + self.translate(tree.children[0])
        elif tree.data == "hashtag":
            return "#" + self.translate(tree.children[0])
        elif tree.data == "function_args":
            return "("  + self.translate(tree.children[0]) + ")"
        elif tree.data == "if_statement":
            expression, block, elseif, optional_else = tree.children
            return "if " + self.translate(expression) + "\nthen\n" + self.translate(block) + self.translate(elseif) + self.translate(optional_else) + "\nend\n"
        elif tree.data == "while_statement":
            expression, block = tree.children
            return "while\n" + self.translate(expression) + "\ndo\n" + self.translate(block) + "\nend\n"
        elif tree.data == "repeat_statement":
            block, expression = tree.children
            return "repeat\n" + block + "until\n" + expression 
        elif tree.data == "do_statement":
            block = tree.children
            return "do\n" + self.translate(block) + "\nend\n"
        elif tree.data == "break_statement":
            return "\nbreak\n"
        elif tree.data == "range": 
            exp1, exp2, exp3 = tree.children
            temp_exp3 = ", " + self.translate(exp2) if self.translate(exp3) else ""
            return self.translate(exp1) + ", " + self.translate(exp2) +  temp_exp3
        elif tree.data == "for_statement1":
            pass
        elif tree.data == "for_statement2":
            pass
        elif tree.data == "local_function":
            pass
        elif tree.data == "local_variable":
            pass
        elif tree.data == "not_expression":
            pass
        elif tree.data == "nil_value":
            pass
        elif tree.data == "false_value":
            pass
        elif tree.data == "true_value":
            pass
        elif tree.data == "function_definition":
            pass
        else:
            return ""
            # print(tree.data)
            # raise SyntaxError("Lune syntaxe invalide (Invalid Lune syntax)")

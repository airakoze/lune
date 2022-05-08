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
            if len(tree.children) == 1:
                return self.transform_to_unicode(tree.children[0])
            else:
                mult_var = ""
                for token in tree.children[1:]:
                    mult_var += ", " + self.transform_to_unicode(token)
                return self.transform_to_unicode(tree.children[0]) + mult_var
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
            return "while " + self.translate(expression) + "\ndo\n" + self.translate(block) + "\nend\n"
        elif tree.data == "repeat_statement":
            block, expression = tree.children
            return "repeat\n" + self.translate(block) + "\nuntil\n" + self.translate(expression)
        elif tree.data == "do_statement":
            block = tree.children
            return "do\n" + self.translate(block) + "\nend\n"
        elif tree.data == "break_statement":
            return "\nbreak\n"
        elif tree.data == "range": 
            exp1, exp2, exp3 = tree.children
            opt_exp3 = "," + exp3 if exp3 else ""
            return exp1 + "," + exp2 + opt_exp3
        elif tree.data == "for_statement":
            var, for_range, block = tree.children
            return "for " + var + " = " + self.translate(for_range) + "\ndo\n" + self.translate(block) + "\nend\n"
        elif tree.data == "function":
            function_name, args, block = tree.children
            return "function " + function_name + " (" + self.translate(args) + ")\n" + self.translate(block) + "\nend\n"
        elif tree.data == "return": 
            exp = tree.children[0]
            return "return " + self.translate(exp)
        elif tree.data == "local_function":
            function_name, args, block = tree.children
            return "local function " + function_name + " (" + self.translate(args) + ")\n" + self.translate(block) + "\nend\n"
        elif tree.data == "function_call":
            function_name, var = tree.children
            return function_name + "(" + self.translate(var) + ")"
        elif tree.data == "table":
            var, table_constructor = tree.children
            return self.translate(var) + "=" + self.translate(table_constructor)
        elif tree.data == "table_constructor":
            exp = tree.children[0]
            print(exp)
            opt_exp = self.translate(exp) if self.translate(exp) else ""
            return "{" + opt_exp + "}"
        else:
            return ""
            # print(tree.data)
            # raise SyntaxError("Lune syntaxe invalide (Invalid Lune syntax)")

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        pos_stack = []
        neg_stack = []
        for aster in asteroids:
            if aster >0:
                pos_stack.append(aster)
            if aster < 0:
                final_val = None
                if pos_stack:
                    while pos_stack:
                        val = aster+pos_stack[-1]
                        final_val = val
                        if val <0:
                            pos_stack.pop()
                        elif val == 0:
                            pos_stack.pop()
                            break
                        else:
                            break
                if final_val is None or final_val<0:
                    neg_stack.append(aster)
        return neg_stack + pos_stack


        
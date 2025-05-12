class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        from collections import deque 

        recipe_queue = deque(range(len(recipes)))
        
        last_size = 0 

        supplies = set(supplies)
        ans = []
        # if there is no change.
        while len(supplies) > last_size:
            last_size = len(supplies)
            q_size = len(recipe_queue)
            while q_size:
                q_size -= 1
                idx = recipe_queue.popleft()
                if all(ingredient in supplies for ingredient in ingredients[idx]):
                    supplies.add(recipes[idx])
                    ans.append(recipes[idx])
                else:
                    recipe_queue.append(idx)
        return ans

        
            

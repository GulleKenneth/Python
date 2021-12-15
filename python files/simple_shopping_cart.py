class ShoppingCart(object):
    cart = []
        
    def add_cart(self, item):
        self.cart.append(item)
        print(f'{item} has been added to cart.')
    
    def remove_cart(self, item):
        try:
            self.cart.remove(item)
            print(f'{item} has been remove to cart.')
            
        except:
            print(f'Sorry we could not remove that item!')
        
    def clear_cart(self):
        self.cart.clear()
        print(f'You cart is empty!')
        
    def show_cart(self):
        if self.cart:
            print(f'Here is your cart')
        
            for item in self.cart:
                print(f'{item}')
        else:
            print(f'Your cart is empty')
        
    def main(self):
        done = False
        
        while not done:
            ans = input("quit/add/remove/show/clear: ").lower()
            
            if ans == 'quit':
                print('Thanks for using our program. ')
                self.show_cart()
                done = True
                
            elif ans == 'add':
                item = input('Add item in cart: ').title()
                self.add_cart(item)
            
            elif ans == 'remove':
                item = input('Enter item you would what to remove in cart: ').title()
                self.remove_cart(item)    
                
            elif ans == 'show':
                self.show_cart()
                
            elif ans == 'clear':
                self.clear_cart()    
            
            else:
                print("Sorry that was not an option.")             
    
if __name__ == '__main__':
    a = ShoppingCart()
    a.main()
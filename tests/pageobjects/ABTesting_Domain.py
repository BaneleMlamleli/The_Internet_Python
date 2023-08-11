class ABTestingDomain(object):
    def __init__(self, link, ABTestControl):
        self.link = link
        self.ABTestControl = ABTestControl
    
    def __init__(self, link):
        self.link = link
        
    def __init__(self, ABTestControl):
        self.ABTestControl = ABTestControl
        
    def welcome_page(self):
        print('Welcome page')
        
    def click_link(self):
        print(f'click on {self.link}')
    
    def redirect(self):
        print(f'redirected to the {self.ABTestControl} page')
#imports
import pygame 
import sys
import random
import os

class FlappyBird:
    
    def __init__(self):
        
        #initialize variables
        self.folder = "repos/flappy_bird_pygame/flappy_bird/"
        self.score = 0
        self.high_score = 0
        self.high_score_name = []
        self.high_score_num = []

        #load high score from file
        self.load_high_score(f"{self.folder}high_score.txt")
        
        #initialize pygame
        pygame.init()

        #fonts and texts
        self.text_color = (0, 0, 0)
        self.font1 = pygame.font.SysFont("Courier", 60)
        self.font2 = pygame.font.SysFont("Arial", 30)

        #create window 
        window_width = 550
        window_height = 650
        self.window1 = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Flappy bird")
        self.clock = pygame.time.Clock()
        
        #load images
        
        #load bird image
        bird_img1 = pygame.image.load((f"{self.folder}bird.png"))
        self.bird_img = pygame.transform.scale(bird_img1, (70, 54))

        #load pipe image 
        pipe_img1 = pygame.image.load((f"{self.folder}pipe.png"))
        self.down_pipe_img = pygame.transform.scale(pipe_img1, (69, 758))

        #flip pipe img 
        self.top_pipe_img = pygame.transform.flip(self.down_pipe_img, False, True)
        
        #start screen loop
        self.start_screen_loop()
        
    #game over function
    def game_over(self):
        if len(self.high_score_name) > 0:
            low_high_score = self.high_score_num[-1]
            if self.score > low_high_score or len(self.high_score_name) < 5 and self.score > 0:
                self.high_score_window_loop()
            else:
                self.game_over_loop()
        elif len(self.high_score_name) == 0 and self.score > 0:
            self.high_score_window_loop()
        else:
            self.game_over_loop()
            
        
    #function that checks if a txt file is empty
    def is_empty(self, file):
        if os.stat(file).st_size > 0:
            return False
        else:
            return True
        
    #function for encrypting a num
    def encrypt(self, num):
        list1 = list(str(num))
        list1 = [int(s) for s in list1]
        list2 = []
        str1 = ""
        for i in list1:
            list2.append(chr(i + 110))
        list2.reverse()
        for i in list2:
            str1 += i
        return str1

    #function for deencrypting a text into a num
    def deencrypt(self, text):
        list1 = list(text)
        list2 = []
        str1 = ""
        for i in list1:
            list2.append(ord(i) - 110)
        list2.reverse()
        for i in list2:
            str1 += str(i)
        return int(str1)
    
    #loads high score from file 
    def load_high_score(self, file1):
        high_score_file = open(file1, "a")
        high_score_file.close()
        if not self.is_empty(file1):
            with open(file1, "r") as high_score_file:
                high_score_table = high_score_file.read()
                high_score_list = high_score_table.splitlines()
                self.high_score_name = []
                self.high_score_num = []
                for i in high_score_list:
                    var = i.split("/")
                    self.high_score_name.append(var[0])
                    self.high_score_num.append(self.deencrypt(var[1]))
                self.high_score_num = [int(s) for s in self.high_score_num]
                self.high_score = self.high_score_num[0]

    #write the scores into a txt file
    def write_high_scores(self, file1):
        with open(file1, "w") as high_score_file:
            for idx, i in enumerate(self.high_score_name):
                high_score_file.write(f"{i}/{self.encrypt(self.high_score_num[idx])}\n")
        
    def start_screen_loop(self):
        
        #texts
        flappy_bird_text = self.font1.render("Flappy bird", True, self.text_color)
        jump_start_text = self.font2.render("Press the Jump button to start", True, self.text_color)
        high_score_text = self.font2.render(f"High score: {self.high_score}", True, self.text_color)
        
        #start screen loop
        while True:

            #set fps
            self.clock.tick(20)
            
            #sets window color
            self.window1.fill((135, 206, 235))
            
            #render text
            self.window1.blit(flappy_bird_text, (70, 110))
            self.window1.blit(jump_start_text, (110, 250))
            self.window1.blit(high_score_text, (190, 320))
            
            #checking for events
            for event in pygame.event.get():
                
                #exit the app
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    return
                    
                #binds
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_SPACE:
                        self.main_loop()
                        return
                        
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        return
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.main_loop()
                        return
            
            #update the window
            pygame.display.update()
    
    def main_loop(self):
        
        #initialize variables
        birdx = 110
        birdy = 150   
        bird_width = 70
        bird_height = 54
        pipe_width = 69   
        pipe_height = 758
        bird_speed = 0
        gravity = 0.5
        jump_strength = 9.5
        pipe1x = 650 
        pipe1y = random.randint(225, 575)
        pipe2x = 975
        pipe2y = random.randint(225, 575)
        pipe3x = 1300
        pipe3y = random.randint(225, 575)
        pipe_space = 950
        pipe_pause = 325
        pipe_speed = 2.5
        pipe1_counted = False
        pipe2_counted = False
        pipe3_counted = False
        self.score = 0
                
        #text 
        score_text = self.font2.render(f"Score: {self.score}", True, self.text_color)
        
        #main game loop
        while True:
            
            #set fps
            self.clock.tick(60)
            
            #sets window color
            self.window1.fill((135, 206, 235))
            
            #check for events
            for event in pygame.event.get():
                
                #check for quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    return
                    
                #check for key presses that trigger a jump
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_SPACE:
                        bird_speed = -jump_strength
                        
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        return
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        bird_speed = -jump_strength
                        
            #moves pipes and bird by adjusting position variables
            bird_speed += gravity
            birdy += bird_speed
            pipe1x -= pipe_speed
            pipe2x -= pipe_speed
            pipe3x -= pipe_speed
            
            #hitboxes
            bird_rect = pygame.Rect(birdx + 5, birdy + 3, bird_width - 5, bird_height - 3)
            down_pipe1_rect = pygame.Rect(pipe1x, pipe1y, pipe_width, pipe_height)
            top_pipe1_rect = pygame.Rect(pipe1x, pipe1y - pipe_space, pipe_width, pipe_height)
            down_pipe2_rect = pygame.Rect(pipe2x, pipe2y, pipe_width, pipe_height)
            top_pipe2_rect = pygame.Rect(pipe2x, pipe2y - pipe_space, pipe_width, pipe_height)
            down_pipe3_rect = pygame.Rect(pipe3x, pipe3y, pipe_width, pipe_height)
            top_pipe3_rect = pygame.Rect(pipe3x, pipe3y - pipe_space, pipe_width, pipe_height)
            
            #check for collisions or bird getting out of bounds
            if bird_rect.colliderect(down_pipe1_rect) or bird_rect.colliderect(down_pipe2_rect) or bird_rect.colliderect(down_pipe3_rect):
                self.game_over()
                return
            if bird_rect.colliderect(top_pipe1_rect) or bird_rect.colliderect(top_pipe2_rect) or bird_rect.colliderect(top_pipe3_rect):
                self.game_over()
                return
            if birdy < -3 or birdy > 653 - bird_height:
                self.game_over()
                return

            #checks if pipes are at the end of the screen and if so, moves them to the start
            if pipe1x < -100:
                pipe1x = pipe3x + pipe_pause
                pipe1y = random.randint(225, 575)
                pipe1_counted = False
            if pipe2x < -100:
                pipe2x = pipe1x + pipe_pause
                pipe2y = random.randint(225, 575)
                pipe2_counted = False
            if pipe3x < -100:
                pipe3x = pipe2x + pipe_pause
                pipe3y = random.randint(225, 575)
                pipe3_counted = False
            
            #places all images at their desired spot 
            self.window1.blit(self.bird_img, (birdx, birdy))
            
            pipe_arr = [(pipe1x, pipe1y), (pipe2x, pipe2y), (pipe3x, pipe3y)]
            for pipe in pipe_arr:
                self.window1.blit(self.down_pipe_img, (pipe[0], pipe[1]))
                self.window1.blit(self.top_pipe_img, (pipe[0], pipe[1] - pipe_space))
            
            #increases the score if the bird has passed a pipe
            if pipe1x < birdx and not pipe1_counted:
                self.score += 1
                pipe1_counted = True
            
            if pipe2x < birdx and not pipe2_counted:
                self.score += 1
                pipe2_counted = True
            
            if pipe3x < birdx and not pipe3_counted:
                self.score += 1
                pipe3_counted = True
            
            #score text 
            score_text = self.font2.render(f"Score: {self.score}", True, self.text_color)
            self.window1.blit(score_text, (220, 600))
            
            #displays all updates that happened
            pygame.display.update()
        
    #high score window loop
    def high_score_window_loop(self):
        
        #initialize variables
        name_input = ""
        num = 0
        
        #text
        you_got_text = self.font2.render(f"You got one of the top 5 highest scores!", True, self.text_color)
        insert_name_text = self.font2.render(f"Insert a 3 letter name:", True, self.text_color)
        score_text = self.font2.render(f"Score: {self.score}", True, self.text_color)
        
        #loop
        while True:
            
            #set fps
            self.clock.tick(20)
            
            #sets window color
            self.window1.fill((135, 206, 235))
            
            #text
            name_display = self.font2.render(name_input + "|", True, self.text_color)
            self.window1.blit(name_display, (255 - (len(name_input) * 6.3), 240))
            self.window1.blit(you_got_text, (60, 100))
            self.window1.blit(score_text, (220, 150))
            self.window1.blit(insert_name_text, (145, 200))
            
            #checking for events
            for event in pygame.event.get():
                
                #exit the app
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    return
                    
                #binds
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        return
                        
                    elif event.key == pygame.K_RETURN and len(name_input) > 0 and name_input not in self.high_score_name:
                        
                        #process scores
                        num = 0
                        for i in self.high_score_num:
                            if self.score > i:
                                num += 1
                                
                        if num > 0:
                            self.high_score_name.insert(-num, name_input)
                            self.high_score_num.insert(-num, self.score)
                        else:
                            self.high_score_name.append(name_input)
                            self.high_score_num.append(self.score)

                        #make the high score lists 5 items long
                        self.high_score_name = self.high_score_name[:5]
                        self.high_score_num = self.high_score_num[:5]
                        
                        self.high_score = self.high_score_num[0]
                        
                        self.write_high_scores(f"{self.folder}high_score.txt")
                        
                        self.game_over_loop()
                        return
                        
                    elif event.key == pygame.K_RETURN and len(name_input) == 0 :
                        self.game_over_loop()
                        return

                    elif event.key == pygame.K_BACKSPACE:
                        name_input = name_input[:-1]

                    elif len(name_input) < 3 and event.unicode.isalpha():
                        name_input += event.unicode.upper()
                        
            #update the window
            pygame.display.update()
        
    #game over loop
    def game_over_loop(self):
        
        #text
        game_over_text = self.font1.render("Game over", True, self.text_color)
        restart_text = self.font2.render("Press backspace to retry", True, self.text_color)
        high_scores_text = self.font2.render(f"Top 5 highest scores:", True, self.text_color)
        
        if len(self.high_score_name) > 0:
            high_scores_text = self.font2.render(f"Top 5 highest scores:", True, self.text_color)
        else:
            high_scores_text = self.font2.render("", True, self.text_color)
    
        while True:
            
            #set fps
            self.clock.tick(20)
            
            #sets window color
            self.window1.fill((135, 206, 235))
            
            #render text
            self.window1.blit(game_over_text, (100, 5))
            self.window1.blit(restart_text, (130, 70))
            score_text = self.font2.render(f"Score: {self.score}", True, self.text_color)
            self.window1.blit(score_text, (220, 115))
            
            self.window1.blit(high_scores_text, (140, 160))
            
            high_score_y = 240
            for idx, i in enumerate(self.high_score_name):
                high_score_text = self.font2.render(i, True, self.text_color)
                high_score_text2 = self.font2.render(str(self.high_score_num[idx]), True, self.text_color)
                self.window1.blit(high_score_text, (100, high_score_y))
                self.window1.blit(high_score_text2, (390 - (10 * len(str(self.high_score_num[idx]))), high_score_y))
                high_score_y += 70
            
            #checking for events
            for event in pygame.event.get():
                
                #exit the app
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    return
                    
                #binds
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_BACKSPACE:
                        self.main_loop()
                        return
                        
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        return
            
            #update the window
            pygame.display.update()
            
if __name__ == "__main__":
    game = FlappyBird()
    pygame.quit()
    sys.exit()
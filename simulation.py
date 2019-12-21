import tkinter as tk

print('첫번째 공의 질량 : ')
fball_mess=input()
fball_mess=float(fball_mess)
print('첫번째 공의 속력 : ')
fball_velo=input()
fball_velo=float(fball_velo)
print('두번째 공의 질량 : ')
sball_mess=input()
sball_mess=float(sball_mess)
print('두번째 공의 속력 : ')
sball_velo=input()
sball_velo=float(sball_velo)

class simul(tk.Frame):
    def __init__(self,master):
        super(simul,self).__init__(master)
        self.width = 600
        self.height = 400
        self.before=False
        self.canvas = tk.Canvas(self,bg = '#aaaaaa',width = self.width,
                                height = self.height)
        self.canvas.pack()
        self.pack()

        self.fball = Ball(self.canvas,self.width*(9/20),self.height*(1/2),10,
                         fball_mess,fball_velo,0.0,'white')
        self.sball = Ball(self.canvas,self.width*(11/20),self.height*(1/2),10,
                         sball_mess,sball_velo,0.0,'black')

        self.simul_loop()
        self.canvas.focus_set()
        pass

    def simul_loop(self):
        self.check_collision()
        self.fball.update()
        self.sball.update()
        self.after(50,self.simul_loop)
        pass

    def check_collision(self):
        if self.before==True:
            pass
        else:
            fball_coords = self.fball.get_position()
            sball_coords = self.sball.get_position()
            if fball_coords[2]>=sball_coords[0]:
                mid_mess=(fball_mess+sball_mess)/2
                fball_nextx_velocity=self.fball.x_velocity+sball_mess*((self.sball.x_velocity-self.fball.x_velocity)/mid_mess)
                sball_nextx_velocity=self.sball.x_velocity+fball_mess*((self.fball.x_velocity-self.sball.x_velocity)/mid_mess)
                self.fball.x_velocity=fball_nextx_velocity
                self.sball.x_velocity=sball_nextx_velocity
                self.before=True
                pass
            pass
        pass
    pass


class simulOBJ:
    def __init__(self,canvas,item):
        self.canvas = canvas
        self.item = item
        pass

    def get_position(self):
        return self.canvas.coords(self.item)

    def move(self,x,y):
        self.canvas.move(self.item,x,y)
        pass
    pass

class Ball(simulOBJ):
    def __init__(self,canvas,x,y,radius,mess,xv,yv,color):
        self.radius = radius
        self.x_velocity = xv
        self.y_velocity = yv
        item = canvas.create_oval(x-self.radius,y-self.radius,
                                  x+self.radius,y+self.radius,
                                  fill=color)
        super(Ball,self).__init__(canvas,item)
        pass

    def update(self):
        coords = self.get_position()
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        x=self.x_velocity
        y=self.y_velocity
        self.move(x,y)
        pass
    pass

if __name__ == '__main__':
    root = tk.Tk()
    root.title('물리학 시뮬레이션')
    game = simul(root)
    game.mainloop()


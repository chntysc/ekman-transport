from manimlib.imports import *

class EkmanTransportNorthernHemisphere(ThreeDScene):
    def construct(self):
        self.add_sound("hidro/ekman.wav")
        judul = TextMobject("Transpor Ekman\\\\",
                            "di BBU", arg_separator="").scale(0.8).set_color_by_gradient(BLUE_B, TEAL)
        self.add_fixed_in_frame_mobjects(judul)  # <----- Add this
        judul.to_corner(UL)
        self.wait()

        self.set_camera_orientation(phi=30 * DEGREES, theta=-90 * DEGREES)

        cube = Cube(side_length=5, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(GREEN_B)
        self.play(ShowCreation(cube))

        #wind flow
        #1
        arah1 = np.array([2, 0, 3])
        wind1 = Polygon(UP*0.5 + LEFT*0.5, ORIGIN, DOWN*0.5 + LEFT*0.5, RIGHT*0.5).scale(1)
        wind1.move_to(arah1)


        #2
        arah2 = np.array([1, 0, 3])
        wind2 = wind1.copy()
        wind2.move_to(arah2)

        #3
        arah3 = np.array([0, 0, 3])
        wind3 = wind1.copy()
        wind3.move_to(arah3)

        #4
        arah4 = np.array([-1, 0, 3])
        wind4 = wind1.copy()
        wind4.move_to(arah4)

        #5
        arah5 = np.array([-2, 0, 3])
        wind5 = wind1.copy()
        wind5.move_to(arah5)

        wind = VGroup(wind1, wind2, wind3, wind4, wind5)
        self.play(Write(wind))

        #text wind
        textnorth = TextMobject("Utara")
        textnorth.next_to(wind1, RIGHT)
        self.play(Write(textnorth))
        textwind = TextMobject("WIND")
        textwind.next_to(wind5, LEFT)
        self.play(Write(textwind))
        self.wait(1)

        #arus spiral ekman
        center = Line(np.array([0, 0, -2]), np.array([0, 0, 2]), color=RED,  buff=0)
        arrow1 = Arrow(np.array([0, 0, 2]), np.array([2, -2, 2]), color=RED, buff=0)
        arrow2 = Arrow(np.array([0, 0, 1.6]), np.array([1.6, -1.8, 1.6]), color=RED,buff=0)
        arrow3 = Arrow(np.array([0, 0, 1.2]), np.array([1.2, -1.6, 1.2]), color=RED, buff=0)
        arrow4 = Arrow(np.array([0, 0, 0.8]), np.array([0.8, -1.4, 0.8]), color=RED, buff=0)
        arrow5 = Arrow(np.array([0, 0, 0.4]), np.array([0.4, -1.2, 0.4]), color=RED,buff=0)
        arrow6 = Arrow(np.array([0, 0, 0]), np.array([0, -1, 0]), color=RED,buff=0)
        arrow7 = Arrow(np.array([0, 0, -0.4]), np.array([-0.8, -0.8, -0.4]),  color=RED, buff=0)
        arrow8 = Arrow(np.array([0, 0, -0.8]), np.array([-0.6, -0.6, -0.8]), color=RED, buff=0)
        arrow9 = Arrow(np.array([0, 0, -1.2]), np.array([-0.4, -0.4, -1.2]), color=RED, buff=0)
        arrow10 = Arrow(np.array([0, 0, -1.6]), np.array([-0.2, -0.2, -1.6]), color=RED, buff=0)
        arrow11 = Arrow(np.array([0, 0, -2]), np.array([-0.1, -0.1, -2]), color=RED, buff=0)

        self.play(GrowArrow(center))
        self.play(GrowArrow(arrow1))
        arrow = VGroup(arrow2, arrow3, arrow4 , arrow5 , arrow6 , arrow7, arrow8 , arrow9 , arrow10,arrow11)
        number = -30
        for i in arrow:
            self.play(ShowCreation(i))
            number = number - 10
            self.move_camera(phi=60 * DEGREES, theta=number * DEGREES, distance=20)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait()

        arrowekman = Arrow(np.array([0,-1.5 , 0]), np.array([0, -3, 0]), color=BLUE, buff=0)
        textekman= TextMobject("Ekman\\\\",
                                 "Transport", arg_separator="")
        textekman.next_to(arrowekman, LEFT)
        self.play(ShowCreation(VGroup(arrowekman,textekman)))
        self.wait()

        self.play(
            *[FadeOut(mob) for mob in self.mobjects])


class EkmanTransportSouthernHemisphere(ThreeDScene):
    def construct(self):

        judul = TextMobject("Transpor Ekman\\\\",
                                "di BBS", arg_separator="").scale(0.8).set_color_by_gradient(BLUE_B, TEAL)
        self.add_fixed_in_frame_mobjects(judul)  # <----- Add this
        judul.to_corner(UL)

        self.set_camera_orientation(phi=30 * DEGREES, theta=-90 * DEGREES)

        cube = Cube(side_length=5, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(GREEN_B)
        self.play(ShowCreation(cube))

        #wind flow
        #1
        arah1 = np.array([2, 0, 3])
        wind1 = Polygon(UP*0.5 + LEFT*0.5, ORIGIN, DOWN*0.5 + LEFT*0.5, RIGHT*0.5).scale(1)
        wind1.move_to(arah1)

        ##text north
        textnorth = TextMobject("Utara").scale(0.8)
        textnorth.next_to(wind1, RIGHT)

        #2
        arah2 = np.array([1, 0, 3])
        wind2 = wind1.copy()
        wind2.move_to(arah2)

        #3
        arah3 = np.array([0, 0, 3])
        wind3 = wind1.copy()
        wind3.move_to(arah3)

        #4
        arah4 = np.array([-1, 0, 3])
        wind4 = wind1.copy()
        wind4.move_to(arah4)

        #5
        arah5 = np.array([-2, 0, 3])
        wind5 = wind1.copy()
        wind5.move_to(arah5)

        wind = VGroup(wind1, wind2 , wind3 , wind4, wind5)
        self.play(Write(wind))
        self.play(Write(textnorth))

        #text wind
        textwind = TextMobject("WIND")
        textwind.next_to(wind5, LEFT)
        self.play(Write(textwind))

        #arus spiral ekman
        center = Line(np.array([0, 0, -2]), np.array([0, 0, 2]), color=RED, buff=0)
        arrow1 = Arrow(np.array([0, 0, 2]), np.array([2, 2, 2]), color=RED, buff=0)
        arrow2 = Arrow(np.array([0, 0, 1.6]), np.array([1.6, 1.8, 1.6]), color=RED, buff=0)
        arrow3 = Arrow(np.array([0, 0, 1.2]), np.array([1.2, 1.6, 1.2]), color=RED, buff=0)
        arrow4 = Arrow(np.array([0, 0, 0.8]), np.array([0.8, 1.4, 0.8]), color=RED, buff=0)
        arrow5 = Arrow(np.array([0, 0, 0.4]), np.array([0.4, 1.2, 0.4]), color=RED, buff=0)
        arrow6 = Arrow(np.array([0, 0, 0]), np.array([0, 1, 0]), color=RED, buff=0)
        arrow7 = Arrow(np.array([0, 0, -0.4]), np.array([-0.8, 0.8, -0.4]), color=RED, buff=0)
        arrow8 = Arrow(np.array([0, 0, -0.8]), np.array([-0.6, 0.6, -0.8]), color=RED, buff=0)
        arrow9 = Arrow(np.array([0, 0, -1.2]), np.array([-0.4, 0.4, -1.2]), color=RED, buff=0)
        arrow10 = Arrow(np.array([0, 0, -1.6]), np.array([-0.2, 0.2, -1.6]), color=RED, buff=0)
        arrow11 = Arrow(np.array([0, 0, -2]), np.array([-0.1, 0.1, -2]), color=RED, buff=0)

        self.play(GrowArrow(center))
        self.play(GrowArrow(arrow1))
        arrow = VGroup(arrow2, arrow3, arrow4 , arrow5 , arrow6 , arrow7, arrow8 , arrow9 , arrow10,arrow11)
        number = 30
        for i in arrow:
            self.play(ShowCreation(i))
            number = number + 10
            self.move_camera(phi=60 * DEGREES, theta=number * DEGREES, distance=15)

        self.begin_ambient_camera_rotation(rate=0.3)



        arrowekman = Arrow(np.array([0,1.5 , 0]), np.array([0, 3, 0]), color=BLUE, buff=0)
        textekman= TextMobject("Ekman\\\\",
                                 "Transport", arg_separator="").scale(0.8)
        textekman.next_to(arrowekman, LEFT)
        self.play(ShowCreation(VGroup(arrowekman,textekman)))
        self.wait(5)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects])


class ekman_momentum_equationX(Scene):
    def construct(self):
        
        textx=TextMobject("Persamaan Momentum Arah Sumbu-X").scale(1.5).set_color_by_gradient(BLUE_E, TEAL)
        textx.move_to(UP*3)
        self.play(ShowCreation(textx))
        #part1
        eqX1=TexMobject("\\frac{\partial u}{\partial t}+ u \\frac{\partial u}{\partial x}+v\\frac{\partial u}{\partial y}").scale(0.8).set_color(BLUE_B)
        eqX2=TexMobject("- 2v\\Omega sin \\theta ").scale(0.8).set_color(BLUE_B)
        eqX3=TexMobject("=").scale(0.8).set_color(BLUE_B)
        eqX4=TexMobject("-\\frac{1}{\\rho}\\frac{\partial p}{\partial x} ").scale(0.8).set_color(BLUE_B)
        eqX5=TexMobject("+\\frac{1}{\\rho}(\\frac{\partial \\tau_{xx}}{\partial x} +\\frac{\partial \\tau_{yx}}{\partial y})").scale(0.8).set_color(BLUE_B)
        eqX6=TexMobject("+\\frac{1}{\\rho}\\frac{\partial \\tau_{zx}}{\partial z}").scale(0.8).set_color(BLUE_B)

        eqX3.move_to(np.array([0,0,0]))
        eqX2.next_to(eqX3, LEFT)
        eqX1.next_to(eqX2, LEFT)
        eqX4.next_to(eqX3, RIGHT)
        eqX5.next_to(eqX4, RIGHT)
        eqX6.next_to(eqX5, RIGHT)
        self.play(Write(VGroup(eqX1,eqX2,eqX3,eqX4,eqX5,eqX6)))
        self.wait()

        #part2
        eq2X1=TexMobject("f = 2 \\Omega sin \\theta").scale(0.8).set_color(BLUE_B)
        eq2X2=TexMobject(" = 0").scale(0.8).set_color(BLUE_B)
        eq2X3=TexMobject("= 0").scale(0.8).set_color(BLUE_B)
        eq2X4=TexMobject("= 0").scale(0.8).set_color(BLUE_B)
        eq2X5=TexMobject("0").scale(0.8).set_color(BLUE_B)
        eq2X6=TexMobject("0").scale(0.8).set_color(BLUE_B)
        eq2X7=TexMobject("0").scale(0.8).set_color(BLUE_B)
        eq2X9=TexMobject("\\frac{1}{\\rho}\\frac{\partial \\tau_{zx}}{\partial z}").scale(0.8).set_color(BLUE_B)
        eq2X8=TexMobject(" - fv ").scale(0.8).set_color(BLUE_B)
        eq2X9.next_to(eqX3,RIGHT)
        eq2X1.add_background_rectangle(opacity=0.2, color=MAROON_A, buff=0.25)

        #change to 0
        framebox_eqX1 = SurroundingRectangle(eqX1, buff=.1).set_color(MAROON_D)
        framebox_eqX1.set_stroke(MAROON_D)
        framebox_eqX4 = SurroundingRectangle(eqX4, buff=.1).set_color(MAROON_D)
        framebox_eqX4.set_stroke(MAROON_D)
        framebox_eqX5 = SurroundingRectangle(eqX5, buff=.1).set_color(MAROON_D)
        framebox_eqX5.set_stroke(MAROON_D)
        eq2X1.next_to(eqX3, DOWN*4)
        eq2X2.next_to(framebox_eqX1, UP)
        eq2X3.next_to(framebox_eqX4, UP)
        eq2X4.next_to(framebox_eqX5, UP)
        eq2X5.move_to(eqX1)
        eq2X6.move_to(eqX4)
        eq2X7.move_to(eqX5)
        eq2X8.move_to(eqX2)
        self.play(ShowCreation(VGroup(framebox_eqX1,framebox_eqX4,framebox_eqX5)))
        self.wait(1)
        self.play(ShowCreation(VGroup(eq2X2,eq2X3,eq2X4)))
        self.play(ReplacementTransform(eq2X2.copy(),eq2X5), FadeOut(VGroup(eqX1,eq2X2)))
        self.play(ReplacementTransform(eq2X3.copy(),eq2X6), FadeOut(VGroup(eqX4,eq2X3)))
        self.play(ReplacementTransform(eq2X4.copy(),eq2X7), FadeOut(VGroup(eqX5,eq2X4)))
        self.play(FadeOut(VGroup(framebox_eqX1,framebox_eqX4,framebox_eqX5)))

        self.play(FadeOut(VGroup(eq2X5,eq2X6,eq2X7)))
        self.play(ReplacementTransform(eqX6.copy() , eq2X9), FadeOut(eqX6))

        #sisa eq2x9 , eqx3 , eqx2
        # change to fv
        framebox_eq2X1 = SurroundingRectangle(eq2X1, buff=.1).set_color(MAROON_D)
        framebox_eq2X1.set_stroke(MAROON_D)
        self.play(ShowCreation(VGroup(eq2X1, framebox_eq2X1)))
        self.wait(1)
        self.play(ReplacementTransform(eqX2.copy(), eq2X8), FadeOut(eqX2))
        self.wait(1)
        self.play(FadeOut(VGroup(eq2X1, framebox_eq2X1)))
        self.wait(1)

        # part3
        eq3X1 = TexMobject("\\frac{\partial \\tau_{zx}}{\partial z} = \mu \\frac{\partial^2 u}{\partial z^2}").scale(0.8).set_color(BLUE_B)
        eq3X2 = TexMobject("\\frac{\mu}{\\rho} ").scale(0.8).set_color(BLUE_B)
        eq3X3 = TexMobject("\\frac{\partial^2 u}{\partial z^2}").scale(0.8).set_color(BLUE_B)
        eq3X4 = TexMobject("\\upsilon").scale(0.8).set_color(BLUE_B)
        eq3X1.next_to(eq2X9, DOWN*4)
        eq3X2.next_to(eqX3, RIGHT)
        eq3X3.next_to(eq3X2, RIGHT)
        eq3X4.move_to(eq3X2)
        eq3X1.add_background_rectangle(opacity=0.2, color=MAROON_A, buff=0.25)

        # part4
        eq4X = TexMobject("- fv = \\nu \\frac{\partial^2 u}{\partial z^2} ")

        # change rigth handside
        framebox_eq3X1 = SurroundingRectangle(eq3X1, buff=.1).set_color(MAROON_D)
        framebox_eq3X1.set_stroke(MAROON_D)
        box1 = VGroup(framebox_eq3X1, eq3X1)
        self.play(ShowCreation(box1))
        self.wait()

        self.play(ReplacementTransform(eq2X9.copy() , eq3X2) ,
                  FadeOut(eq2X9),
                  ShowCreation(eq3X3)
                  )
        self.play(FadeOut(box1))
        self.wait()
        self.play(ReplacementTransform(eq3X2.copy() , eq3X4), FadeOut(eq3X2))
        self.play(
            textx.shift, DOWN*2,
            textx.scale, 0.8
        )

        self.wait()
        self.play(
            *[FadeOut(mob) for mob in self.mobjects])


class ekman_momentum_equationY(Scene):
    def construct(self):
        
        textY=TextMobject("Persamaan Momentum Arah Sumbu-Y").scale(1.5).set_color_by_gradient(BLUE_B, TEAL)
        textY.move_to(UP*3)
        self.play(ShowCreation(textY))
        #part1
        eqY1=TexMobject("\\frac{\partial v}{\partial t}+ u \\frac{\partial v}{\partial x}+v\\frac{\partial v}{\partial y}").scale(0.8).set_color(BLUE_B)
        eqY2=TexMobject("2u\\Omega sin \\theta ").scale(0.8).set_color(BLUE_B)
        eqY3=TexMobject("=").scale(0.8).set_color(BLUE_B)
        eqY4=TexMobject("-\\frac{1}{\\rho}\\frac{\partial p}{\partial y} ").scale(0.8).set_color(BLUE_B)
        eqY5=TexMobject("+\\frac{1}{\\rho}(\\frac{\partial \\tau_{xy}}{\partial x} +\\frac{\partial \\tau_{yy}}{\partial y})").scale(0.8).set_color(BLUE_B)
        eqY6=TexMobject("+\\frac{1}{\\rho}\\frac{\partial \\tau_{zy}}{\partial z}").scale(0.8).set_color(BLUE_B)
        eqY3.move_to(np.array([0,0,0]))
        eqY2.next_to(eqY3, LEFT)
        eqY1.next_to(eqY2, LEFT)
        eqY4.next_to(eqY3, RIGHT)
        eqY5.next_to(eqY4, RIGHT)
        eqY6.next_to(eqY5, RIGHT)
        self.play(Write(VGroup(eqY1,eqY2,eqY3,eqY4,eqY5,eqY6)))

        #part2
        eq2Y1=TexMobject("f = 2 \\Omega sin \\theta").scale(0.8).set_color(BLUE_B)
        eq2Y2=TexMobject(" = 0").scale(0.8).set_color(BLUE_B)
        eq2Y3=TexMobject("= 0").scale(0.8).set_color(BLUE_B)
        eq2Y4=TexMobject("= 0").scale(0.8).set_color(BLUE_B)
        eq2Y5=TexMobject("0").scale(0.8).set_color(BLUE_B)
        eq2Y6=TexMobject("0").scale(0.8).set_color(BLUE_B)
        eq2Y7=TexMobject("0").scale(0.8).set_color(BLUE_B)
        eq2Y9=TexMobject("\\frac{1}{\\rho}\\frac{\partial \\tau_{zy}}{\partial z}").scale(0.8).set_color(BLUE_B)
        eq2Y8=TexMobject(" fu ").scale(0.8).set_color(BLUE_B)
        eq2Y9.next_to(eqY3,RIGHT)
        eq2Y1.add_background_rectangle(opacity=0.2, color=MAROON_A, buff=0.25)

        #change to 0
        framebox_eqY1 = SurroundingRectangle(eqY1, buff=.1).set_color(MAROON_D)
        framebox_eqY1.set_stroke(MAROON_D)
        framebox_eqY4 = SurroundingRectangle(eqY4, buff=.1).set_color(MAROON_D)
        framebox_eqY4.set_stroke(MAROON_D)
        framebox_eqY5 = SurroundingRectangle(eqY5, buff=.1).set_color(MAROON_D)
        framebox_eqY5.set_stroke(MAROON_D)
        eq2Y1.next_to(eqY3, DOWN*4)
        eq2Y2.next_to(framebox_eqY1, UP)
        eq2Y3.next_to(framebox_eqY4, UP)
        eq2Y4.next_to(framebox_eqY5, UP)
        eq2Y5.move_to(eqY1)
        eq2Y6.move_to(eqY4)
        eq2Y7.move_to(eqY5)
        eq2Y8.move_to(eqY2)
        self.play(ShowCreation(VGroup(framebox_eqY1,framebox_eqY4,framebox_eqY5)))
        self.play(ShowCreation(VGroup(eq2Y2,eq2Y3,eq2Y4)))
        self.play(ReplacementTransform(eq2Y2.copy(),eq2Y5), FadeOut(VGroup(eqY1,eq2Y2)))
        self.play(ReplacementTransform(eq2Y3.copy(),eq2Y6), FadeOut(VGroup(eqY4,eq2Y3)))
        self.play(ReplacementTransform(eq2Y4.copy(),eq2Y7), FadeOut(VGroup(eqY5,eq2Y4)))
        self.wait(1)
        self.play(FadeOut(VGroup(framebox_eqY1,framebox_eqY4,framebox_eqY5)))

        self.play(FadeOut(VGroup(eq2Y5,eq2Y6,eq2Y7)))
        self.play(ReplacementTransform(eqY6.copy() , eq2Y9), FadeOut(eqY6))

        #sisa eq2x9 , eqx3 , eqx2
        # change to fv
        framebox_eq2Y1 = SurroundingRectangle(eq2Y1, buff=.1).set_color(MAROON_D)
        framebox_eq2Y1.set_stroke(MAROON_D)
        self.play(ShowCreation(VGroup(eq2Y1, framebox_eq2Y1)))
        self.wait(1)
        self.play(ReplacementTransform(eqY2.copy(), eq2Y8), FadeOut(eqY2))
        self.wait(1)
        self.play(FadeOut(VGroup(eq2Y1, framebox_eq2Y1)))

        # part3
        eq3Y1 = TexMobject("\\frac{\partial \\tau_{zy}}{\partial z} = \mu \\frac{\partial^2 v}{\partial z^2}").scale(0.8).set_color(BLUE_B)
        eq3Y2 = TexMobject("\\frac{\mu}{\\rho} ").scale(0.8).set_color(BLUE_B)
        eq3Y3 = TexMobject("\\frac{\partial^2 v}{\partial z^2}").scale(0.8).set_color(BLUE_B)
        eq3Y4 = TexMobject("\\upsilon").scale(0.8).set_color(BLUE_B)
        eq3Y1.next_to(eq2Y9, DOWN*4)
        eq3Y2.next_to(eqY3, RIGHT)
        eq3Y3.next_to(eq3Y2, RIGHT)
        eq3Y4.move_to(eq3Y2)
        eq3Y1.add_background_rectangle(opacity=0.2, color=MAROON_A, buff=0.25)


        # change rigth handside
        framebox_eq3Y1 = SurroundingRectangle(eq3Y1, buff=.1).set_color(MAROON_D)
        framebox_eq3Y1.set_stroke(MAROON_D)
        box1 = VGroup(framebox_eq3Y1, eq3Y1)
        self.play(ShowCreation(box1))

        self.play(ReplacementTransform(eq2Y9.copy() , eq3Y2) ,
                  FadeOut(eq2Y9),
                  ShowCreation(eq3Y3)
                  )
        self.play(FadeOut(box1))
        self.play(ReplacementTransform(eq3Y2.copy() , eq3Y4), FadeOut(eq3Y2))
        self.play(
            textY.shift, DOWN * 2,
            textY.scale, 0.8
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects])

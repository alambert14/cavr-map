import math

class Abstract2D(object):
        def __init__(self, x, y, lx, ly, rot, depth):
                self.x = x
                self.y = y
                self.lx = lx
                self.ly = ly
                self.rot = math.radians(rot)
		self.depth = depth

		# Derived Values
		self.dx = lx/2
		self.dy = ly/2

	@property
	def dx(self):
		return self._dx
	
	@dx.setter
	def dx(self, dx):
		self._dx = dx
		self._lx = 2*dx
	@property
	def dy(self):
		return self._dy
	
	@dy.setter
	def dy(self, dy):
		self._dy = dy
		self._ly = 2*dy

	@property
	def lx(self):
		return self._lx

	@lx.setter
	def lx(self, lx):
		self._lx = lx
		self._dx = lx/2

	@property
	def ly(self):
		return self._ly


	@ly.setter
	def ly(self, ly):
		self._ly = ly
		self._dy = ly/2



class Abstract3D(object):
	def __init__(self, x, y, z, lx, ly, lz, rot, depth):
		self.x = x
		self.y = y
		self.z = z
		self.lx = lx
		self.ly = ly
		self.lz = lz
		self.rot = rot
		self.depth = depth

		# TODO: Add the dx vs. lx difference as in the Abstract2D

class Rectangle(Abstract2D):
        def __init__(self, x, y, lx, ly, rot, depth):
                Abstract2D.__init__(self, x, y, lx, ly, rot, depth)
class Ellipse(Abstract2D):
	def __init__(self, x, y, lx, ly, rot, depth):
		Abstract2D.__init__(self, x, y, lx, ly, rot, depth)
class Square(Rectangle):
        def __init__(self, x, y, l, rot, depth):
                Rectangle.__init__(self, x, y, l, l, rot, depth)
class Circle(Ellipse):
	def __init__(self, x, y, l, rot, depth):
		Ellipse.__init__(self, x, y, l, l, rot)
class Rectangle3D(Abstract3D):
	def __init__(self, x, y, z, lx, ly, lz, rot, depth):
		Abstract3D.__init__(self, x, y, z, lx, ly, lz, rot, depth)
class Ellipse3D(Abstract3D):
	def __init__(self, x, y, z, lx, ly, lz, rot, depth):
		Abstract3D.__init__(self, x, y, x, lx, ly, lz, rot, depth)
class Square3D(Rectangle3D):
	def __init__(self, x, y, z, l, rot, depth):
		Rectangle3D.__init__(self, x, y, z, l, l, l, rot, depth)
class Circle3D(Ellipse3D):
	def __init__(self, x, y, z, l, rot, depth):
		Ellipse3D.__init__(self, x, y, z, l, l, l, rot, depth)


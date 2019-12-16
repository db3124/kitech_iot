package Inheritance;

public class PointTest {
	public static void main(String[] args) {
		Point3D p3 = new Point3D();
		System.out.println(p3.x);
		System.out.println(p3.y);
		System.out.println(p3.z);
		System.out.println(p3);
	}
}

class Point{
	int x;
	int y;
	
	Point(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	String getLocation() {
		return "x : "+x+"y : "+y;
	}
}

class Point3D extends Point{
	int z;

	Point3D(){
		this(70, 40, 60);
	}
	
	Point3D(int x, int y, int z) {
		super(x, y);
		this.z = z;
	}
	
	String getLocation() {
		return super.getLocation()+", z : "+z;
	}
}
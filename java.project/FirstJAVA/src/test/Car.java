package test;

public class Car {// public은 대표 클래스 하나에만 들어감
	int gasolineGauge;
	
	public Car(int gasolineGauge) {
//		super();// Object()
		this.gasolineGauge = gasolineGauge;
	}

}

class HybridCar extends Car{
	int electronicGauge;

	public HybridCar(int gasolineGauge) {
		super(gasolineGauge);
	}

	public HybridCar(int gasolineGauge, int electronicGauge) {
		super(gasolineGauge);
		this.electronicGauge = electronicGauge;
	}

}

class HybridWaterCar extends HybridCar{
	int waterGauge;
	
	public HybridWaterCar(int gasolineGauge, int electronicGauge, int waterGauge) {
		super(gasolineGauge, electronicGauge);
		this.waterGauge = waterGauge;
	}

	public void showCurrentGauge() {
		System.out.println("잔여 가솔린 : "+gasolineGauge);
		System.out.println("잔여 가솔린 : "+electronicGauge);
		System.out.println("잔여 가솔린 : "+waterGauge);
	}
	
}

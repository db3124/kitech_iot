package Inheritance;

public class Car {
	int gasolineGauge;
	
	public Car(int gasolineGauge) {
		super();
		this.gasolineGauge = gasolineGauge;
	}

	public static void main(String[] args) {
		HybridWaterCar hwc = new HybridWaterCar(100, 90, 20);
		hwc.showCurrentGauge();
	}

}

class HybridCar extends Car{
	int electronicGauge;

	public HybridCar(int gasolineGauge, int electronicGauge) {
		super(gasolineGauge);
		this.electronicGauge = electronicGauge;
	}	
}

class HybridWaterCar extends HybridCar{
	int waterGauge;
	
	HybridWaterCar(int gasolineGauge, int electronicGauge, int waterGauge) {
		super(gasolineGauge, electronicGauge);
		this.waterGauge = waterGauge;
	}
	
	public void showCurrentGauge() {
		System.out.println("잔여 가솔린 : "+gasolineGauge);
		System.out.println("잔여 가솔린 : "+electronicGauge);
		System.out.println("잔여 가솔린 : "+waterGauge);
	}
}
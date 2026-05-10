package frc.robot.simulation;

import edu.wpi.first.networktables.BooleanSubscriber;
import edu.wpi.first.networktables.NetworkTableInstance;
import edu.wpi.first.wpilibj.Notifier;
import edu.wpi.first.wpilibj.simulation.DriverStationSim;
import edu.wpi.first.wpilibj.smartdashboard.SmartDashboard;

public class SimDriverStationProxy {

    private final BooleanSubscriber enabledSub;
    private final BooleanSubscriber autonomousSub;
    private final Notifier notifier;

    public SimDriverStationProxy() {
        NetworkTableInstance nt = NetworkTableInstance.getDefault();
        enabledSub = nt.getBooleanTopic("/sim/ds/enabled").subscribe(false);
        autonomousSub = nt.getBooleanTopic("/sim/ds/autonomous").subscribe(false);

        DriverStationSim.setDsAttached(true);
        DriverStationSim.notifyNewData();

        notifier = new Notifier(this::update);
        notifier.startPeriodic(0.02);
    }

    private void update() {
        DriverStationSim.setEnabled(enabledSub.get());
        DriverStationSim.setAutonomous(autonomousSub.get());
        DriverStationSim.notifyNewData();
    }

    public void close() {
        notifier.close();
        enabledSub.close();
        autonomousSub.close();
    }
}
## Prometheus exporter for collect data from imu sensors

___

### Used links:
 - https://github.com/niru-5/imusensor
 - https://makersportal.com/blog/calibration-of-an-inertial-measurement-unit-imu-with-raspberry-pi-part-ii
 - https://ashish.one/blogs/write-custom-exporters-prometheus/


___

### Setup

```
sudo -H pip install -r requirements.txt
sudo cp sensors_collect.py /usr/local/bin/sensors_exporter.py
sudo cp sensors-exporter.sevice /lib/systemd/system/sensors-exporter.service
```

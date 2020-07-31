# vrops-splunk
A simple webhook shim for sending vR Ops alerts to Splunk via HEC

This is a simple script for receiving vRealize Operations webhook originating from alerts and forwarding them as
logs to Splunk. It uses the HTTP Event Collector (HEC) feature of Splunk.

## Installing

```
git clone https://github.com/prydin/vrops-splunk.git
cd vrops-splunk
pip install -r requirements.txt
```

Note: On Mac, you may have to replace ```pip``` with ```pip3```

## Usage
Start the server using the following commands:

```
export HEC_URL=https:<your instance>/services/collector
export HEC_TOKEN=<your security token>
flask run
```

By default, all attributes of the alert are sent as key-value pairs. If you want to change the format, you may
set the ```HEC_FORMAT``` environment variable. It accepts a Python format string that maps to the attributes
of the alert. For example:

```
export HEC_FORMAT="Alert: {alertName}, Criticality: {criticality}, Resource: {resourceName}"
```

If you want a different date format than the default one, you may set the ```HEC_DATE_FORMAT``` environment variable
to a valid Python date formatting string.
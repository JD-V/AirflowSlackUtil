# AirflowSlackUtil
This is a utility of airflow slack operator. It can be used to post messsages on slack in formatted manner. depending on success or failure of the task.

Steps to use.

1. Place the utils folder in your dags folder.

2. import slack operator in your dag like this

```from utils import slack```

3. create slack object

```slack = slack.Slack()```

4. Add success or failure callback in at dag level like this.

```
DEFAULT_DAG_ARGS = {
    'owner': 'JD',
    'on_failure_callback': slack.task_fail_slack_alert,
    'on_success_callback': slack.task_success_slack_alert
}
```

You can also use this slack operator at task level the same way.

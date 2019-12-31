from airflow.hooks.base_hook import BaseHook
from airflow.contrib.operators.slack_webhook_operator import SlackWebhookOperator

class Slack():
    """Slack events success and failure."""

    def __init__(self):
        """Initializes the slack connection ID"""
        self.SLACK_CONN_ID = 'slack'

    def task_fail_slack_alert(self, context):
        slack_webhook_token = BaseHook.get_connection(self.SLACK_CONN_ID).password
        slack_msg = """
                :red_circle: Task Failed.
                *Task*: {task}
                *Dag*: {dag}
                *Input*: {input}
                *Environemnt*: {env}
                *Execution Time*: {exec_date}
                *Log Url*: {log_url}
                """.format(
                task=context.get('task_instance').task_id,
                dag=context.get('task_instance').dag_id,
                ti=context.get('task_instance'),
                exec_date=context.get('execution_date'),
                log_url=context.get('task_instance').log_url,
                input= "As specified in dag" if context.get('dag_run').conf is None or context.get('dag_run').conf.get('file') is None else context.get('dag_run').conf.get('file'),
                env= "prod" if context.get('dag_run').conf is None or context.get('dag_run').conf.get('env') is None else context.get('dag_run').conf.get('env')
            )
        failed_alert = SlackWebhookOperator(
            task_id='slack_test',
            http_conn_id='slack',
            webhook_token=slack_webhook_token,
            message=slack_msg,
            username='airflow')
        return failed_alert.execute(context=context)

    def task_success_slack_alert(self, context):
        slack_webhook_token = BaseHook.get_connection(self.SLACK_CONN_ID).password
        slack_msg = """
                :large_blue_circle: Success.
                *Task*: {task}
                *Dag*: {dag}
                *Input*: {input}
                *Environemnt*: {env}
                *Execution Time*: {exec_date}
                *Message*: All the tasks of this dag has been passed.
                """.format(
                task=context.get('task_instance').task_id,
                dag=context.get('task_instance').dag_id,
                ti=context.get('task_instance'),
                exec_date=context.get('execution_date'),
                input= "As specified in dag" if context.get('dag_run').conf is None or context.get('dag_run').conf.get('file') is None else context.get('dag_run').conf.get('file'),
                env= "prod" if context.get('dag_run').conf is None or context.get('dag_run').conf.get('env') is None else context.get('dag_run').conf.get('env')
            )
        success_alert = SlackWebhookOperator(
            task_id='slack_test',
            http_conn_id='slack',
            webhook_token=slack_webhook_token,
            message=slack_msg,
            username='airflow')
        return success_alert.execute(context=context)

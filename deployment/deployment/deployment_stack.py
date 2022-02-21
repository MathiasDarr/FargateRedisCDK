from aws_cdk import (
    aws_autoscaling as autoscaling,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecr as ecr,
    aws_iam as iam,
    aws_elasticloadbalancingv2 as elbv2,
    App, CfnOutput, Stack
)


class LoadBalancerStack(Stack):
    def __init__(self, app: App, construct_id: str, **kwargs) -> None:
        super().__init__(app, construct_id, **kwargs)

        vpc = ec2.Vpc.from_lookup(self,
                                  "VPC",
                                  is_default=True)

        repository = ecr.Repository(
            self,
            "DakobedRepository"
        )

        cluster = ecs.Cluster(
            self,
            id="dakobed-cluster",
            vpc=vpc,
            cluster_name="dakobed-cluster"
        )

        execution_task_role_policy = iam.ManagedPolicy.from_managed_policy_arn(self,id="dakobed_execution_role_policy",managed_policy_arn='arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy')
        managed_s3_policy = iam.ManagedPolicy.from_managed_policy_arn(self, id='managed_s3_policy', managed_policy_arn='arn:aws:iam::aws:policy/AmazonS3FullAccess')
        task_role = iam.Role(
            self,
            "ecs_task_role",
            role_name="ecs_task_role",
            assumed_by=iam.ServicePrincipal('ecs-tasks.amazonaws.com'),
            managed_policies=[execution_task_role_policy, managed_s3_policy]
        )

        execution_role = iam.Role.from_role_arn(self,
                                                id="dakobed_execution_role",
                                                role_arn="arn:aws:iam::710339184759:role/ecsTaskExecutionRole")

        dakobed_task_definition = ecs.FargateTaskDefinition(
            self,
            id='dakobed-cdk-task',
            cpu=512,
            memory_limit_mib=1024,
            task_role=task_role,
            execution_role=execution_role
        )


        # data = open("./httpd.sh", "rb").read()
        # httpd=ec2.UserData.for_linux()
        # httpd.add_commands(str(data,'utf-8'))
        #
        #
        # asg = autoscaling.AutoScalingGroup(
        #     self,
        #     "ASG",
        #     vpc=vpc,
        #     instance_type=ec2.InstanceType.of(
        #         ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
        #     ),
        #     machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
        #     user_data=httpd,
        # )
        #
        lb = elbv2.ApplicationLoadBalancer(
            self,
            "DakobedLB",
            vpc=vpc,
            internet_facing=True)
        #
        # listener = lb.add_listener("Listener", port=80)
        # listener.add_targets("Target", port=80, targets=[asg])
        # listener.connections.allow_default_port_from_any_ipv4("Open to the world")
        #
        # asg.scale_on_request_count("AModestLoad", target_requests_per_minute=60)
        # CfnOutput(self,"LoadBalancer",export_name="LoadBalancer",value=lb.load_balancer_dns_name)

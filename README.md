This project shows how to do simple continous delivery using Gitlab pipelines, docker and AWS services.

Please see [attached presentation](https://github.com/drootnar/gitlab-cd-docker-aws-eb-example/blob/master/presentation.pdf) to see overall concept.

Configuration
------------
1. Set up Gitlab:
1.1 set environements: ```AWS_ACCESS_KEY_ID```, ```AWS_SECRET_ACCESS_KEY```
1.2 run Gitlab runner
2. Set up AWS (Elastic Beanstalk app, ECR repository)
3. Replace gaps in ```*.sample files``` with values and save it removing .sample postfix (config.yml.sample, Dockerrun.aws.json.template.sample, build_and_push_images.sh.sample)
4. Create Gitlab repo and connect it with the code: ```git remote add gitlab <gitlab_repo>```
5. When you ```git push gitlab master``` the pipeline will run and deploy to AWS Elastic Beanstalk

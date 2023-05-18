1. New project for example with `sam init`
2. Copy template to current project ROOT
4. Fix template
   - Description
   - Function name
   - Code Uri
   - Handler (use e.g. poller.handle.handler)
5. Remove outputs
6. Add handler, e.g. (def handler(_event, _context):)
7. Create requirements.txt (poetry export --without-hashes --format=requirements.txt > requirements.txt)
8. sam build
9. Check .aws-sam folder
10. sam deploy --guided
11. Check AWS Console, find Stack
12. Find function, try to run
13. Add environment variable (to AWS, we handle with ssm in the future)
14. Add AWS permissions
15. WORKS
16. Add encrypted ssm paramater
17. Add parameter fetch logic if ENV is not available
18. Remove env variable
19. Test
20. Add SSMParameterReadPolicy
21. WORKS
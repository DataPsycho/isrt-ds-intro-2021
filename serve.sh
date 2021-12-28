mlflow ui
mlflow models serve -m mlruns/0/9ec882099d7f41a7b394b988b177d018/artifacts/model_svm
curl http://127.0.0.1:5000/invocations -H 'Content-Type: application/json' -d '{"data":[[1,1,1,1,0,1,1,1,0,1,1,1,0,0]]}'
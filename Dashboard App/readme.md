gcloud builds submit --tag gcr.io/uk-train-dashboard-425908/project-uk-railways-00002-jph  --project=key-sign-425907-v3



gcloud run deploy --image gcr.io/uk-train-dashboard-425908/project-uk-railways-00002-jph --platform managed  --project=key-sign-425907-v3 --allow-unauthenticated
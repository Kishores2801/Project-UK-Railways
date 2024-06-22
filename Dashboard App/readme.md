gcloud builds submit --tag gcr.io/uk-train-dashboard-425908/project-uk-railways-00001-l2d--project=uk-train-dashboard-425908



gcloud run deploy --image gcr.io/uk-train-dashboard-425908/project-uk-railways-00001-l2d --platform managed  --project=uk-train-dashboard-425908 --allow-unauthenticated
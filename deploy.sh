#!/bin/bash

GCP_PROJECT='visual-essays'

GCR_SERVICE=${1:-ezsitepdf}
MIN_INSTANCE_LIMIT=0

gcloud builds submit --tag gcr.io/${GCP_PROJECT}/${GCR_SERVICE}
gcloud run deploy ${GCR_SERVICE} --image gcr.io/${GCP_PROJECT}/${GCR_SERVICE} --platform managed --region us-central1 --allow-unauthenticated

curl -X POST -H "Content-Type: application/json" \
 -d @test.json \
 http://0.0.0.0:5000/get_best_routes >  results.json

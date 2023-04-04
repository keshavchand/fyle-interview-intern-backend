def test_server_up(client, h_student_1):
    response = client.get(
        '/'
    )

    assert response.status_code == 200

    data = response.json
    assert data['status'] == 'ready'

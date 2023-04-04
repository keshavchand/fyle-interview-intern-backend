def test_post_assignment_and_grade(client, h_student_1, h_teacher_1):
    content = 'ABCD TESTPOST'

    # DRAFT
    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'content': content,
        })

    assert response.status_code == 200

    data = response.json['data']
    assert data['content'] == content
    assert data['state'] == 'DRAFT'
    assert data['teacher_id'] is None

    # SUBMIT
    response = client.post(
        '/student/assignments/submit',
        headers=h_student_1,
        json={
            'id': data['id'],
            'teacher_id': 1
        })

    assert response.status_code == 200

    data = response.json['data']
    assert data['student_id'] == 1
    assert data['state'] == 'SUBMITTED'
    assert data['teacher_id'] == 1

    # GRADE
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1,
        json={
            "id": data['id'],
            "grade": "A"
        }
    )

    assert response.status_code == 200

    data = response.json['data']
    assert data['student_id'] == 1
    assert data['state'] == 'GRADED'
    assert data['teacher_id'] == 1

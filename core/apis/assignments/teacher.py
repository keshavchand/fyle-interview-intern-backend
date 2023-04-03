from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment

from .schema import AssignmentSchema, AssignmentSubmitSchema, AssignmentGradeSchema 

teacher_assignments_resources = Blueprint('teacher_assignments_resources', __name__)

@teacher_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.auth_principal
def list_assignments(p):
    """Returns list of assignments"""

    teachers_assignments = Assignment.get_assignments_to_teacher(p.teacher_id)
    teachers_assignments_dump = AssignmentSchema().dump(teachers_assignments, many=True)
    return APIResponse.respond(data=teachers_assignments_dump)

@teacher_assignments_resources.route('assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.auth_principal
def grade_assignments(p, data):
    """grade an assignments"""

    import pdb
    pdb.set_trace()

    grade_schema_load = AssignmentGradeSchema().load(data)
    graded_assignment = Assignment.set_grade(
            _id = grade_schema_load.id,
            grade = grade_schema_load.grade,
            principal = p
        )

    db.session.commit()
    teacher_graded_assignment = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=teacher_graded_assignment)

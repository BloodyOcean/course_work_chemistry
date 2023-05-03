from models.models import Comment 
from deformation import deformate_string


class CommentDeformationInterface:
    def spoil(self, comment:Comment) -> Comment:
        raise NotImplementedError()

class CommentDeformation(CommentDeformationInterface):
    def __init__(self, probability:float) -> None:
        self.probability = probability

    def spoil(self, comment: Comment) -> Comment:
        comment.comment_text = deformate_string(comment.comment_text, self.probability)
        return comment
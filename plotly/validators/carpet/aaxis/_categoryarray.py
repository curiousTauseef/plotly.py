import _plotly_utils.basevalidators


class CategoryarrayValidator(_plotly_utils.basevalidators.DataArrayValidator):

    def __init__(
        self,
        plotly_name='categoryarray',
        parent_name='carpet.aaxis',
        **kwargs
    ):
        super(CategoryarrayValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='data',
            **kwargs
        )
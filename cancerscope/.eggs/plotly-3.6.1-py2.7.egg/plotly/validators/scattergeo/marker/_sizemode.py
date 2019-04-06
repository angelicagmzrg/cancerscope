import _plotly_utils.basevalidators


class SizemodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self,
        plotly_name='sizemode',
        parent_name='scattergeo.marker',
        **kwargs
    ):
        super(SizemodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            role=kwargs.pop('role', 'info'),
            values=kwargs.pop('values', ['diameter', 'area']),
            **kwargs
        )

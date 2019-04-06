import _plotly_utils.basevalidators


class BordercolorValidator(_plotly_utils.basevalidators.ColorValidator):

    def __init__(
        self, plotly_name='bordercolor', parent_name='layout.slider', **kwargs
    ):
        super(BordercolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'arraydraw'),
            role=kwargs.pop('role', 'style'),
            **kwargs
        )

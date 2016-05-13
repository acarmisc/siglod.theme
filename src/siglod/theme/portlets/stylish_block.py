from zope.interface import implementer

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from plone.app.textfield import RichText

from zope import schema
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFPlone import PloneMessageFactory as _

from plone.app.portlets.browser.z3cformhelper import AddForm as base_AddForm
from plone.app.portlets.browser.z3cformhelper import EditForm as base_EditForm
from z3c.form import field


class IStylishPortlet(IPortletDataProvider):
    """ A portlet which can render the lIStylishPortlet. """

    headline = schema.TextLine(title=_(u'Headline'), description=_(u''), required=True)
    css_classes = schema.TextLine(title=_(u'CSS Classes'), description=_(u''), required=True)
    body_text = RichText(
                    title=u"Body text",
                    default_mime_type='text/html',
                    output_mime_type='text/html',
                    allowed_mime_types=('text/html', 'text/plain',),
                    default=u""
                )


@implementer(IStylishPortlet)
class Assignment(base.Assignment):

    def __init__(self, headline=u'testamelo', css_classes=u'', body_text=None):
        self.headline = headline
        self.css_classes = css_classes
        self.body_text = body_text

    title = _(u'label_logged_in', default=u'IStylishPortlet')


class Renderer(base.Renderer):

    def getHeadline(self):
        return self.data.headline

    def getCssClasses(self):
        return self.data.css_classes

    def getBodyText(self):
        return self.data.body_text.output

    render = ViewPageTemplateFile('templates/stylish_block.pt')


class AddForm(base_AddForm):
    fields = field.Fields(IStylishPortlet)

    label = _(u"title_add_static_portlet", default=u"Add static text portlet")
    description = _(
        u"description_static_portlet",
        default=u"A portlet which can display static HTML text."
    )

    def create(self, data):
        return Assignment(**data)


class EditForm(base_EditForm):
    fields = field.Fields(IStylishPortlet)

    label = _(
        u"title_edit_static_portlet",
        default=u"Edit static text portlet"
    )
    description = _(
        u"description_static_portlet",
        default=u"A portlet which can display static HTML text."
    )

from zope.interface import implements
from zope.component import getMultiAdapter

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from zope.formlib import form
from zope import schema
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from Products.CMFPlone import PloneMessageFactory as _


class IStylishPortlet(IPortletDataProvider):
    """A portlet which can render the lIStylishPortlet.
    """

    headline = schema.TextLine(title=_(u'Headline'), description=_(u''), required=True)


class Assignment(base.Assignment):
    implements(IStylishPortlet)

    def __init__(self, headline=u'testamelo'):
        self.headline = headline

    title = _(u'label_logged_in', default=u'IStylishPortlet')


class AddForm(base.AddForm):
    form_fields = form.Fields(IStylishPortlet)
    label = _(u"Aggiungi Portlet IStylishPortlet")
    description = _(u"")

    def create(self, data):
        assignment = Assignment()
        form.applyChanges(assignment, self.form_fields, data)
        return assignment


class EditForm(base.EditForm):
    form_fields = form.Fields(IStylishPortlet)

    label = _(u"Edit IStylishPortlet in Portlet")
    description = _(u"This portlet displays IStylishPortlet")


class Renderer(base.Renderer):

    def getHeadline(self):
        return self.data.headline

    render = ViewPageTemplateFile('templates/stylish_block.pt')

import FWCore.ParameterSet.Config as cms

from .EventContentAnalyzer import EventContentAnalyzer

printContent = EventContentAnalyzer(
  indentation = '++',
  verbose = False,
  verboseIndentation = '  ',
  verboseForModuleLabels = [],
  getData = False,
  getDataForModuleLabels = [],
  listContent = True,
  listProvenance = False,
  listPathStatus = False
)

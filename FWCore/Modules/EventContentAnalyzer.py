import FWCore.ParameterSet.Config as cms

def EventContentAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EventContentAnalyzer',
    indentation = cms.untracked.string('++'),
    verbose = cms.untracked.bool(False),
    verboseIndentation = cms.untracked.string('  '),
    verboseForModuleLabels = cms.untracked.vstring(),
    getData = cms.untracked.bool(False),
    getDataForModuleLabels = cms.untracked.vstring(),
    listContent = cms.untracked.bool(True),
    listProvenance = cms.untracked.bool(False),
    listPathStatus = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

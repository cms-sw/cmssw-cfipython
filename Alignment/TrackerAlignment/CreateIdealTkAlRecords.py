import FWCore.ParameterSet.Config as cms

def CreateIdealTkAlRecords(**kwargs):
  mod = cms.EDAnalyzer('CreateIdealTkAlRecords',
    alignToGlobalTag = cms.untracked.bool(False),
    skipSubDetectors = cms.untracked.vstring(),
    createReferenceRcd = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

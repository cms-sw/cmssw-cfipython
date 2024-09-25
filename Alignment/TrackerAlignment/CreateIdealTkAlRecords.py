import FWCore.ParameterSet.Config as cms

def CreateIdealTkAlRecords(*args, **kwargs):
  mod = cms.EDAnalyzer('CreateIdealTkAlRecords',
    alignToGlobalTag = cms.untracked.bool(False),
    skipSubDetectors = cms.untracked.vstring(),
    createReferenceRcd = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

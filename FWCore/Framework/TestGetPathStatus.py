import FWCore.ParameterSet.Config as cms

def TestGetPathStatus(*args, **kwargs):
  mod = cms.EDAnalyzer('TestGetPathStatus',
    expectedStates = cms.required.vint32,
    expectedIndexes = cms.required.vuint32,
    pathStatusTag = cms.required.InputTag,
    endPathStatusTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

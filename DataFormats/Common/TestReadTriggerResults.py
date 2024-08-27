import FWCore.ParameterSet.Config as cms

def TestReadTriggerResults(**kwargs):
  mod = cms.EDAnalyzer('TestReadTriggerResults',
    expectedParameterSetID = cms.required.string,
    expectedNames = cms.required.vstring,
    expectedHLTStates = cms.required.vuint32,
    expectedModuleIndexes = cms.required.vuint32,
    triggerResultsTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

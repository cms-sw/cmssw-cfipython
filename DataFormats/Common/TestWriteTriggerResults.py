import FWCore.ParameterSet.Config as cms

def TestWriteTriggerResults(**kwargs):
  mod = cms.EDProducer('TestWriteTriggerResults',
    parameterSetID = cms.required.string,
    names = cms.required.vstring,
    hltStates = cms.required.vuint32,
    moduleIndexes = cms.required.vuint32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

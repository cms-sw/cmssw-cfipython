import FWCore.ParameterSet.Config as cms

def TestWriteTriggerResults(*args, **kwargs):
  mod = cms.EDProducer('TestWriteTriggerResults',
    parameterSetID = cms.required.string,
    names = cms.required.vstring,
    hltStates = cms.required.vuint32,
    moduleIndexes = cms.required.vuint32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

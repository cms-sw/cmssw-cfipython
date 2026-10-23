import FWCore.ParameterSet.Config as cms

def ThingWithMergeProducer(*args, **kwargs):
  mod = cms.EDProducer('ThingWithMergeProducer',
    changeIsEqualValue = cms.untracked.bool(False),
    labelsToGet = cms.untracked.vstring(),
    noPut = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

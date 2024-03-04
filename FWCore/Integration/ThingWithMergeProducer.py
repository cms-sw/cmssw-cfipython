import FWCore.ParameterSet.Config as cms

def ThingWithMergeProducer(**kwargs):
  mod = cms.EDProducer('ThingWithMergeProducer',
    changeIsEqualValue = cms.untracked.bool(False),
    labelsToGet = cms.untracked.vstring(),
    noPut = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

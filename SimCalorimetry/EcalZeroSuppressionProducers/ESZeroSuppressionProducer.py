import FWCore.ParameterSet.Config as cms

def ESZeroSuppressionProducer(**kwargs):
  mod = cms.EDProducer('ESZeroSuppressionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

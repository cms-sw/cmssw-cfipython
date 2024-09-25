import FWCore.ParameterSet.Config as cms

def ESZeroSuppressionProducer(*args, **kwargs):
  mod = cms.EDProducer('ESZeroSuppressionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

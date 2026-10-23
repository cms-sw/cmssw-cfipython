import FWCore.ParameterSet.Config as cms

def Multi5x5SuperClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('Multi5x5SuperClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

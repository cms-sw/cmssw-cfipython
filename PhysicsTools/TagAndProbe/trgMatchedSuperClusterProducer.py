import FWCore.ParameterSet.Config as cms

def trgMatchedSuperClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('trgMatchedSuperClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

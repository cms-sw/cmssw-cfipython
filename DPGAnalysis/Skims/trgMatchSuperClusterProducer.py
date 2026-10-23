import FWCore.ParameterSet.Config as cms

def trgMatchSuperClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('trgMatchSuperClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def PhotonIsoProducer(*args, **kwargs):
  mod = cms.EDFilter('PhotonIsoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

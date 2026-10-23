import FWCore.ParameterSet.Config as cms

def PhotonIDProducer(*args, **kwargs):
  mod = cms.EDProducer('PhotonIDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

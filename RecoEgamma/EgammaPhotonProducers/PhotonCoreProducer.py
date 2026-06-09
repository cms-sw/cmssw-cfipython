import FWCore.ParameterSet.Config as cms

def PhotonCoreProducer(*args, **kwargs):
  mod = cms.EDProducer('PhotonCoreProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

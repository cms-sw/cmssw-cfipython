import FWCore.ParameterSet.Config as cms

def PhotonValidator(*args, **kwargs):
  mod = cms.EDProducer('PhotonValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

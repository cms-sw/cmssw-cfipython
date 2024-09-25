import FWCore.ParameterSet.Config as cms

def PhotonOfflineClient(*args, **kwargs):
  mod = cms.EDProducer('PhotonOfflineClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

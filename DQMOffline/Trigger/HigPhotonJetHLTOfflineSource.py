import FWCore.ParameterSet.Config as cms

def HigPhotonJetHLTOfflineSource(*args, **kwargs):
  mod = cms.EDProducer('HigPhotonJetHLTOfflineSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

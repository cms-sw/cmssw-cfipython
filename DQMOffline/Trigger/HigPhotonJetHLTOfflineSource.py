import FWCore.ParameterSet.Config as cms

def HigPhotonJetHLTOfflineSource(**kwargs):
  mod = cms.EDProducer('HigPhotonJetHLTOfflineSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

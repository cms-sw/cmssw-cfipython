import FWCore.ParameterSet.Config as cms

def HLTTauDQMOfflineSource(**kwargs):
  mod = cms.EDProducer('HLTTauDQMOfflineSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

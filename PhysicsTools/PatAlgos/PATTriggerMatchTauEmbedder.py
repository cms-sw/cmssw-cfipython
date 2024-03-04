import FWCore.ParameterSet.Config as cms

def PATTriggerMatchTauEmbedder(**kwargs):
  mod = cms.EDProducer('PATTriggerMatchTauEmbedder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

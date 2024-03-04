import FWCore.ParameterSet.Config as cms

def PATTriggerMatchMETEmbedder(**kwargs):
  mod = cms.EDProducer('PATTriggerMatchMETEmbedder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def PATTriggerMatchPhotonEmbedder(**kwargs):
  mod = cms.EDProducer('PATTriggerMatchPhotonEmbedder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

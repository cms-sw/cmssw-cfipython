import FWCore.ParameterSet.Config as cms

def PATTriggerMatchElectronEmbedder(**kwargs):
  mod = cms.EDProducer('PATTriggerMatchElectronEmbedder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

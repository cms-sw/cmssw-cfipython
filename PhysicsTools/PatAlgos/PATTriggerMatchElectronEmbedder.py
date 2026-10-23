import FWCore.ParameterSet.Config as cms

def PATTriggerMatchElectronEmbedder(*args, **kwargs):
  mod = cms.EDProducer('PATTriggerMatchElectronEmbedder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

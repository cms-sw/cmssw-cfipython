import FWCore.ParameterSet.Config as cms

def PATTriggerMatchPhotonEmbedder(*args, **kwargs):
  mod = cms.EDProducer('PATTriggerMatchPhotonEmbedder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

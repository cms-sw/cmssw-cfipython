import FWCore.ParameterSet.Config as cms

def PATTriggerMatchTauEmbedder(*args, **kwargs):
  mod = cms.EDProducer('PATTriggerMatchTauEmbedder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
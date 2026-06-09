import FWCore.ParameterSet.Config as cms

def PATTriggerMatchMETEmbedder(*args, **kwargs):
  mod = cms.EDProducer('PATTriggerMatchMETEmbedder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

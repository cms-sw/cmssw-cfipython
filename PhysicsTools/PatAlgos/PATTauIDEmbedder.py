import FWCore.ParameterSet.Config as cms

def PATTauIDEmbedder(*args, **kwargs):
  mod = cms.EDProducer('PATTauIDEmbedder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

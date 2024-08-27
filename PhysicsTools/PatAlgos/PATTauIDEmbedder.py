import FWCore.ParameterSet.Config as cms

def PATTauIDEmbedder(**kwargs):
  mod = cms.EDProducer('PATTauIDEmbedder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

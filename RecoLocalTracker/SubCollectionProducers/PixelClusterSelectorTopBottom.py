import FWCore.ParameterSet.Config as cms

def PixelClusterSelectorTopBottom(**kwargs):
  mod = cms.EDProducer('PixelClusterSelectorTopBottom',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

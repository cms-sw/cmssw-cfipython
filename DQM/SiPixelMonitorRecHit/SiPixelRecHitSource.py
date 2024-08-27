import FWCore.ParameterSet.Config as cms

def SiPixelRecHitSource(**kwargs):
  mod = cms.EDProducer('SiPixelRecHitSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

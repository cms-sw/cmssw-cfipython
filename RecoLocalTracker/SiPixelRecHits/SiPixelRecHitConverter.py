import FWCore.ParameterSet.Config as cms

def SiPixelRecHitConverter(**kwargs):
  mod = cms.EDProducer('SiPixelRecHitConverter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

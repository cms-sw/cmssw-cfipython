import FWCore.ParameterSet.Config as cms

def SiPixelRecHitSource(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

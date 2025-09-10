import FWCore.ParameterSet.Config as cms

def SiPixelRecHitsValid(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitsValid',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

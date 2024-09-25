import FWCore.ParameterSet.Config as cms

def SiPixelHitEfficiencySource(*args, **kwargs):
  mod = cms.EDProducer('SiPixelHitEfficiencySource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

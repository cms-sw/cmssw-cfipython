import FWCore.ParameterSet.Config as cms

def SiPixelClusterMultiplicityProducer(*args, **kwargs):
  mod = cms.EDProducer('SiPixelClusterMultiplicityProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

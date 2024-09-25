import FWCore.ParameterSet.Config as cms

def SiPixelRecHitFromCUDAPhase1(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitFromCUDAPhase1',
    pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingCUDA'),
    src = cms.InputTag('siPixelClustersPreSplitting'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

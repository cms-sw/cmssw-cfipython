import FWCore.ParameterSet.Config as cms

def SiPixelRecHitFromCUDAPhase2(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitFromCUDAPhase2',
    pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingCUDA'),
    src = cms.InputTag('siPixelClustersPreSplitting'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

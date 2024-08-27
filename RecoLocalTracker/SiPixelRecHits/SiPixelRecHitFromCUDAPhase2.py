import FWCore.ParameterSet.Config as cms

def SiPixelRecHitFromCUDAPhase2(**kwargs):
  mod = cms.EDProducer('SiPixelRecHitFromCUDAPhase2',
    pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingCUDA'),
    src = cms.InputTag('siPixelClustersPreSplitting'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

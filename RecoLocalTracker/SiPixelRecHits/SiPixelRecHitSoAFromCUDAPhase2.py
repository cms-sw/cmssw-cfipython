import FWCore.ParameterSet.Config as cms

def SiPixelRecHitSoAFromCUDAPhase2(**kwargs):
  mod = cms.EDProducer('SiPixelRecHitSoAFromCUDAPhase2',
    pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingCUDA'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

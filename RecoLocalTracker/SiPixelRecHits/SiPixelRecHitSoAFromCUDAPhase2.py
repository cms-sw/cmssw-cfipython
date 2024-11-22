import FWCore.ParameterSet.Config as cms

def SiPixelRecHitSoAFromCUDAPhase2(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitSoAFromCUDAPhase2',
    pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingCUDA'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

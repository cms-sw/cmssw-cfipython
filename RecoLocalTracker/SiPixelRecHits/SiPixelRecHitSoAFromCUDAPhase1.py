import FWCore.ParameterSet.Config as cms

def SiPixelRecHitSoAFromCUDAPhase1(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitSoAFromCUDAPhase1',
    pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingCUDA'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

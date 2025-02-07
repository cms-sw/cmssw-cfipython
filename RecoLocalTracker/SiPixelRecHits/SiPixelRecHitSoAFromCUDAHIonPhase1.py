import FWCore.ParameterSet.Config as cms

def SiPixelRecHitSoAFromCUDAHIonPhase1(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitSoAFromCUDAHIonPhase1',
    pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingCUDA'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

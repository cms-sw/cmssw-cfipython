import FWCore.ParameterSet.Config as cms

def SiPixelRecHitSoAFromCUDAHIonPhase1(**kwargs):
  mod = cms.EDProducer('SiPixelRecHitSoAFromCUDAHIonPhase1',
    pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingCUDA'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

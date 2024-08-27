import FWCore.ParameterSet.Config as cms

def SiPixelRecHitFromCUDAHIonPhase1(**kwargs):
  mod = cms.EDProducer('SiPixelRecHitFromCUDAHIonPhase1',
    pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingCUDA'),
    src = cms.InputTag('siPixelClustersPreSplitting'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

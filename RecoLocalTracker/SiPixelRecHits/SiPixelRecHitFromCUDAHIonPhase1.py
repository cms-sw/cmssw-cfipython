import FWCore.ParameterSet.Config as cms

def SiPixelRecHitFromCUDAHIonPhase1(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitFromCUDAHIonPhase1',
    pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingCUDA'),
    src = cms.InputTag('siPixelClustersPreSplitting'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

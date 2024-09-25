import FWCore.ParameterSet.Config as cms

def SiPixelRecHitFromSoAAlpakaHIonPhase1(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitFromSoAAlpakaHIonPhase1',
    pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
    src = cms.InputTag('siPixelClustersPreSplitting'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

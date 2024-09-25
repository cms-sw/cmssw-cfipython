import FWCore.ParameterSet.Config as cms

def SiPixelRecHitFromSoAAlpakaPhase2(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitFromSoAAlpakaPhase2',
    pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
    src = cms.InputTag('siPixelClustersPreSplitting'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

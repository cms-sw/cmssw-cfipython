import FWCore.ParameterSet.Config as cms

def SiPixelRecHitFromSoAAlpakaPhase1(**kwargs):
  mod = cms.EDProducer('SiPixelRecHitFromSoAAlpakaPhase1',
    pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
    src = cms.InputTag('siPixelClustersPreSplitting'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

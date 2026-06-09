import FWCore.ParameterSet.Config as cms

def SiPixelRecHitFromSoAAlpaka(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitFromSoAAlpaka',
    maxHitsInModules = cms.uint32(1024),
    pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
    src = cms.InputTag('siPixelClustersPreSplitting'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

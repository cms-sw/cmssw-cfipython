import FWCore.ParameterSet.Config as cms

def SiPixelRecHitExtendedAlpaka_alpaka(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitExtendedAlpaka@alpaka',
    pixelRecHitsSoA = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
    trackerRecHitsSoA = cms.InputTag('phase2OTRecHitsSoAConverter'),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

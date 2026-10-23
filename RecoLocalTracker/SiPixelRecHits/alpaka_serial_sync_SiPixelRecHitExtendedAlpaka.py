import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_SiPixelRecHitExtendedAlpaka(*args, **kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::SiPixelRecHitExtendedAlpaka',
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

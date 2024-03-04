import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_SiPixelRecHitAlpakaPhase1(**kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::SiPixelRecHitAlpakaPhase1',
    beamSpot = cms.InputTag('offlineBeamSpotDevice'),
    src = cms.InputTag('siPixelClustersPreSplittingAlpaka'),
    CPE = cms.string('PixelCPEFastParams'),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

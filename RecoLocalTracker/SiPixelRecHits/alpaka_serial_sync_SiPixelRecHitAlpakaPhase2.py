import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_SiPixelRecHitAlpakaPhase2(*args, **kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::SiPixelRecHitAlpakaPhase2',
    beamSpot = cms.InputTag('offlineBeamSpotDevice'),
    src = cms.InputTag('siPixelClustersPreSplittingAlpaka'),
    CPE = cms.string('PixelCPEFastParamsPhase2'),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

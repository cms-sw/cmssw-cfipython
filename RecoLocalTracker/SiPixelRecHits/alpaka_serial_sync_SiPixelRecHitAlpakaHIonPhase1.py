import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_SiPixelRecHitAlpakaHIonPhase1(**kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::SiPixelRecHitAlpakaHIonPhase1',
    beamSpot = cms.InputTag('offlineBeamSpotDevice'),
    src = cms.InputTag('siPixelClustersPreSplittingAlpaka'),
    CPE = cms.string('PixelCPEFastParamsHIonPhase1'),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
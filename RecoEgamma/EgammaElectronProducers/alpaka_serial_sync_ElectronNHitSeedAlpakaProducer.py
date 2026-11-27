import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_ElectronNHitSeedAlpakaProducer(*args, **kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::ElectronNHitSeedAlpakaProducer',
    initialSeeds = cms.InputTag('hltElePixelSeedsCombined'),
    beamSpot = cms.InputTag('hltOnlineBeamSpot'),
    superClusters = cms.InputTag('hltEgammaSuperClustersToPixelMatch'),
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

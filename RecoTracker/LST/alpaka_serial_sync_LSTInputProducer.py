import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_LSTInputProducer(*args, **kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::LSTInputProducer',
    ptCut = cms.double(0.8),
    phase2OTRecHits = cms.InputTag('siPhase2RecHits'),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    seedTracks = cms.VInputTag(
      'lstInitialStepSeedTracks',
      'lstHighPtTripletStepSeedTracks'
    ),
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

import FWCore.ParameterSet.Config as cms

seedProducerFromSoAPhase1 = cms.EDProducer('SeedProducerFromSoAPhase1',
  beamSpot = cms.InputTag('offlineBeamSpot'),
  src = cms.InputTag('pixelTrackSoA'),
  minNumberOfHits = cms.int32(0),
  mightGet = cms.optional.untracked.vstring
)

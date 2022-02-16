import FWCore.ParameterSet.Config as cms

seedProducerFromSoA = cms.EDProducer('SeedProducerFromSoA',
  beamSpot = cms.InputTag('offlineBeamSpot'),
  src = cms.InputTag('pixelTrackSoA'),
  minNumberOfHits = cms.int32(0),
  mightGet = cms.optional.untracked.vstring
)

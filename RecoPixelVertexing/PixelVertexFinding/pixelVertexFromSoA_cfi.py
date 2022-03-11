import FWCore.ParameterSet.Config as cms

pixelVertexFromSoA = cms.EDProducer('PixelVertexProducerFromSoA',
  TrackCollection = cms.InputTag('pixelTracks'),
  beamSpot = cms.InputTag('offlineBeamSpot'),
  src = cms.InputTag('pixelVerticesSoA'),
  mightGet = cms.optional.untracked.vstring
)

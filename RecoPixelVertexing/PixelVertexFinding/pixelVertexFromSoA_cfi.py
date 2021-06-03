import FWCore.ParameterSet.Config as cms

pixelVertexFromSoA = cms.EDProducer('PixelVertexProducerFromSoA',
  TrackCollection = cms.InputTag('pixelTracks'),
  beamSpot = cms.InputTag('offlineBeamSpot'),
  src = cms.InputTag('pixelVertexSoA'),
  mightGet = cms.optional.untracked.vstring
)

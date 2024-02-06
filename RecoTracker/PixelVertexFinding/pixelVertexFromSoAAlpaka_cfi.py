import FWCore.ParameterSet.Config as cms

pixelVertexFromSoAAlpaka = cms.EDProducer('PixelVertexProducerFromSoAAlpaka',
  TrackCollection = cms.InputTag('pixelTracks'),
  beamSpot = cms.InputTag('offlineBeamSpot'),
  src = cms.InputTag('pixelVerticesAlpaka'),
  mightGet = cms.optional.untracked.vstring
)

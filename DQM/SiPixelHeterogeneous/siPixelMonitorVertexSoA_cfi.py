import FWCore.ParameterSet.Config as cms

siPixelMonitorVertexSoA = cms.EDProducer('SiPixelMonitorVertexSoA',
  pixelVertexSrc = cms.InputTag('pixelVerticesSoA'),
  beamSpotSrc = cms.InputTag('offlineBeamSpot'),
  topFolderName = cms.string('SiPixelHeterogeneous/PixelVertexSoA'),
  mightGet = cms.optional.untracked.vstring
)

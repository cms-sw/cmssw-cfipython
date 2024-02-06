import FWCore.ParameterSet.Config as cms

siPixelMonitorVertexSoAAlpaka = cms.EDProducer('SiPixelMonitorVertexSoAAlpaka',
  pixelVertexSrc = cms.InputTag('pixelVerticesAlpaka'),
  beamSpotSrc = cms.InputTag('offlineBeamSpot'),
  topFolderName = cms.string('SiPixelHeterogeneous/PixelVertexAlpaka'),
  mightGet = cms.optional.untracked.vstring
)

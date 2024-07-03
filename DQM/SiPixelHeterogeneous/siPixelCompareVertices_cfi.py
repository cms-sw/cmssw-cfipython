import FWCore.ParameterSet.Config as cms

siPixelCompareVertices = cms.EDProducer('SiPixelCompareVertices',
  pixelVertexReferenceSoA = cms.InputTag('pixelVerticesAlpakaSerial'),
  pixelVertexTargetSoA = cms.InputTag('pixelVerticesAlpaka'),
  beamSpotSrc = cms.InputTag('offlineBeamSpot'),
  topFolderName = cms.string('SiPixelHeterogeneous/PixelVertexCompareSoADeviceVSHost'),
  dzCut = cms.double(1),
  mightGet = cms.optional.untracked.vstring
)

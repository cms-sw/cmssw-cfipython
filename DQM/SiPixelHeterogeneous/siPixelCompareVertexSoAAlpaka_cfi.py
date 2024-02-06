import FWCore.ParameterSet.Config as cms

siPixelCompareVertexSoAAlpaka = cms.EDProducer('SiPixelCompareVertexSoAAlpaka',
  pixelVertexSrcHost = cms.InputTag('pixelVerticesAlpakaSerial'),
  pixelVertexSrcDevice = cms.InputTag('pixelVerticesAlpaka'),
  beamSpotSrc = cms.InputTag('offlineBeamSpot'),
  topFolderName = cms.string('SiPixelHeterogeneous/PixelVertexCompareSoADeviceVSHost'),
  dzCut = cms.double(1),
  mightGet = cms.optional.untracked.vstring
)

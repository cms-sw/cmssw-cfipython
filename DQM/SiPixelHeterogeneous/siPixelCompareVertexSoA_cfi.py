import FWCore.ParameterSet.Config as cms

siPixelCompareVertexSoA = cms.EDProducer('SiPixelCompareVertexSoA',
  pixelVertexSrcCPU = cms.InputTag('pixelVerticesSoA@cpu'),
  pixelVertexSrcGPU = cms.InputTag('pixelVerticesSoA@cuda'),
  beamSpotSrc = cms.InputTag('offlineBeamSpot'),
  topFolderName = cms.string('SiPixelHeterogeneous/PixelVertexCompareSoAGPUvsCPU'),
  dzCut = cms.double(1),
  mightGet = cms.optional.untracked.vstring
)

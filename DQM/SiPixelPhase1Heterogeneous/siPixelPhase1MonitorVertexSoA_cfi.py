import FWCore.ParameterSet.Config as cms

siPixelPhase1MonitorVertexSoA = cms.EDProducer('SiPixelPhase1MonitorVertexSoA',
  pixelVertexSrc = cms.InputTag('pixelVerticesSoA'),
  beamSpotSrc = cms.InputTag('offlineBeamSpot'),
  TopFolderName = cms.string('SiPixelHeterogeneous/PixelVertexSoA'),
  mightGet = cms.optional.untracked.vstring
)

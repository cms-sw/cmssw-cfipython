import FWCore.ParameterSet.Config as cms

siPixelPhase2CompareTrackSoA = cms.EDProducer('SiPixelPhase2CompareTrackSoA',
  pixelTrackSrcCPU = cms.InputTag('pixelTracksSoA@cpu'),
  pixelTrackSrcGPU = cms.InputTag('pixelTracksSoA@cuda'),
  topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU'),
  useQualityCut = cms.bool(True),
  minQuality = cms.string('loose'),
  deltaR2cut = cms.double(0.04),
  mightGet = cms.optional.untracked.vstring
)

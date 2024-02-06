import FWCore.ParameterSet.Config as cms

siPixelPhase1RawDataErrorComparator = cms.EDProducer('SiPixelPhase1RawDataErrorComparator',
  pixelErrorSrcGPU = cms.InputTag('siPixelDigis@cuda'),
  pixelErrorSrcCPU = cms.InputTag('siPixelDigis@cpu'),
  topFolderName = cms.string('SiPixelHeterogeneous/PixelErrorCompareGPUvsCPU'),
  mightGet = cms.optional.untracked.vstring
)

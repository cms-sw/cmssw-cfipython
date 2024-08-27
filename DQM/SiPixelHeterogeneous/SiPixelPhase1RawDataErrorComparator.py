import FWCore.ParameterSet.Config as cms

def SiPixelPhase1RawDataErrorComparator(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1RawDataErrorComparator',
    pixelErrorSrcGPU = cms.InputTag('siPixelDigis@cuda'),
    pixelErrorSrcCPU = cms.InputTag('siPixelDigis@cpu'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelErrorCompareGPUvsCPU'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

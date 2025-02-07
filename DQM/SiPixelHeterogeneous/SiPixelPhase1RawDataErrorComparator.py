import FWCore.ParameterSet.Config as cms

def SiPixelPhase1RawDataErrorComparator(*args, **kwargs):
  mod = cms.EDProducer('SiPixelPhase1RawDataErrorComparator',
    pixelErrorSrcGPU = cms.InputTag('siPixelDigis@cuda'),
    pixelErrorSrcCPU = cms.InputTag('siPixelDigis@cpu'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelErrorCompareGPUvsCPU'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

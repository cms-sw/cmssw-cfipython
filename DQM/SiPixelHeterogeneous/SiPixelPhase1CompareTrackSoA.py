import FWCore.ParameterSet.Config as cms

def SiPixelPhase1CompareTrackSoA(*args, **kwargs):
  mod = cms.EDProducer('SiPixelPhase1CompareTrackSoA',
    pixelTrackSrcCPU = cms.InputTag('pixelTracksSoA@cpu'),
    pixelTrackSrcGPU = cms.InputTag('pixelTracksSoA@cuda'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU'),
    useQualityCut = cms.bool(True),
    minQuality = cms.string('loose'),
    deltaR2cut = cms.double(0.0004),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

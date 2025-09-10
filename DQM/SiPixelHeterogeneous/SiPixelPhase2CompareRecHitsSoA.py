import FWCore.ParameterSet.Config as cms

def SiPixelPhase2CompareRecHitsSoA(*args, **kwargs):
  mod = cms.EDProducer('SiPixelPhase2CompareRecHitsSoA',
    pixelHitsSrcCPU = cms.InputTag('siPixelRecHitsPreSplittingSoA@cpu'),
    pixelHitsSrcGPU = cms.InputTag('siPixelRecHitsPreSplittingSoA@cuda'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU'),
    minD2cut = cms.double(0.0001),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

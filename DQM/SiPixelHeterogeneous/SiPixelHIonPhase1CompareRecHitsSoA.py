import FWCore.ParameterSet.Config as cms

def SiPixelHIonPhase1CompareRecHitsSoA(**kwargs):
  mod = cms.EDProducer('SiPixelHIonPhase1CompareRecHitsSoA',
    pixelHitsSrcCPU = cms.InputTag('siPixelRecHitsPreSplittingSoA@cpu'),
    pixelHitsSrcGPU = cms.InputTag('siPixelRecHitsPreSplittingSoA@cuda'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU'),
    minD2cut = cms.double(0.0001),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

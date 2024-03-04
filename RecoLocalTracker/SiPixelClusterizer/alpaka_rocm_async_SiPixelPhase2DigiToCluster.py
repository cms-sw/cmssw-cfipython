import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_SiPixelPhase2DigiToCluster(**kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::SiPixelPhase2DigiToCluster',
    IncludeErrors = cms.bool(True),
    clusterThreshold_layer1 = cms.int32(4000),
    clusterThreshold_otherLayers = cms.int32(4000),
    ElectronPerADCGain = cms.double(1500),
    Phase2ReadoutMode = cms.int32(3),
    Phase2DigiBaseline = cms.uint32(1000),
    Phase2KinkADC = cms.uint32(8),
    InputDigis = cms.InputTag('simSiPixelDigis', 'Pixel'),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_SiPixelRawToClusterHIonPhase1(**kwargs):
  mod = cms.EDProducer('alpaka_cuda_async::SiPixelRawToClusterHIonPhase1',
    IncludeErrors = cms.bool(True),
    UseQualityInfo = cms.bool(False),
    clusterThreshold_layer1 = cms.int32(2000),
    clusterThreshold_otherLayers = cms.int32(4000),
    VCaltoElectronGain = cms.double(47),
    VCaltoElectronGain_L1 = cms.double(50),
    VCaltoElectronOffset = cms.double(-60),
    VCaltoElectronOffset_L1 = cms.double(-670),
    InputLabel = cms.InputTag('rawDataCollector'),
    Regions = cms.PSet(
      inputs = cms.optional.VInputTag,
      deltaPhi = cms.optional.vdouble,
      maxZ = cms.optional.vdouble,
      beamSpot = cms.optional.InputTag
    ),
    CablingMapLabel = cms.string(''),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

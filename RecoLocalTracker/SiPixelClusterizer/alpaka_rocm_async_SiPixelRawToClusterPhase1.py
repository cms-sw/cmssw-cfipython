import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_SiPixelRawToClusterPhase1(*args, **kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::SiPixelRawToClusterPhase1',
    IncludeErrors = cms.bool(True),
    UseQualityInfo = cms.bool(False),
    verbose = cms.bool(False),
    clusterThreshold_layer1 = cms.int32(2000),
    clusterThreshold_otherLayers = cms.int32(4000),
    VCaltoElectronGain = cms.double(47),
    VCaltoElectronGain_L1 = cms.double(50),
    VCaltoElectronOffset = cms.double(-60),
    VCaltoElectronOffset_L1 = cms.double(-670),
    DoDigiMorphing = cms.bool(False),
    MaxFakesInModule = cms.uint32(2400),
    InputLabel = cms.InputTag('rawDataCollector'),
    Regions = cms.PSet(
      inputs = cms.optional.VInputTag,
      deltaPhi = cms.optional.vdouble,
      maxZ = cms.optional.vdouble,
      beamSpot = cms.optional.InputTag
    ),
    barrelRegions = cms.vstring(
      '1,1-12,1-2',
      '1,1-12,7-8',
      '2,1-28,1',
      '2,1-28,8'
    ),
    endcapRegions = cms.vstring(),
    CablingMapLabel = cms.string(''),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

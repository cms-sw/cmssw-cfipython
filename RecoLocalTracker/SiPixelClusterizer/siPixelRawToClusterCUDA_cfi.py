import FWCore.ParameterSet.Config as cms

siPixelRawToClusterCUDA = cms.EDProducer('SiPixelRawToClusterCUDA',
  isRun2 = cms.bool(True),
  IncludeErrors = cms.bool(True),
  UseQualityInfo = cms.bool(False),
  InputLabel = cms.InputTag('rawDataCollector'),
  Regions = cms.PSet(
    inputs = cms.optional.VInputTag,
    deltaPhi = cms.optional.vdouble,
    maxZ = cms.optional.vdouble,
    beamSpot = cms.optional.InputTag
  ),
  CablingMapLabel = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)

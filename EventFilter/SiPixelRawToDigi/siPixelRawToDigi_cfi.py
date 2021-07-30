import FWCore.ParameterSet.Config as cms

siPixelRawToDigi = cms.EDProducer('SiPixelRawToDigi',
  IncludeErrors = cms.bool(True),
  UseQualityInfo = cms.bool(False),
  ErrorList = cms.vint32(29),
  UserErrorList = cms.vint32(40),
  InputLabel = cms.InputTag('siPixelRawData'),
  Regions = cms.PSet(
    inputs = cms.optional.VInputTag,
    deltaPhi = cms.optional.vdouble,
    maxZ = cms.optional.vdouble,
    beamSpot = cms.optional.InputTag
  ),
  UsePilotBlade = cms.bool(False),
  UsePhase1 = cms.bool(False),
  CablingMapLabel = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)

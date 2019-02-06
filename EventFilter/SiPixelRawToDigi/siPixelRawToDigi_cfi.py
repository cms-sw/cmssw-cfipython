import FWCore.ParameterSet.Config as cms

siPixelRawToDigi = cms.EDProducer('SiPixelRawToDigi',
  IncludeErrors = cms.bool(True),
  UseQualityInfo = cms.bool(False),
  ErrorList = cms.vint32(29),
  UserErrorList = cms.vint32(40),
  InputLabel = cms.InputTag('siPixelRawData'),
  Regions = cms.PSet(),
  Timing = cms.untracked.bool(False),
  UsePilotBlade = cms.bool(False),
  UsePhase1 = cms.bool(False),
  CablingMapLabel = cms.string('')
)

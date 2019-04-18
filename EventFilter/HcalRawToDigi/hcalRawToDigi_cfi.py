import FWCore.ParameterSet.Config as cms

hcalRawToDigi = cms.EDProducer('HcalRawToDigi',
  HcalFirstFED = cms.untracked.int32(700),
  firstSample = cms.int32(0),
  lastSample = cms.int32(9),
  FilterDataQuality = cms.bool(True),
  FEDs = cms.untracked.vint32(),
  UnpackZDC = cms.untracked.bool(True),
  UnpackCalib = cms.untracked.bool(True),
  UnpackUMNio = cms.untracked.bool(True),
  UnpackTTP = cms.untracked.bool(True),
  silent = cms.untracked.bool(True),
  ComplainEmptyData = cms.untracked.bool(False),
  UnpackerMode = cms.untracked.int32(0),
  ExpectedOrbitMessageTime = cms.untracked.int32(-1),
  InputLabel = cms.InputTag('rawDataCollector'),
  ElectronicsMap = cms.string('')
)

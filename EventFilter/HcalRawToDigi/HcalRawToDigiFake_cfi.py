import FWCore.ParameterSet.Config as cms

HcalRawToDigiFake = cms.EDProducer('HcalRawToDigiFake',
  UnpackZDC = cms.bool(True),
  UnpackCalib = cms.bool(True),
  UnpackTTP = cms.bool(True),
  QIE10 = cms.InputTag('simHcalDigis', 'HFQIE10DigiCollection'),
  QIE11 = cms.InputTag('simHcalDigis', 'HBHEQIE11DigiCollection'),
  HBHE = cms.InputTag('simHcalDigis'),
  HF = cms.InputTag('simHcalDigis'),
  HO = cms.InputTag('simHcalDigis'),
  TRIG = cms.InputTag('simHcalTriggerPrimitiveDigis'),
  HOTP = cms.InputTag(''),
  CALIB = cms.InputTag(''),
  ZDC = cms.InputTag('simHcalUnsuppressedDigis'),
  ZDCQIE10 = cms.InputTag(''),
  TTP = cms.InputTag(''),
  InputLabel = cms.InputTag('rawDataCollector'),
  firstSample = cms.int32(0),
  lastSample = cms.int32(0)
)

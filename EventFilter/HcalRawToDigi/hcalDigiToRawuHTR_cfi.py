import FWCore.ParameterSet.Config as cms

hcalDigiToRawuHTR = cms.EDProducer('HcalDigiToRawuHTR',
  Verbosity = cms.untracked.int32(0),
  tdc1 = cms.int32(4),
  tdc2 = cms.int32(20),
  packHBTDC = cms.bool(False),
  ElectronicsMap = cms.string(''),
  QIE10 = cms.InputTag('simHcalDigis', 'HFQIE10DigiCollection'),
  QIE11 = cms.InputTag('simHcalDigis', 'HBHEQIE11DigiCollection'),
  HBHEqie8 = cms.InputTag('simHcalDigis'),
  HFqie8 = cms.InputTag('simHcalDigis'),
  TP = cms.InputTag('simHcalTriggerPrimitiveDigis'),
  premix = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)

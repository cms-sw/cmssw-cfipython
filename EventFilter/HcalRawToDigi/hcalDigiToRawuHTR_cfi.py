import FWCore.ParameterSet.Config as cms

hcalDigiToRawuHTR = cms.EDProducer('HcalDigiToRawuHTR',
  Verbosity = cms.untracked.int32(0),
  ElectronicsMap = cms.string(''),
  QIE10 = cms.InputTag('simHcalDigis', 'HFQIE10DigiCollection'),
  QIE11 = cms.InputTag('simHcalDigis', 'HBHEQIE11DigiCollection'),
  HBHEqie8 = cms.InputTag('simHcalDigis'),
  HFqie8 = cms.InputTag('simHcalDigis'),
  TP = cms.InputTag('simHcalTriggerPrimitiveDigis'),
  premix = cms.bool(False)
)

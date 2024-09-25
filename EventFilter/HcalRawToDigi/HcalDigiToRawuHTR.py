import FWCore.ParameterSet.Config as cms

def HcalDigiToRawuHTR(*args, **kwargs):
  mod = cms.EDProducer('HcalDigiToRawuHTR',
    Verbosity = cms.untracked.int32(0),
    tdc1 = cms.vint32(
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12,
      12
    ),
    tdc2 = cms.vint32(
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14,
      14
    ),
    packHBTDC = cms.bool(True),
    ElectronicsMap = cms.string(''),
    QIE10 = cms.InputTag('simHcalDigis', 'HFQIE10DigiCollection'),
    QIE11 = cms.InputTag('simHcalDigis', 'HBHEQIE11DigiCollection'),
    HBHEqie8 = cms.InputTag('simHcalDigis'),
    HFqie8 = cms.InputTag('simHcalDigis'),
    TP = cms.InputTag('simHcalTriggerPrimitiveDigis'),
    premix = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def EcalTrigPrimProducer(**kwargs):
  mod = cms.EDProducer('EcalTrigPrimProducer',
    BarrelOnly = cms.bool(False),
    TcpOutput = cms.bool(False),
    Debug = cms.bool(False),
    Famos = cms.bool(False),
    Label = cms.string('simEcalUnsuppressedDigis'),
    InstanceEB = cms.string(''),
    InstanceEE = cms.string(''),
    binOfMaximum = cms.int32(-1),
    TPinfoPrintout = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

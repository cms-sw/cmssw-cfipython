import FWCore.ParameterSet.Config as cms

def EcalTrigPrimProducer(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

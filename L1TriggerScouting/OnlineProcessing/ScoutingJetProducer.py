import FWCore.ParameterSet.Config as cms

def ScoutingJetProducer(*args, **kwargs):
  mod = cms.EDProducer('ScoutingJetProducer',
    src = cms.required.InputTag,
    akR = cms.required.double,
    ptMin = cms.required.double,
    towerMinHwEt = cms.int32(1),
    towerMaxHwEt = cms.int32(-1),
    mantissaPrecision = cms.int32(10),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def L1ScoutingCaloJetProducer(*args, **kwargs):
  mod = cms.EDProducer('L1ScoutingCaloJetProducer',
    src = cms.required.InputTag,
    akR = cms.required.double,
    ptMin = cms.required.double,
    towerMinHwEt = cms.int32(1),
    towerMaxHwEt = cms.int32(-1),
    applyJECs = cms.bool(False),
    jecFile = cms.required.FileInPath,
    jecPUProxyTowerMinHwEt = cms.int32(1),
    jecPUProxyTowerMaxHwEt = cms.int32(-1),
    jecPUProxyTowerMinAbsHwEta = cms.int32(0),
    jecPUProxyTowerMaxAbsHwEta = cms.int32(4),
    mantissaPrecision = cms.int32(10),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

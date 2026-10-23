import FWCore.ParameterSet.Config as cms

def L1ScoutingEtSumOrbitFlatTableProducer(*args, **kwargs):
  mod = cms.EDProducer('L1ScoutingEtSumOrbitFlatTableProducer',
    src = cms.required.InputTag,
    name = cms.required.string,
    doc = cms.required.string,
    singleton = cms.bool(True),
    writePhysicalValues = cms.bool(True),
    writeHardwareValues = cms.bool(False),
    writeHF = cms.bool(True),
    writeAsym = cms.bool(True),
    writeMinBias = cms.bool(True),
    writeTowerCount = cms.bool(True),
    writeCentrality = cms.bool(True),
    ptPrecision = cms.int32(-1),
    phiPrecision = cms.int32(-1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

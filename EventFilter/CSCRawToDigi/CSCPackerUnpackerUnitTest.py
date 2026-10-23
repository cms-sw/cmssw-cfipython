import FWCore.ParameterSet.Config as cms

def CSCPackerUnpackerUnitTest(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCPackerUnpackerUnitTest',
    wireTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCWireDigi'),
    stripTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCStripDigi'),
    comparatorTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCComparatorDigi'),
    wireUnpackedTag = cms.InputTag('muonCSCDigis', 'MuonCSCWireDigi'),
    stripUnpackedTag = cms.InputTag('muonCSCDigis', 'MuonCSCStripDigi'),
    comparatorUnpackedTag = cms.InputTag('muonCSCDigis', 'MuonCSCComparatorDigi'),
    alctTag = cms.InputTag('simCscTriggerPrimitiveDigis'),
    clctTag = cms.InputTag('simCscTriggerPrimitiveDigis'),
    clctpreTag = cms.InputTag('simCscTriggerPrimitiveDigis'),
    corrclctTag = cms.InputTag('simCscTriggerPrimitiveDigis'),
    showerDigiTag = cms.InputTag('simCscTriggerPrimitiveDigis'),
    alctWindowMin = cms.int32(-3),
    alctWindowMax = cms.int32(3),
    clctWindowMin = cms.int32(-3),
    clctWindowMax = cms.int32(3),
    preTriggerWindowMin = cms.int32(-3),
    preTriggerWindowMax = cms.int32(1),
    formatVersion = cms.uint32(2005),
    testALCT = cms.bool(True),
    testCLCT = cms.bool(True),
    testPreCLCT = cms.bool(True),
    usePreTriggers = cms.bool(True),
    packEverything = cms.bool(False),
    useCSCShowers = cms.bool(False),
    packByCFEB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

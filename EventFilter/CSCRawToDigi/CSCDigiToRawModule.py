import FWCore.ParameterSet.Config as cms

def CSCDigiToRawModule(*args, **kwargs):
  mod = cms.EDProducer('CSCDigiToRawModule',
    formatVersion = cms.uint32(2005),
    usePreTriggers = cms.bool(True),
    packEverything = cms.bool(False),
    packByCFEB = cms.bool(False),
    useGEMs = cms.bool(False),
    useCSCShowers = cms.bool(False),
    wireDigiTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCWireDigi'),
    stripDigiTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCStripDigi'),
    comparatorDigiTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCComparatorDigi'),
    alctDigiTag = cms.InputTag('simCscTriggerPrimitiveDigis'),
    clctDigiTag = cms.InputTag('simCscTriggerPrimitiveDigis'),
    preTriggerTag = cms.InputTag('simCscTriggerPrimitiveDigis'),
    preTriggerDigiTag = cms.InputTag('simCscTriggerPrimitiveDigis'),
    correlatedLCTDigiTag = cms.InputTag('simCscTriggerPrimitiveDigis', 'MPCSORTED'),
    padDigiClusterTag = cms.InputTag('simMuonGEMPadDigiClusters'),
    showerDigiTag = cms.InputTag('simCscTriggerPrimitiveDigis'),
    anodeShowerDigiTag = cms.InputTag('simCscTriggerPrimitiveDigis'),
    cathodeShowerDigiTag = cms.InputTag('simCscTriggerPrimitiveDigis'),
    anodeALCTShowerDigiTag = cms.InputTag('simCscTriggerPrimitiveDigis'),
    alctWindowMin = cms.int32(-3),
    alctWindowMax = cms.int32(3),
    clctWindowMin = cms.int32(-3),
    clctWindowMax = cms.int32(3),
    preTriggerWindowMin = cms.int32(-3),
    preTriggerWindowMax = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

cscPacker = cms.EDProducer('CSCDigiToRawModule',
  useFormatVersion = cms.uint32(2005),
  usePreTriggers = cms.bool(True),
  packEverything = cms.bool(False),
  wireDigiTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCWireDigi'),
  stripDigiTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCStripDigi'),
  comparatorDigiTag = cms.InputTag('simMuonCSCDigis', 'MuonCSCComparatorDigi'),
  alctDigiTag = cms.InputTag('simCscTriggerPrimitiveDigis'),
  clctDigiTag = cms.InputTag('simCscTriggerPrimitiveDigis'),
  preTriggerTag = cms.InputTag('simCscTriggerPrimitiveDigis'),
  correlatedLCTDigiTag = cms.InputTag('simCscTriggerPrimitiveDigis', 'MPCSORTED'),
  alctWindowMin = cms.int32(-3),
  alctWindowMax = cms.int32(3),
  clctWindowMin = cms.int32(-3),
  clctWindowMax = cms.int32(3),
  preTriggerWindowMin = cms.int32(-3),
  preTriggerWindowMax = cms.int32(1)
)

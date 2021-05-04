import FWCore.ParameterSet.Config as cms

simEmtfShowersDef = cms.EDProducer('L1TMuonEndCapShowerProducer',
  enableOneNominalShowers = cms.bool(True),
  enableTwoLooseShowers = cms.bool(False),
  nLooseShowers = cms.uint32(2),
  nNominalShowers = cms.uint32(1),
  CSCShowerInput = cms.InputTag('simCscTriggerPrimitiveDigis'),
  mightGet = cms.optional.untracked.vstring
)

import FWCore.ParameterSet.Config as cms

simEmtfShowersDef = cms.EDProducer('L1TMuonEndCapShowerProducer',
  enableOneLooseShower = cms.bool(True),
  enableOneNominalShower = cms.bool(True),
  enableOneTightShower = cms.bool(True),
  enableTwoLooseShowers = cms.bool(False),
  CSCShowerInput = cms.InputTag('simCscTriggerPrimitiveDigis'),
  mightGet = cms.optional.untracked.vstring
)

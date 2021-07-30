import FWCore.ParameterSet.Config as cms

simGmtShowerDigisDef = cms.EDProducer('L1TMuonShowerProducer',
  showerInput = cms.InputTag('simEmtfShowers', 'EMTF'),
  bxMin = cms.int32(0),
  bxMax = cms.int32(0),
  minNominalShowers = cms.uint32(1),
  minTwoLooseShowers = cms.uint32(0),
  mightGet = cms.optional.untracked.vstring
)

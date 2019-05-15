import FWCore.ParameterSet.Config as cms

puTable = cms.EDProducer('NPUTablesProducer',
  src = cms.InputTag('slimmedAddPileupInfo')
)

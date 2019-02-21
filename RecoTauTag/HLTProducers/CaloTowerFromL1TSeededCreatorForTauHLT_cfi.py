import FWCore.ParameterSet.Config as cms

CaloTowerFromL1TSeededCreatorForTauHLT = cms.EDProducer('CaloTowerFromL1TSeededCreatorForTauHLT',
  TauTrigger = cms.InputTag('hltL1sDoubleIsoTau40er'),
  towers = cms.InputTag('towerMaker'),
  UseTowersInCone = cms.double(0.8),
  minimumE = cms.double(0.8),
  minimumEt = cms.double(0.5),
  verbose = cms.untracked.int32(0)
)

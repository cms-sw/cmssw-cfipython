import FWCore.ParameterSet.Config as cms

caloTowerMakerHLT = cms.EDProducer('CaloTowerCreatorForTauHLT',
  TauTrigger = cms.InputTag('l1extraParticles', 'Tau'),
  TauId = cms.int32(0),
  towers = cms.InputTag('towerMaker'),
  UseTowersInCone = cms.double(0.8),
  minimumE = cms.double(0.8),
  minimumEt = cms.double(0.5),
  verbose = cms.untracked.int32(0)
)

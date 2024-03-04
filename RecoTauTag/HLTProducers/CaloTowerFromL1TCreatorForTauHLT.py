import FWCore.ParameterSet.Config as cms

def CaloTowerFromL1TCreatorForTauHLT(**kwargs):
  mod = cms.EDProducer('CaloTowerFromL1TCreatorForTauHLT',
    TauTrigger = cms.InputTag('caloStage2Digis'),
    towers = cms.InputTag('towerMaker'),
    TauId = cms.int32(0),
    UseTowersInCone = cms.double(0.8),
    minimumE = cms.double(0.8),
    minimumEt = cms.double(0.5),
    BX = cms.int32(0),
    verbose = cms.untracked.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

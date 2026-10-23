import FWCore.ParameterSet.Config as cms

def CaloTowerFromL1TSeededCreatorForTauHLT(*args, **kwargs):
  mod = cms.EDProducer('CaloTowerFromL1TSeededCreatorForTauHLT',
    TauTrigger = cms.InputTag('hltL1sDoubleIsoTau40er'),
    towers = cms.InputTag('towerMaker'),
    UseTowersInCone = cms.double(0.8),
    minimumE = cms.double(0.8),
    minimumEt = cms.double(0.5),
    verbose = cms.untracked.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

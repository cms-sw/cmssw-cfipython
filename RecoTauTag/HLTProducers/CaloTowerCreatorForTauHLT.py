import FWCore.ParameterSet.Config as cms

def CaloTowerCreatorForTauHLT(**kwargs):
  mod = cms.EDProducer('CaloTowerCreatorForTauHLT',
    TauTrigger = cms.InputTag('l1extraParticles', 'Tau'),
    TauId = cms.int32(0),
    towers = cms.InputTag('towerMaker'),
    UseTowersInCone = cms.double(0.8),
    minimumE = cms.double(0.8),
    minimumEt = cms.double(0.5),
    verbose = cms.untracked.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

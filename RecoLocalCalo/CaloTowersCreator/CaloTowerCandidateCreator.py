import FWCore.ParameterSet.Config as cms

def CaloTowerCandidateCreator(**kwargs):
  mod = cms.EDProducer('CaloTowerCandidateCreator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

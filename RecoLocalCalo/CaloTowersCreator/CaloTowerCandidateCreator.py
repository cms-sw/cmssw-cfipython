import FWCore.ParameterSet.Config as cms

def CaloTowerCandidateCreator(*args, **kwargs):
  mod = cms.EDProducer('CaloTowerCandidateCreator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

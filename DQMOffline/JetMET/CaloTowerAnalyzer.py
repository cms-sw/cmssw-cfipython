import FWCore.ParameterSet.Config as cms

def CaloTowerAnalyzer(**kwargs):
  mod = cms.EDProducer('CaloTowerAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

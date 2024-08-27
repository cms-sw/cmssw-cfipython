import FWCore.ParameterSet.Config as cms

def CaloTowersAnalyzer(**kwargs):
  mod = cms.EDProducer('CaloTowersAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

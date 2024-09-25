import FWCore.ParameterSet.Config as cms

def CaloTowersAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('CaloTowersAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

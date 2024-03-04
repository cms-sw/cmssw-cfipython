import FWCore.ParameterSet.Config as cms

def HGCalTriggerNtupleManager(**kwargs):
  mod = cms.EDAnalyzer('HGCalTriggerNtupleManager',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

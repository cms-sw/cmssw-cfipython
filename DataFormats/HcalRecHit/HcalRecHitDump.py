import FWCore.ParameterSet.Config as cms

def HcalRecHitDump(**kwargs):
  mod = cms.EDAnalyzer('HcalRecHitDump',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

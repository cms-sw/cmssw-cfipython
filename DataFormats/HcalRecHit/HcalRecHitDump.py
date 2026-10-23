import FWCore.ParameterSet.Config as cms

def HcalRecHitDump(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalRecHitDump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

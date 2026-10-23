import FWCore.ParameterSet.Config as cms

def HcalHitAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalHitAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

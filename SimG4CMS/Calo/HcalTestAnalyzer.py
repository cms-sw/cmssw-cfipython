import FWCore.ParameterSet.Config as cms

def HcalTestAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalTestAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

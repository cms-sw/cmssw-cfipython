import FWCore.ParameterSet.Config as cms

def L1O2OTestAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('L1O2OTestAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

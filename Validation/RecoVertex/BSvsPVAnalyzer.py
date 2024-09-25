import FWCore.ParameterSet.Config as cms

def BSvsPVAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('BSvsPVAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

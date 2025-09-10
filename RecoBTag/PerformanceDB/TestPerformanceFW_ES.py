import FWCore.ParameterSet.Config as cms

def TestPerformanceFW_ES(*args, **kwargs):
  mod = cms.EDAnalyzer('TestPerformanceFW_ES',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

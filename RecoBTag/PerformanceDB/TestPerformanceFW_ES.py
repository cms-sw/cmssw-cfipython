import FWCore.ParameterSet.Config as cms

def TestPerformanceFW_ES(**kwargs):
  mod = cms.EDAnalyzer('TestPerformanceFW_ES',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

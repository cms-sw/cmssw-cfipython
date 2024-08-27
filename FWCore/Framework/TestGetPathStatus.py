import FWCore.ParameterSet.Config as cms

def TestGetPathStatus(**kwargs):
  mod = cms.EDAnalyzer('TestGetPathStatus',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

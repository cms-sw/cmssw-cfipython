import FWCore.ParameterSet.Config as cms

def TestServiceOne(**kwargs):
  mod = cms.Service('TestServiceOne',
    verbose = cms.untracked.bool(False)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

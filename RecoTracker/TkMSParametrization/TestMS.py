import FWCore.ParameterSet.Config as cms

def TestMS(*args, **kwargs):
  mod = cms.EDAnalyzer('TestMS',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def TestETLNavigation(*args, **kwargs):
  mod = cms.EDAnalyzer('TestETLNavigation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

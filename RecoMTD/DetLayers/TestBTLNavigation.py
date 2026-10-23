import FWCore.ParameterSet.Config as cms

def TestBTLNavigation(*args, **kwargs):
  mod = cms.EDAnalyzer('TestBTLNavigation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def TestAssociator(*args, **kwargs):
  mod = cms.EDAnalyzer('TestAssociator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

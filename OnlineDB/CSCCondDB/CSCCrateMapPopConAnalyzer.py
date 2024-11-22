import FWCore.ParameterSet.Config as cms

def CSCCrateMapPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCCrateMapPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

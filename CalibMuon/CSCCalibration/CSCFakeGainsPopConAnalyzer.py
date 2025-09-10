import FWCore.ParameterSet.Config as cms

def CSCFakeGainsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCFakeGainsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

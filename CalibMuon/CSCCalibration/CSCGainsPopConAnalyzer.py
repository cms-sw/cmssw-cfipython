import FWCore.ParameterSet.Config as cms

def CSCGainsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCGainsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def CSCCrosstalkPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCCrosstalkPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

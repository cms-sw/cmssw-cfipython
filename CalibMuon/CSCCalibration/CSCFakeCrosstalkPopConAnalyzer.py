import FWCore.ParameterSet.Config as cms

def CSCFakeCrosstalkPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCFakeCrosstalkPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

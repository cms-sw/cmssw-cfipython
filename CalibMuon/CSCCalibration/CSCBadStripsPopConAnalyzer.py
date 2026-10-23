import FWCore.ParameterSet.Config as cms

def CSCBadStripsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCBadStripsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

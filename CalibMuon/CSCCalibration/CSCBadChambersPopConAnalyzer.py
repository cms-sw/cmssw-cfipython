import FWCore.ParameterSet.Config as cms

def CSCBadChambersPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCBadChambersPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

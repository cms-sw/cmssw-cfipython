import FWCore.ParameterSet.Config as cms

def CSCChamberIndexPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCChamberIndexPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

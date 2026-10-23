import FWCore.ParameterSet.Config as cms

def CSCBadWiresPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCBadWiresPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

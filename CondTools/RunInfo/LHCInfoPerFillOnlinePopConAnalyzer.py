import FWCore.ParameterSet.Config as cms

def LHCInfoPerFillOnlinePopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('LHCInfoPerFillOnlinePopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

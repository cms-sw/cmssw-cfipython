import FWCore.ParameterSet.Config as cms

def DTStatusFlagPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DTStatusFlagPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def DTDeadFlagPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DTDeadFlagPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

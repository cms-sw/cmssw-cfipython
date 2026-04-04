import FWCore.ParameterSet.Config as cms

def CondReader(*args, **kwargs):
  mod = cms.EDAnalyzer('CondReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

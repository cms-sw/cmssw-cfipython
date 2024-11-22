import FWCore.ParameterSet.Config as cms

def HitEff(*args, **kwargs):
  mod = cms.EDAnalyzer('HitEff',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

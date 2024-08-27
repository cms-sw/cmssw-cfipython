import FWCore.ParameterSet.Config as cms

def HitEff(**kwargs):
  mod = cms.EDAnalyzer('HitEff',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

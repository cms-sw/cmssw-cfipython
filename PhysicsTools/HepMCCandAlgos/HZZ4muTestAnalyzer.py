import FWCore.ParameterSet.Config as cms

def HZZ4muTestAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HZZ4muTestAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

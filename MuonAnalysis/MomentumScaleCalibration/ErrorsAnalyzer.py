import FWCore.ParameterSet.Config as cms

def ErrorsAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ErrorsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

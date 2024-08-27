import FWCore.ParameterSet.Config as cms

def DTEffAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DTEffAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

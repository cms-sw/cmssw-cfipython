import FWCore.ParameterSet.Config as cms

def GctErrorAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('GctErrorAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

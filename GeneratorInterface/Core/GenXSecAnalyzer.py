import FWCore.ParameterSet.Config as cms

def GenXSecAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('GenXSecAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

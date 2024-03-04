import FWCore.ParameterSet.Config as cms

def GctTimingAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('GctTimingAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

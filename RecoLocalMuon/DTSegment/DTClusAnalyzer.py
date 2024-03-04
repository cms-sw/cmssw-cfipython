import FWCore.ParameterSet.Config as cms

def DTClusAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DTClusAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

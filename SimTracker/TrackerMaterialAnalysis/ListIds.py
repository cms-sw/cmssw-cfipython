import FWCore.ParameterSet.Config as cms

def ListIds(**kwargs):
  mod = cms.EDAnalyzer('ListIds',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

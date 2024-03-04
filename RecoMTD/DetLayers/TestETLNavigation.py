import FWCore.ParameterSet.Config as cms

def TestETLNavigation(**kwargs):
  mod = cms.EDAnalyzer('TestETLNavigation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

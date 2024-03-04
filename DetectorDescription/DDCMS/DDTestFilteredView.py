import FWCore.ParameterSet.Config as cms

def DDTestFilteredView(**kwargs):
  mod = cms.EDAnalyzer('DDTestFilteredView',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

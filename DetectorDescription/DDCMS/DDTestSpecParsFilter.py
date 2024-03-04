import FWCore.ParameterSet.Config as cms

def DDTestSpecParsFilter(**kwargs):
  mod = cms.EDAnalyzer('DDTestSpecParsFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

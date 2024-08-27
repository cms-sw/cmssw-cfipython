import FWCore.ParameterSet.Config as cms

def DDTestCompactView(**kwargs):
  mod = cms.EDAnalyzer('DDTestCompactView',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

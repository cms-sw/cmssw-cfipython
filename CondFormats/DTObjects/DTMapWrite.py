import FWCore.ParameterSet.Config as cms

def DTMapWrite(**kwargs):
  mod = cms.EDAnalyzer('DTMapWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

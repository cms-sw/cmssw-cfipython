import FWCore.ParameterSet.Config as cms

def UTC_SLUMMARY(**kwargs):
  mod = cms.EDAnalyzer('UTC_SLUMMARY',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

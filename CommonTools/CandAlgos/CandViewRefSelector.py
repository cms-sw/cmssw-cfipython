import FWCore.ParameterSet.Config as cms

def CandViewRefSelector(**kwargs):
  mod = cms.EDFilter('CandViewRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

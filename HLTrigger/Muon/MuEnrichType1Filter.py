import FWCore.ParameterSet.Config as cms

def MuEnrichType1Filter(*args, **kwargs):
  mod = cms.EDFilter('MuEnrichType1Filter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

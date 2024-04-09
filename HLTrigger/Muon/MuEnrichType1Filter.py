import FWCore.ParameterSet.Config as cms

def MuEnrichType1Filter(**kwargs):
  mod = cms.EDFilter('MuEnrichType1Filter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
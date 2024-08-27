import FWCore.ParameterSet.Config as cms

def FilterByLTC(**kwargs):
  mod = cms.EDFilter('FilterByLTC',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

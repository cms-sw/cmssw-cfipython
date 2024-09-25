import FWCore.ParameterSet.Config as cms

def FilterByLTC(*args, **kwargs):
  mod = cms.EDFilter('FilterByLTC',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

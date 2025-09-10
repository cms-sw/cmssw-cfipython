import FWCore.ParameterSet.Config as cms

def LHEmttFilter(*args, **kwargs):
  mod = cms.EDFilter('LHEmttFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

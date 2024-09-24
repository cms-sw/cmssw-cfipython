import FWCore.ParameterSet.Config as cms

def FilterOutScraping(*args, **kwargs):
  mod = cms.EDFilter('FilterOutScraping',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

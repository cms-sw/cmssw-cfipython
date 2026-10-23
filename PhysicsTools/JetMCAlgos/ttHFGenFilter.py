import FWCore.ParameterSet.Config as cms

def ttHFGenFilter(*args, **kwargs):
  mod = cms.EDFilter('ttHFGenFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

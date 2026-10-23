import FWCore.ParameterSet.Config as cms

def ExhumeGeneratorFilter(*args, **kwargs):
  mod = cms.EDFilter('ExhumeGeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def PythiaDauVFilter(*args, **kwargs):
  mod = cms.EDFilter('PythiaDauVFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

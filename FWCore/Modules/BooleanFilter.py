import FWCore.ParameterSet.Config as cms

def BooleanFilter(*args, **kwargs):
  mod = cms.EDFilter('BooleanFilter',
    src = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

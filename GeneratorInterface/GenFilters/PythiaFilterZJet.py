import FWCore.ParameterSet.Config as cms

def PythiaFilterZJet(*args, **kwargs):
  mod = cms.EDFilter('PythiaFilterZJet',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

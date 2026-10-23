import FWCore.ParameterSet.Config as cms

def PythiaFilterHT(*args, **kwargs):
  mod = cms.EDFilter('PythiaFilterHT',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

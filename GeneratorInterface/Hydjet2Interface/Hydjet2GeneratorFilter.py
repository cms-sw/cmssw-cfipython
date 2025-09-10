import FWCore.ParameterSet.Config as cms

def Hydjet2GeneratorFilter(*args, **kwargs):
  mod = cms.EDFilter('Hydjet2GeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

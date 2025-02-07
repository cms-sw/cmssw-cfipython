import FWCore.ParameterSet.Config as cms

def PythiaHLTSoupFilter(*args, **kwargs):
  mod = cms.EDFilter('PythiaHLTSoupFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

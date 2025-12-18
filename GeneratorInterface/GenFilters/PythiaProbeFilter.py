import FWCore.ParameterSet.Config as cms

def PythiaProbeFilter(*args, **kwargs):
  mod = cms.EDFilter('PythiaProbeFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

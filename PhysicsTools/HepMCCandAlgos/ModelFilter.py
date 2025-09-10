import FWCore.ParameterSet.Config as cms

def ModelFilter(*args, **kwargs):
  mod = cms.EDFilter('ModelFilter',
    source = cms.required.InputTag,
    modelTag = cms.required.string,
    parameterMins = cms.required.vdouble,
    parameterMaxs = cms.required.vdouble,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def ModelFilter(**kwargs):
  mod = cms.EDFilter('ModelFilter',
    source = cms.required.InputTag,
    modelTag = cms.required.string,
    parameterMins = cms.required.vdouble,
    parameterMaxs = cms.required.vdouble,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

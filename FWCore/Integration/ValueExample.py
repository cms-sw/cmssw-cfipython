import FWCore.ParameterSet.Config as cms

def ValueExample(**kwargs):
  mod = cms.Service('ValueExample',
    value = cms.required.int32
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

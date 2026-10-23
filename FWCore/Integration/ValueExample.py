import FWCore.ParameterSet.Config as cms

def ValueExample(*args, **kwargs):
  mod = cms.Service('ValueExample',
    value = cms.required.int32
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

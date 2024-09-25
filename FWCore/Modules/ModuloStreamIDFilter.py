import FWCore.ParameterSet.Config as cms

def ModuloStreamIDFilter(*args, **kwargs):
  mod = cms.EDFilter('ModuloStreamIDFilter',
    modulo = cms.required.uint32,
    offset = cms.required.uint32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

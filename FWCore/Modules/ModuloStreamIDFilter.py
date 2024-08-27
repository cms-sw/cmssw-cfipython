import FWCore.ParameterSet.Config as cms

def ModuloStreamIDFilter(**kwargs):
  mod = cms.EDFilter('ModuloStreamIDFilter',
    modulo = cms.required.uint32,
    offset = cms.required.uint32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

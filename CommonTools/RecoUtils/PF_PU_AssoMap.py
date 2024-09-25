import FWCore.ParameterSet.Config as cms

def PF_PU_AssoMap(*args, **kwargs):
  mod = cms.EDProducer('PF_PU_AssoMap',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def PFMET(*args, **kwargs):
  mod = cms.EDProducer('PFMET',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

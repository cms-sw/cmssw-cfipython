import FWCore.ParameterSet.Config as cms

def DTDataIntegrityTask(*args, **kwargs):
  mod = cms.EDProducer('DTDataIntegrityTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

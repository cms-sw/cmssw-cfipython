import FWCore.ParameterSet.Config as cms

def ESIntegrityTask(*args, **kwargs):
  mod = cms.EDProducer('ESIntegrityTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def ESIntegrityTask(**kwargs):
  mod = cms.EDProducer('ESIntegrityTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

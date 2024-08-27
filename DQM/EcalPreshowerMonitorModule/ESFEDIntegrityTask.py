import FWCore.ParameterSet.Config as cms

def ESFEDIntegrityTask(**kwargs):
  mod = cms.EDProducer('ESFEDIntegrityTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

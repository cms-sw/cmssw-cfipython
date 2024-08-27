import FWCore.ParameterSet.Config as cms

def DTDataIntegrityTask(**kwargs):
  mod = cms.EDProducer('DTDataIntegrityTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

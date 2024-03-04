import FWCore.ParameterSet.Config as cms

def DTDataIntegrityROSOffline(**kwargs):
  mod = cms.EDProducer('DTDataIntegrityROSOffline',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def DTDataIntegrityROSOffline(*args, **kwargs):
  mod = cms.EDProducer('DTDataIntegrityROSOffline',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

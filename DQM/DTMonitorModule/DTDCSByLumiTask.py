import FWCore.ParameterSet.Config as cms

def DTDCSByLumiTask(*args, **kwargs):
  mod = cms.EDProducer('DTDCSByLumiTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

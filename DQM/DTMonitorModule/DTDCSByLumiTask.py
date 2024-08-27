import FWCore.ParameterSet.Config as cms

def DTDCSByLumiTask(**kwargs):
  mod = cms.EDProducer('DTDCSByLumiTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def DTDDUFileReader(**kwargs):
  mod = cms.EDProducer('DTDDUFileReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

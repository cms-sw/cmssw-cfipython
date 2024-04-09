import FWCore.ParameterSet.Config as cms

def L1TEMTFEventInfoClient(**kwargs):
  mod = cms.EDProducer('L1TEMTFEventInfoClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
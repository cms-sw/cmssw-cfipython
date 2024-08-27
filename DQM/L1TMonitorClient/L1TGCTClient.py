import FWCore.ParameterSet.Config as cms

def L1TGCTClient(**kwargs):
  mod = cms.EDProducer('L1TGCTClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

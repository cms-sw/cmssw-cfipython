import FWCore.ParameterSet.Config as cms

def L1TCSCTFClient(**kwargs):
  mod = cms.EDProducer('L1TCSCTFClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

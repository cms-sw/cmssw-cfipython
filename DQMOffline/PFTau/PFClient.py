import FWCore.ParameterSet.Config as cms

def PFClient(**kwargs):
  mod = cms.EDProducer('PFClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

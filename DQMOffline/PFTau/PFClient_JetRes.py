import FWCore.ParameterSet.Config as cms

def PFClient_JetRes(**kwargs):
  mod = cms.EDProducer('PFClient_JetRes',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

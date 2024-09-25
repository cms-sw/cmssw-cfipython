import FWCore.ParameterSet.Config as cms

def PFClient_JetRes(*args, **kwargs):
  mod = cms.EDProducer('PFClient_JetRes',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

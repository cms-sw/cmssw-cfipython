import FWCore.ParameterSet.Config as cms

def PFClient(*args, **kwargs):
  mod = cms.EDProducer('PFClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

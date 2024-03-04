import FWCore.ParameterSet.Config as cms

def PFLinker(**kwargs):
  mod = cms.EDProducer('PFLinker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

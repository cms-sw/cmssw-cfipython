import FWCore.ParameterSet.Config as cms

def PFV0Producer(**kwargs):
  mod = cms.EDProducer('PFV0Producer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

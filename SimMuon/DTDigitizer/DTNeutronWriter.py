import FWCore.ParameterSet.Config as cms

def DTNeutronWriter(**kwargs):
  mod = cms.EDProducer('DTNeutronWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

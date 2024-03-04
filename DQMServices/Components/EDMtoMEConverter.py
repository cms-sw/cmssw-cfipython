import FWCore.ParameterSet.Config as cms

def EDMtoMEConverter(**kwargs):
  mod = cms.EDProducer('EDMtoMEConverter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

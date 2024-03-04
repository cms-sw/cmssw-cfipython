import FWCore.ParameterSet.Config as cms

def V0Monitor(**kwargs):
  mod = cms.EDProducer('V0Monitor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

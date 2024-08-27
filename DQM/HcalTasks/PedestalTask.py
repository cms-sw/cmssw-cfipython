import FWCore.ParameterSet.Config as cms

def PedestalTask(**kwargs):
  mod = cms.EDProducer('PedestalTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

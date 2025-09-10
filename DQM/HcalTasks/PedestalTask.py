import FWCore.ParameterSet.Config as cms

def PedestalTask(*args, **kwargs):
  mod = cms.EDProducer('PedestalTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

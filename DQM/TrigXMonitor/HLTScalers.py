import FWCore.ParameterSet.Config as cms

def HLTScalers(**kwargs):
  mod = cms.EDProducer('HLTScalers',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

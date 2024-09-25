import FWCore.ParameterSet.Config as cms

def IntProducerEndProcessBlock(*args, **kwargs):
  mod = cms.EDProducer('IntProducerEndProcessBlock',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

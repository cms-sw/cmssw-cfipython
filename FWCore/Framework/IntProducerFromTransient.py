import FWCore.ParameterSet.Config as cms

def IntProducerFromTransient(*args, **kwargs):
  mod = cms.EDProducer('IntProducerFromTransient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

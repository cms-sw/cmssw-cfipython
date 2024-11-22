import FWCore.ParameterSet.Config as cms

def PFMETProducerMVA(*args, **kwargs):
  mod = cms.EDProducer('PFMETProducerMVA',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

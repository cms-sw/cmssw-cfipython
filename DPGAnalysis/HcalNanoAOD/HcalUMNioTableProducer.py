import FWCore.ParameterSet.Config as cms

def HcalUMNioTableProducer(*args, **kwargs):
  mod = cms.EDProducer('HcalUMNioTableProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

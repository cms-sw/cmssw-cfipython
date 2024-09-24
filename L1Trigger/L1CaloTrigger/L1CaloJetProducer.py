import FWCore.ParameterSet.Config as cms

def L1CaloJetProducer(*args, **kwargs):
  mod = cms.EDProducer('L1CaloJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

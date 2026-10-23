import FWCore.ParameterSet.Config as cms

def L1CaloJetHTTProducer(*args, **kwargs):
  mod = cms.EDProducer('L1CaloJetHTTProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

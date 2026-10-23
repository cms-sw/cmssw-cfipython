import FWCore.ParameterSet.Config as cms

def DispJetTableProducer(*args, **kwargs):
  mod = cms.EDProducer('DispJetTableProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

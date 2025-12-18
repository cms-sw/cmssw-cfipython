import FWCore.ParameterSet.Config as cms

def NoPileUpPFMEtProducer(*args, **kwargs):
  mod = cms.EDProducer('NoPileUpPFMEtProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

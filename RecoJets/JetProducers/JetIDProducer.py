import FWCore.ParameterSet.Config as cms

def JetIDProducer(*args, **kwargs):
  mod = cms.EDProducer('JetIDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

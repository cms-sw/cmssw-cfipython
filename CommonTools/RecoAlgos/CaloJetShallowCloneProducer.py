import FWCore.ParameterSet.Config as cms

def CaloJetShallowCloneProducer(*args, **kwargs):
  mod = cms.EDProducer('CaloJetShallowCloneProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

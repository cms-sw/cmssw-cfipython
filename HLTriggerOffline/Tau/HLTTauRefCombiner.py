import FWCore.ParameterSet.Config as cms

def HLTTauRefCombiner(**kwargs):
  mod = cms.EDProducer('HLTTauRefCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

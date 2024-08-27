import FWCore.ParameterSet.Config as cms

def HLTTauRefProducer(**kwargs):
  mod = cms.EDProducer('HLTTauRefProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

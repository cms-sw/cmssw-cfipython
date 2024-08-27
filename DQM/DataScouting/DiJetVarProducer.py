import FWCore.ParameterSet.Config as cms

def DiJetVarProducer(**kwargs):
  mod = cms.EDProducer('DiJetVarProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def AlphaTVarProducer(**kwargs):
  mod = cms.EDProducer('AlphaTVarProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

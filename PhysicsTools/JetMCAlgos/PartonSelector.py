import FWCore.ParameterSet.Config as cms

def PartonSelector(**kwargs):
  mod = cms.EDProducer('PartonSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

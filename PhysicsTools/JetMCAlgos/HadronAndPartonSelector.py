import FWCore.ParameterSet.Config as cms

def HadronAndPartonSelector(**kwargs):
  mod = cms.EDProducer('HadronAndPartonSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

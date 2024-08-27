import FWCore.ParameterSet.Config as cms

def PFJetFromFwdPtrProducer(**kwargs):
  mod = cms.EDProducer('PFJetFromFwdPtrProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

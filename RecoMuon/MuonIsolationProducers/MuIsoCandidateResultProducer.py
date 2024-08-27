import FWCore.ParameterSet.Config as cms

def MuIsoCandidateResultProducer(**kwargs):
  mod = cms.EDProducer('MuIsoCandidateResultProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def PFCandMETcorrInputProducer(**kwargs):
  mod = cms.EDProducer('PFCandMETcorrInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

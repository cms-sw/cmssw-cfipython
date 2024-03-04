import FWCore.ParameterSet.Config as cms

def Type0PFMETcorrInputProducer(**kwargs):
  mod = cms.EDProducer('Type0PFMETcorrInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

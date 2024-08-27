import FWCore.ParameterSet.Config as cms

def MultShiftMETcorrInputProducer(**kwargs):
  mod = cms.EDProducer('MultShiftMETcorrInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

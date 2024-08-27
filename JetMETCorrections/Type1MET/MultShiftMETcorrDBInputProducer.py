import FWCore.ParameterSet.Config as cms

def MultShiftMETcorrDBInputProducer(**kwargs):
  mod = cms.EDProducer('MultShiftMETcorrDBInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

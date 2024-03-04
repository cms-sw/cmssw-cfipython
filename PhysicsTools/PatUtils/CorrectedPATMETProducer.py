import FWCore.ParameterSet.Config as cms

def CorrectedPATMETProducer(**kwargs):
  mod = cms.EDProducer('CorrectedPATMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

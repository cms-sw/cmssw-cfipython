import FWCore.ParameterSet.Config as cms

def MuonTimingProducer(**kwargs):
  mod = cms.EDProducer('MuonTimingProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

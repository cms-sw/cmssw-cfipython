import FWCore.ParameterSet.Config as cms

def MuonShowerInformationProducer(**kwargs):
  mod = cms.EDProducer('MuonShowerInformationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

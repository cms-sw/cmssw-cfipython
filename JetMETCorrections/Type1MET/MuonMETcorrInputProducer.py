import FWCore.ParameterSet.Config as cms

def MuonMETcorrInputProducer(**kwargs):
  mod = cms.EDProducer('MuonMETcorrInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

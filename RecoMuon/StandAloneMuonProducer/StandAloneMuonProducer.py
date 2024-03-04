import FWCore.ParameterSet.Config as cms

def StandAloneMuonProducer(**kwargs):
  mod = cms.EDProducer('StandAloneMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

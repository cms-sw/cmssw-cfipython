import FWCore.ParameterSet.Config as cms

def MuonCalIsolationProducer(**kwargs):
  mod = cms.EDProducer('MuonCalIsolationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

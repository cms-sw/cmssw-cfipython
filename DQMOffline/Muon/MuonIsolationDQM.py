import FWCore.ParameterSet.Config as cms

def MuonIsolationDQM(**kwargs):
  mod = cms.EDProducer('MuonIsolationDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

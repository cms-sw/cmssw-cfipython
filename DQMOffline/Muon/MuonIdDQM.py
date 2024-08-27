import FWCore.ParameterSet.Config as cms

def MuonIdDQM(**kwargs):
  mod = cms.EDProducer('MuonIdDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

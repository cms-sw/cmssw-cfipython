import FWCore.ParameterSet.Config as cms

def MuonTestSummary(**kwargs):
  mod = cms.EDProducer('MuonTestSummary',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

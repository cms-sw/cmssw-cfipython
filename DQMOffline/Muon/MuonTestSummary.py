import FWCore.ParameterSet.Config as cms

def MuonTestSummary(*args, **kwargs):
  mod = cms.EDProducer('MuonTestSummary',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

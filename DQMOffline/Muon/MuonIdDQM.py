import FWCore.ParameterSet.Config as cms

def MuonIdDQM(*args, **kwargs):
  mod = cms.EDProducer('MuonIdDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

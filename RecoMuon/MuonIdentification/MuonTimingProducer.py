import FWCore.ParameterSet.Config as cms

def MuonTimingProducer(*args, **kwargs):
  mod = cms.EDProducer('MuonTimingProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def MuonTiming(*args, **kwargs):
  mod = cms.EDProducer('MuonTiming',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def MuonFromPVSelector(*args, **kwargs):
  mod = cms.EDProducer('MuonFromPVSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def MuonTrackResidualsTest(*args, **kwargs):
  mod = cms.EDProducer('MuonTrackResidualsTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

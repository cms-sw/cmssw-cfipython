import FWCore.ParameterSet.Config as cms

def AlignmentMuonHIPTrajectorySelector(*args, **kwargs):
  mod = cms.EDProducer('AlignmentMuonHIPTrajectorySelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

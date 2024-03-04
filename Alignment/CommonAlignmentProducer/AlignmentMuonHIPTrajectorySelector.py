import FWCore.ParameterSet.Config as cms

def AlignmentMuonHIPTrajectorySelector(**kwargs):
  mod = cms.EDProducer('AlignmentMuonHIPTrajectorySelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

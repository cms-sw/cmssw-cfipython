import FWCore.ParameterSet.Config as cms

def SiStripCPEAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripCPEAnalyzer',
    tracks = cms.untracked.InputTag('generalTracks'),
    trajectories = cms.untracked.InputTag('generalTracks'),
    association = cms.untracked.InputTag('generalTracks'),
    clusters = cms.untracked.InputTag('siStripClusters'),
    StripCPE = cms.ESInputTag('StripCPEfromTrackAngleESProducer', 'StripCPEfromTrackAngle'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

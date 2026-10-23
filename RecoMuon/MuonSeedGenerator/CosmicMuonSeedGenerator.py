import FWCore.ParameterSet.Config as cms

def CosmicMuonSeedGenerator(*args, **kwargs):
  mod = cms.EDProducer('CosmicMuonSeedGenerator',
    EnableDTMeasurement = cms.bool(True),
    EnableCSCMeasurement = cms.bool(True),
    DTRecSegmentLabel = cms.InputTag('dt4DSegments'),
    CSCRecSegmentLabel = cms.InputTag('cscSegments'),
    MaxSeeds = cms.int32(1000),
    MaxDTChi2 = cms.double(300),
    MaxCSCChi2 = cms.double(300),
    ForcePointDown = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

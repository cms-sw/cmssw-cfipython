import FWCore.ParameterSet.Config as cms

def ScoutingTrackMonitor(*args, **kwargs):
  mod = cms.EDProducer('ScoutingTrackMonitor',
    tracks = cms.InputTag('hltScoutingTrackPacker'),
    vertices = cms.InputTag('hltScoutingPrimaryVertexPacker', 'primaryVtx'),
    topFolderName = cms.string('HLT/ScoutingOffline/Tracks'),
    DxyBin = cms.int32(100),
    DxyMin = cms.double(-5000),
    DxyMax = cms.double(5000),
    DzBin = cms.int32(100),
    DzMin = cms.double(-2000),
    DzMax = cms.double(2000),
    PhiBin = cms.int32(32),
    PhiMin = cms.double(-3.1415926535897931),
    PhiMax = cms.double(3.1415926535897931),
    EtaBin = cms.int32(26),
    EtaMin = cms.double(-3),
    EtaMax = cms.double(3),
    PtBin = cms.int32(49),
    PtMin = cms.double(1),
    PtMax = cms.double(50),
    PhiBin2D = cms.int32(12),
    EtaBin2D = cms.int32(8),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

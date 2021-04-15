import FWCore.ParameterSet.Config as cms

hltScoutingTrackProducer = cms.EDProducer('HLTScoutingTrackProducer',
  OtherTracks = cms.InputTag('hltPixelTracksL3MuonNoVtx'),
  vertexCollection = cms.InputTag('hltPixelVertices'),
  mantissaPrecision = cms.int32(10),
  vtxMinDist = cms.double(0.01),
  mightGet = cms.optional.untracked.vstring
)

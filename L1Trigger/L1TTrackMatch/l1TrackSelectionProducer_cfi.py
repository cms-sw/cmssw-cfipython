import FWCore.ParameterSet.Config as cms

l1TrackSelectionProducer = cms.EDProducer('L1TrackSelectionProducer',
  l1TracksInputTag = cms.InputTag('TTTracksFromTrackletEmulation', 'Level1TTTracks'),
  outputCollectionName = cms.string('Level1TTTracksSelected'),
  cutSet = cms.PSet(
    ptMin = cms.double(2),
    absEtaMax = cms.double(2.4),
    absZ0Max = cms.double(15),
    nStubsMin = cms.int32(4),
    nPSStubsMin = cms.int32(0),
    reducedBendChi2Max = cms.double(2.25),
    reducedChi2RZMax = cms.double(5),
    reducedChi2RPhiMax = cms.double(20)
  ),
  processSimulatedTracks = cms.bool(True),
  processEmulatedTracks = cms.bool(True),
  debug = cms.int32(0),
  mightGet = cms.optional.untracked.vstring
)

import FWCore.ParameterSet.Config as cms

l1TrackSelectionProducer = cms.EDProducer('L1TrackSelectionProducer',
  l1TracksInputTag = cms.InputTag('TTTracksFromTrackletEmulation', 'Level1TTTracks'),
  l1VerticesInputTag = cms.InputTag('L1VertexFinder', 'l1vertices'),
  l1VerticesEmulationInputTag = cms.InputTag('L1VertexFinderEmulator', 'l1verticesEmulation'),
  outputCollectionName = cms.string('Level1TTTracksSelected'),
  cutSet = cms.PSet(
    ptMin = cms.double(2),
    absEtaMax = cms.double(2.4),
    absZ0Max = cms.double(15),
    nStubsMin = cms.int32(4),
    nPSStubsMin = cms.int32(0),
    reducedBendChi2Max = cms.double(2.25),
    reducedChi2RZMax = cms.double(5),
    reducedChi2RPhiMax = cms.double(20),
    deltaZMaxEtaBounds = cms.vdouble(
      0,
      0.7,
      1,
      1.2,
      1.6,
      2,
      2.4
    ),
    deltaZMax = cms.vdouble(
      0.37,
      0.5,
      0.6,
      0.75,
      1,
      1.6
    )
  ),
  useDisplacedTracksDeltaZOverride = cms.double(-1),
  processSimulatedTracks = cms.bool(True),
  processEmulatedTracks = cms.bool(True),
  debug = cms.int32(0),
  mightGet = cms.optional.untracked.vstring
)

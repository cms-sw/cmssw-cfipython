import FWCore.ParameterSet.Config as cms

l1tTrackJetsEmulator = cms.EDProducer('L1TrackJetEmulatorProducer',
  L1TrackInputTag = cms.InputTag('l1tTTTracksFromTrackletEmulation', 'Level1TTTracks'),
  L1PVertexInputTag = cms.InputTag('l1tVertexFinderEmulator', 'L1VerticesEmulation'),
  MaxDzTrackPV = cms.double(1),
  trk_zMax = cms.double(15),
  trk_ptMax = cms.double(200),
  trk_ptMin = cms.double(3),
  trk_etaMax = cms.double(2.4),
  nStubs4PromptChi2 = cms.double(5),
  nStubs4PromptBend = cms.double(1.7),
  nStubs5PromptChi2 = cms.double(2.75),
  nStubs5PromptBend = cms.double(3.5),
  trk_nPSStubMin = cms.int32(-1),
  minTrkJetpT = cms.double(-1),
  etaBins = cms.int32(24),
  phiBins = cms.int32(27),
  zBins = cms.int32(1),
  d0_cutNStubs4 = cms.double(-1),
  d0_cutNStubs5 = cms.double(-1),
  lowpTJetMinTrackMultiplicity = cms.int32(2),
  lowpTJetThreshold = cms.double(50),
  highpTJetMinTrackMultiplicity = cms.int32(3),
  highpTJetThreshold = cms.double(100),
  displaced = cms.bool(False),
  nStubs4DisplacedChi2 = cms.double(5),
  nStubs4DisplacedBend = cms.double(1.7),
  nStubs5DisplacedChi2 = cms.double(2.75),
  nStubs5DisplacedBend = cms.double(3.5),
  nDisplacedTracks = cms.int32(2),
  mightGet = cms.optional.untracked.vstring
)

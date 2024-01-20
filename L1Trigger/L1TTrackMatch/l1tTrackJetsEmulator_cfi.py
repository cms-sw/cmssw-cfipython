import FWCore.ParameterSet.Config as cms

l1tTrackJetsEmulator = cms.EDProducer('L1TrackJetEmulatorProducer',
  L1TrackInputTag = cms.InputTag('l1tTTTracksFromTrackletEmulation', 'Level1TTTracks'),
  trk_zMax = cms.double(15),
  trk_ptMax = cms.double(200),
  trk_etaMax = cms.double(2.4),
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
  nDisplacedTracks = cms.int32(2),
  mightGet = cms.optional.untracked.vstring
)

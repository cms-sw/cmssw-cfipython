import FWCore.ParameterSet.Config as cms

L1TkElectronsEllipticMatchHGC = cms.EDProducer('L1TkElectronTrackProducer',
  label = cms.string('EG'),
  L1EGammaInputTag = cms.InputTag('l1EGammaEEProducer', 'L1EGammaCollectionBXVWithCuts'),
  ETmin = cms.double(-1),
  L1TrackInputTag = cms.InputTag('TTTracksFromTrackletEmulation', 'Level1TTTracks'),
  TrackChi2 = cms.double(10000000000),
  TrackMinPt = cms.double(10),
  useTwoStubsPT = cms.bool(False),
  useClusterET = cms.bool(False),
  TrackEGammaMatchType = cms.string('EllipticalCut'),
  TrackEGammaDeltaPhi = cms.vdouble(
    0.07,
    0,
    0
  ),
  TrackEGammaDeltaR = cms.vdouble(
    0.08,
    0,
    0
  ),
  TrackEGammaDeltaEta = cms.vdouble(
    0.01,
    0.01,
    10000000000
  ),
  RelativeIsolation = cms.bool(True),
  IsoCut = cms.double(-0.1),
  PTMINTRA = cms.double(2),
  DRmin = cms.double(0.03),
  DRmax = cms.double(0.2),
  maxChi2IsoTracks = cms.double(100),
  minNStubsIsoTracks = cms.int32(4),
  DeltaZ = cms.double(0.6),
  mightGet = cms.optional.untracked.vstring
)

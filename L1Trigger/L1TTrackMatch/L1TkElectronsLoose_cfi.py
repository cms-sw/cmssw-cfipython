import FWCore.ParameterSet.Config as cms

L1TkElectronsLoose = cms.EDProducer('L1TkElectronTrackProducer',
  label = cms.string('EG'),
  L1EGammaInputTag = cms.InputTag('simCaloStage2Digis'),
  ETmin = cms.double(-1),
  L1TrackInputTag = cms.InputTag('TTTracksFromTrackletEmulation', 'Level1TTTracks'),
  TrackChi2 = cms.double(10000000000),
  TrackMinPt = cms.double(3),
  useTwoStubsPT = cms.bool(False),
  useClusterET = cms.bool(False),
  TrackEGammaMatchType = cms.string('PtDependentCut'),
  TrackEGammaDeltaPhi = cms.vdouble(
    0.07,
    0,
    0
  ),
  TrackEGammaDeltaR = cms.vdouble(
    0.12,
    0,
    0
  ),
  TrackEGammaDeltaEta = cms.vdouble(
    10000000000,
    0,
    0
  ),
  RelativeIsolation = cms.bool(True),
  IsoCut = cms.double(-0.1),
  PTMINTRA = cms.double(2),
  DRmin = cms.double(0.03),
  DRmax = cms.double(0.2),
  maxChi2IsoTracks = cms.double(10000000000),
  minNStubsIsoTracks = cms.int32(0),
  DeltaZ = cms.double(0.6),
  mightGet = cms.optional.untracked.vstring
)

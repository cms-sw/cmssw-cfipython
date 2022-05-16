import FWCore.ParameterSet.Config as cms

L1TkGlbMuons = cms.EDProducer('L1TkGlbMuonProducer',
  L1MuonInputTag = cms.InputTag('simGmtStage2Digis'),
  L1TrackInputTag = cms.InputTag('TTTracksFromTrackletEmulation', 'Level1TTTracks'),
  ETAMIN = cms.double(0),
  ETAMAX = cms.double(5),
  ZMAX = cms.double(25),
  CHI2MAX = cms.double(100),
  PTMINTRA = cms.double(2),
  DRmax = cms.double(0.5),
  nStubsmin = cms.int32(4),
  correctGMTPropForTkZ = cms.bool(True),
  use5ParameterFit = cms.bool(False),
  useTPMatchWindows = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)

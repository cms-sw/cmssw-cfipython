import FWCore.ParameterSet.Config as cms

l1TkEmParticleProducer = cms.EDProducer('L1TkEmParticleProducer',
  label = cms.string('EG'),
  L1EGammaInputTag = cms.InputTag('simCaloStage2Digis'),
  L1TrackInputTag = cms.InputTag('TTTracksFromTrackletEmulation', 'Level1TTTracks'),
  L1VertexInputTag = cms.InputTag('L1TkPrimaryVertex'),
  ETmin = cms.double(-1),
  RelativeIsolation = cms.bool(True),
  IsoCut = cms.double(0.23),
  ZMAX = cms.double(25),
  CHI2MAX = cms.double(100),
  PTMINTRA = cms.double(2),
  DRmin = cms.double(0.07),
  DRmax = cms.double(0.3),
  PrimaryVtxConstrain = cms.bool(False),
  DeltaZMax = cms.double(0.6),
  mightGet = cms.optional.untracked.vstring
)

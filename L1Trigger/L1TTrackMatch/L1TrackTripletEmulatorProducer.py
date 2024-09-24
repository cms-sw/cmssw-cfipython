import FWCore.ParameterSet.Config as cms

def L1TrackTripletEmulatorProducer(*args, **kwargs):
  mod = cms.EDProducer('L1TrackTripletEmulatorProducer',
    L1TrackInputTag = cms.InputTag('l1tTTTracksFromTrackletEmulation', 'Level1TTTracks'),
    L1PVertexInputTag = cms.InputTag('l1tVertexFinderEmulator', 'L1VerticesEmulation'),
    trk1_ptMin = cms.double(-1),
    trk1_absEtaMax = cms.double(100000000),
    trk1_mvaMin = cms.double(-1),
    trk1_nstubMin = cms.int32(-1),
    trk1_dzMax = cms.double(100000000),
    trk1_mass = cms.double(0.139),
    trk2_ptMin = cms.double(-1),
    trk2_absEtaMax = cms.double(100000000),
    trk2_mvaMin = cms.double(-1),
    trk2_nstubMin = cms.int32(-1),
    trk2_dzMax = cms.double(100000000),
    trk2_mass = cms.double(0.139),
    trk3_ptMin = cms.double(-1),
    trk3_absEtaMax = cms.double(100000000),
    trk3_mvaMin = cms.double(-1),
    trk3_nstubMin = cms.int32(0),
    trk3_dzMax = cms.double(100000000),
    trk3_mass = cms.double(0.139),
    displaced = cms.bool(False),
    triplet_massMin = cms.double(-1),
    triplet_massMax = cms.double(100000000),
    triplet_absEtaMin = cms.double(-1),
    triplet_absEtaMax = cms.double(100000000),
    triplet_ptMin = cms.double(-1),
    triplet_ptMax = cms.double(100000000),
    triplet_absCharge = cms.int32(-1),
    triplet_massOverflow = cms.double(1000),
    pair1_massMin = cms.double(-1),
    pair1_massMax = cms.double(100000000),
    pair2_massMin = cms.double(-1),
    pair2_massMax = cms.double(100000000),
    pair1_dzMin = cms.double(-1),
    pair1_dzMax = cms.double(100000000),
    pair2_dzMin = cms.double(-1),
    pair2_dzMax = cms.double(100000000),
    float_precision = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def L1TruthTrackFastJetProducer(*args, **kwargs):
  mod = cms.EDProducer('L1TruthTrackFastJetProducer',
    L1TrackInputTag = cms.InputTag('l1tTTTracksFromTrackletEmulation', 'Level1TTTracks'),
    MCTruthTrackInputTag = cms.InputTag('TTTrackAssociatorFromPixelDigis', 'Level1TTTracks'),
    trk_zMax = cms.double(15),
    trk_ptMin = cms.double(2),
    trk_etaMax = cms.double(2.4),
    trk_nStubMin = cms.int32(4),
    trk_nPSStubMin = cms.int32(-1),
    coneSize = cms.double(0.4),
    displaced = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

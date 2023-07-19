import FWCore.ParameterSet.Config as cms

L1FastTrackingJets = cms.EDProducer('L1FastTrackingJetProducer',
  L1TrackInputTag = cms.InputTag('l1tTTTracksFromTrackletEmulation', 'Level1TTTracks'),
  L1PrimaryVertexTag = cms.string('l1vertices'),
  GenInfo = cms.InputTag('TTTrackAssociatorFromPixelDigis', 'Level1TTTracks'),
  trk_zMax = cms.double(15),
  trk_chi2dofMax = cms.double(10),
  trk_bendChi2Max = cms.double(2.2),
  trk_ptMin = cms.double(2),
  trk_etaMax = cms.double(2.5),
  trk_nStubMin = cms.int32(4),
  trk_nPSStubMin = cms.int32(-1),
  deltaZ0Cut = cms.double(0.5),
  doTightChi2 = cms.bool(True),
  trk_ptTightChi2 = cms.double(20),
  trk_chi2dofTightChi2 = cms.double(5),
  coneSize = cms.double(0.4),
  displaced = cms.bool(False),
  selectTrkMatchGenTight = cms.bool(True),
  selectTrkMatchGenLoose = cms.bool(False),
  selectTrkMatchGenOrPU = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)

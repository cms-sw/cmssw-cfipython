import FWCore.ParameterSet.Config as cms

hltEgammaHLTEleL1TrackIsolProducer = cms.EDProducer('EgammaHLTEleL1TrackIsolProducer',
  ecalCands = cms.InputTag('hltEgammaCandidates'),
  eles = cms.InputTag('hltEgammaGsfElectrons'),
  l1Tracks = cms.InputTag('TTTracksFromTrackletEmulation', 'Level1TTTracks'),
  isolCfg = cms.PSet(
    useAbsEta = cms.bool(True),
    etaBoundaries = cms.vdouble(1.5),
    trkCuts = cms.VPSet(
      cms.PSet(),
      cms.PSet()
    )
  ),
  mightGet = cms.optional.untracked.vstring
)

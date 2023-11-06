import FWCore.ParameterSet.Config as cms

hltEgammaHLTGsfTrackVarProducer = cms.EDProducer('EgammaHLTGsfTrackVarProducer',
  recoEcalCandidateProducer = cms.InputTag('hltRecoEcalSuperClusterActivityCandidate'),
  inputCollection = cms.InputTag('hltActivityElectronGsfTracks'),
  beamSpotProducer = cms.InputTag('hltOnlineBeamSpot'),
  upperTrackNrToRemoveCut = cms.int32(9999),
  lowerTrackNrToRemoveCut = cms.int32(-1),
  useDefaultValuesForBarrel = cms.bool(False),
  useDefaultValuesForEndcap = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)

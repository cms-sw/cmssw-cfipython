import FWCore.ParameterSet.Config as cms

def EgammaHLTGsfTrackVarProducer(**kwargs):
  mod = cms.EDProducer('EgammaHLTGsfTrackVarProducer',
    recoEcalCandidateProducer = cms.InputTag('hltRecoEcalSuperClusterActivityCandidate'),
    inputCollection = cms.InputTag('hltActivityElectronGsfTracks'),
    beamSpotProducer = cms.InputTag('hltOnlineBeamSpot'),
    upperTrackNrToRemoveCut = cms.int32(9999),
    lowerTrackNrToRemoveCut = cms.int32(-1),
    useDefaultValuesForBarrel = cms.bool(False),
    useDefaultValuesForEndcap = cms.bool(False),
    produceAbsValues = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

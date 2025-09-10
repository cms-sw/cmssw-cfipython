import FWCore.ParameterSet.Config as cms

def IsolatedTracksCone(*args, **kwargs):
  mod = cms.EDAnalyzer('IsolatedTracksCone',
    doMC = cms.untracked.bool(False),
    verbosity = cms.untracked.int32(1),
    useJetTrigger = cms.untracked.bool(False),
    drLeadJetVeto = cms.untracked.double(1.2),
    ptMinLeadJet = cms.untracked.double(15),
    debugTracks = cms.untracked.int32(0),
    printTrkHitPattern = cms.untracked.bool(True),
    minTrackP = cms.untracked.double(1),
    maxTrackEta = cms.untracked.double(2.6),
    maxNearTrackP = cms.untracked.double(1),
    debugEcalSimInfo = cms.untracked.bool(False),
    applyEcalIsolation = cms.untracked.bool(True),
    debugL1Info = cms.untracked.bool(False),
    L1extraTauJetSource = cms.InputTag('l1extraParticles', 'Tau'),
    L1extraCenJetSource = cms.InputTag('l1extraParticles', 'Central'),
    L1extraFwdJetSource = cms.InputTag('l1extraParticles', 'Forward'),
    TrackAssociatorParameters = cms.PSet(
      muonMaxDistanceSigmaX = cms.double(0),
      muonMaxDistanceSigmaY = cms.double(0),
      CSCSegmentCollectionLabel = cms.InputTag('cscSegments'),
      dRHcal = cms.double(9999),
      dREcal = cms.double(9999),
      CaloTowerCollectionLabel = cms.InputTag('towerMaker'),
      useEcal = cms.bool(True),
      dREcalPreselection = cms.double(0.05),
      HORecHitCollectionLabel = cms.InputTag('horeco'),
      dRMuon = cms.double(9999),
      crossedEnergyType = cms.string('SinglePointAlongTrajectory'),
      muonMaxDistanceX = cms.double(5),
      muonMaxDistanceY = cms.double(5),
      useHO = cms.bool(False),
      accountForTrajectoryChangeCalo = cms.bool(False),
      DTRecSegment4DCollectionLabel = cms.InputTag('dt4DSegments'),
      EERecHitCollectionLabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
      dRHcalPreselection = cms.double(0.2),
      useMuon = cms.bool(False),
      useCalo = cms.bool(True),
      EBRecHitCollectionLabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
      dRMuonPreselection = cms.double(0.2),
      truthMatch = cms.bool(False),
      HBHERecHitCollectionLabel = cms.InputTag('hbhereco'),
      useHcal = cms.bool(True),
      usePreshower = cms.bool(False),
      dRPreshowerPreselection = cms.double(0.2),
      trajectoryUncertaintyTolerance = cms.double(1)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def SimHitCaloHitDumper(*args, **kwargs):
  mod = cms.EDAnalyzer('SimHitCaloHitDumper',
    TrackerHitsPixelBarrelLowTof = cms.InputTag('g4SimHits', 'TrackerHitsPixelBarrelLowTof'),
    TrackerHitsPixelBarrelHighTof = cms.InputTag('g4SimHits', 'TrackerHitsPixelBarrelHighTof'),
    TrackerHitsPixelEndcapLowTof = cms.InputTag('g4SimHits', 'TrackerHitsPixelEndcapLowTof'),
    TrackerHitsPixelEndcapHighTof = cms.InputTag('g4SimHits', 'TrackerHitsPixelEndcapHighTof'),
    TrackerHitsTIBLowTof = cms.InputTag('g4SimHits', 'TrackerHitsTIBLowTof'),
    TrackerHitsTIBHighTof = cms.InputTag('g4SimHits', 'TrackerHitsTIBHighTof'),
    TrackerHitsTIDLowTof = cms.InputTag('g4SimHits', 'TrackerHitsTIDLowTof'),
    TrackerHitsTIDHighTof = cms.InputTag('g4SimHits', 'TrackerHitsTIDHighTof'),
    TrackerHitsTOBLowTof = cms.InputTag('g4SimHits', 'TrackerHitsTOBLowTof'),
    TrackerHitsTOBHighTof = cms.InputTag('g4SimHits', 'TrackerHitsTOBHighTof'),
    TrackerHitsTECLowTof = cms.InputTag('g4SimHits', 'TrackerHitsTECLowTof'),
    TrackerHitsTECHighTof = cms.InputTag('g4SimHits', 'TrackerHitsTECHighTof'),
    MuonDTHits = cms.InputTag('g4SimHits', 'MuonDTHits'),
    MuonCSCHits = cms.InputTag('g4SimHits', 'MuonCSCHits'),
    MuonRPCHits = cms.InputTag('g4SimHits', 'MuonRPCHits'),
    FastTimerHitsBarrel = cms.InputTag('g4SimHits', 'FastTimerHitsBarrel'),
    FastTimerHitsEndcap = cms.InputTag('g4SimHits', 'FastTimerHitsEndcap'),
    EcalHitsEB = cms.InputTag('g4SimHits', 'EcalHitsEB'),
    EcalHitsEE = cms.InputTag('g4SimHits', 'EcalHitsEE'),
    EcalHitsES = cms.InputTag('g4SimHits', 'EcalHitsES'),
    HcalHits = cms.InputTag('g4SimHits', 'HcalHits'),
    CaloHitsTk = cms.InputTag('g4SimHits', 'CaloHitsTk'),
    ZDCHITS = cms.InputTag('g4SimHits', 'ZDCHITS'),
    CastorTU = cms.InputTag('g4SimHits', 'CastorTU'),
    CastorPL = cms.InputTag('g4SimHits', 'CastorPL'),
    CastorFI = cms.InputTag('g4SimHits', 'CastorFI'),
    CastorBU = cms.InputTag('g4SimHits', 'CastorBU'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

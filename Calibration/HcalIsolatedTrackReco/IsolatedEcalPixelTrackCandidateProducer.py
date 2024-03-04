import FWCore.ParameterSet.Config as cms

def IsolatedEcalPixelTrackCandidateProducer(**kwargs):
  mod = cms.EDProducer('IsolatedEcalPixelTrackCandidateProducer',
    filterLabel = cms.InputTag('hltIsolPixelTrackL2Filter'),
    EBRecHitSource = cms.InputTag('hltEcalRecHit', 'EcalRecHitsEB'),
    EERecHitSource = cms.InputTag('hltEcalRecHit', 'EcalRecHitsEE'),
    EBHitEnergyThreshold = cms.double(0.1),
    EBHitCountEnergyThreshold = cms.double(0.5),
    EEHitEnergyThreshold0 = cms.double(-41.0664),
    EEHitEnergyThreshold1 = cms.double(68.795),
    EEHitEnergyThreshold2 = cms.double(-38.1483),
    EEHitEnergyThreshold3 = cms.double(7.04303),
    EEFacHitCountEnergyThreshold = cms.double(10),
    EcalConeSizeEta0 = cms.double(0.09),
    EcalConeSizeEta1 = cms.double(0.14),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

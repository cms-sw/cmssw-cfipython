import FWCore.ParameterSet.Config as cms

alCaPhiSymStream = cms.EDFilter('HLTEcalPhiSymFilter',
  barrelHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
  endcapHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
  statusThreshold = cms.uint32(3),
  useRecoFlag = cms.bool(False),
  eCut_barrel = cms.double(150),
  eCut_endcap = cms.double(750),
  eCut_barrel_high = cms.double(999999),
  eCut_endcap_high = cms.double(999999),
  phiSymBarrelHitCollection = cms.string('phiSymEcalRecHitsEB'),
  phiSymEndcapHitCollection = cms.string('phiSymEcalRecHitsEE')
)

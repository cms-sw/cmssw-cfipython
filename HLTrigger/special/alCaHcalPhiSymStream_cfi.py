import FWCore.ParameterSet.Config as cms

alCaHcalPhiSymStream = cms.EDFilter('HLTHcalPhiSymFilter',
  saveTags = cms.bool(True),
  HBHEHitCollection = cms.InputTag('hbhereco'),
  HOHitCollection = cms.InputTag('horeco'),
  HFHitCollection = cms.InputTag('hfreco'),
  eCut_HE = cms.double(-10),
  eCut_HF = cms.double(-10),
  eCut_HB = cms.double(-10),
  eCut_HO = cms.double(-10),
  phiSymHOHitCollection = cms.string('phiSymHcalRecHitsHO'),
  phiSymHBHEHitCollection = cms.string('phiSymHcalRecHitsHBHE'),
  phiSymHFHitCollection = cms.string('phiSymHcalRecHitsHF')
)

import FWCore.ParameterSet.Config as cms

hltHFAsymmetryFilter = cms.EDFilter('HLTHFAsymmetryFilter',
  HFHitCollection = cms.InputTag('hltHfreco'),
  ECut_HF = cms.double(3),
  OS_Asym_max = cms.double(0.2),
  SS_Asym_min = cms.double(0.8)
)

import FWCore.ParameterSet.Config as cms

hltPixelActivityHFSumEnergyFilter = cms.EDFilter('HLTPixelActivityHFSumEnergyFilter',
  inputTag = cms.InputTag('hltSiPixelClusters'),
  HFHitCollection = cms.InputTag('hltHfreco'),
  eCut_HF = cms.double(0),
  eMin_HF = cms.double(10000),
  offset = cms.double(-1000),
  slope = cms.double(0.5)
)

import FWCore.ParameterSet.Config as cms

hltCSCRing2or3Filter = cms.EDFilter('HLTCSCRing2or3Filter',
  saveTags = cms.bool(True),
  input = cms.InputTag('hltCsc2DRecHits'),
  minHits = cms.uint32(4),
  xWindow = cms.double(2),
  yWindow = cms.double(2)
)

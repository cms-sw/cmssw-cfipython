import FWCore.ParameterSet.Config as cms

hltDeDxFilter = cms.EDFilter('HLTDeDxFilter',
  saveTags = cms.bool(False),
  minDEDx = cms.double(0),
  minPT = cms.double(0),
  minNOM = cms.double(0),
  maxETA = cms.double(5.5),
  inputTracksTag = cms.InputTag('hltL3Mouns'),
  inputDeDxTag = cms.InputTag('HLTdedxHarm2')
)

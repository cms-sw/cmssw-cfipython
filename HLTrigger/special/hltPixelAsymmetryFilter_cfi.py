import FWCore.ParameterSet.Config as cms

hltPixelAsymmetryFilter = cms.EDFilter('HLTPixelAsymmetryFilter',
  saveTags = cms.bool(True),
  inputTag = cms.InputTag('hltSiPixelClusters'),
  MinAsym = cms.double(0),
  MaxAsym = cms.double(1),
  MinCharge = cms.double(4000),
  MinBarrel = cms.double(10000)
)

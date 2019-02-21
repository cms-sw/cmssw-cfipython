import FWCore.ParameterSet.Config as cms

PATJetSelector = cms.EDFilter('PATJetSelector',
  src = cms.InputTag('no default'),
  cut = cms.string(''),
  cutLoose = cms.string(''),
  filter = cms.bool(False),
  nLoose = cms.uint32(0)
)

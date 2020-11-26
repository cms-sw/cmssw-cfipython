import FWCore.ParameterSet.Config as cms

DoodadESSource = cms.ESSource('DoodadESSource',
  appendToDataLabel = cms.optional.string,
  test2 = cms.optional.untracked.string,
  test = cms.untracked.bool(False)
)

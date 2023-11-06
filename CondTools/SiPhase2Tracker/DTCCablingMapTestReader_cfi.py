import FWCore.ParameterSet.Config as cms

DTCCablingMapTestReader = cms.EDAnalyzer('DTCCablingMapTestReader',
  mightGet = cms.optional.untracked.vstring
)
